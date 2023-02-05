import sys
import importlib
import os

from feynmodel.feyn_model import FeynModel
from feynmodel.particle import Particle
from feynmodel.ufo_base_class import UFOBaseClass
from feynmodel.vertex import Vertex


def ufo_to_fm_particle(ufo_object, model):
    return model.get_particle(name=ufo_object.name, pdg_code=ufo_object.pdg_code)


def ufo_to_fm_parameter(ufo_object, model):
    return model.get_parameter(name=ufo_object.name)


def ufo_to_fm_lorentz(ufo_object, model):
    return model.get_lorentz(name=ufo_object.name)


def ufo_to_fm_couplings(ufo_object, model):
    return model.get_coupling(name=ufo_object.name)


def ufo_object_to_dict(ufo_object, model=None):
    """Convert an UFO object to a dictionary"""
    if isinstance(ufo_object, UFOBaseClass):
        # We have to replace all instances of the UFO particle class with the FeynModel particle class

        # Fix particle
        if "mass" in ufo_object.require_args:
            ufo_object.mass = ufo_to_fm_parameter(ufo_object.mass, model)
        if "width" in ufo_object.require_args:
            ufo_object.width = ufo_to_fm_parameter(ufo_object.width, model)

        # Fix vertex
        if "particles" in ufo_object.require_args:
            np = [ufo_to_fm_particle(p, model) for p in ufo_object.particles]
            ufo_object.particles = np
        # Fix decay
        if "lorentz" in ufo_object.require_args:  # ufo_object.__dict__:
            ufo_object.lorentz = ufo_to_fm_lorentz(ufo_object.lorentz, model)
        if "couplings" in ufo_object.require_args:  # ufo_object.__dict__:
            for k, v in ufo_object.partial_widths.items():
                ufo_object.couplings[k] = ufo_to_fm_couplings(v, model)
        # Fix decay
        if "particle" in ufo_object.require_args:  # ufo_object.__dict__:
            ufo_object.particle = ufo_to_fm_particle(ufo_object.particle, model)
        if "partial_widths" in ufo_object.require_args:  # ufo_object.__dict__:
            for k, v in ufo_object.partial_widths.items():
                ufo_object.partial_widths[
                    (ufo_to_fm_particle(k[0], model), ufo_to_fm_particle(k[2], model))
                ] = v

    return ufo_object.__dict__
    # return {key: ufo_object.__dict__[key] for key in ufo_object.require_args}


def import_ufo_model(model_path, model_name="imported_ufo_model"):
    # Add the model path to the PYTHONPATH
    # This fixes the imports in the UFO model
    sys.path.append(os.path.abspath(model_path))
    # Madgraph workaround
    # os.environ["PYTHONPATH"] += os.pathsep + os.path.dirname(model_path)
    # Load the UFO model
    spec = importlib.util.spec_from_file_location(
        model_name, os.path.abspath(model_path) + "/" + "__init__.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    model = module
    return model


def ufo_to_feynmodel(model, model_object=None, model_class=FeynModel):
    # Convert the UFO model to a FeynModel object
    if model_object is not None:
        if not isinstance(model_object, model_class):
            raise ValueError(
                f"model_object must be a {model_class} object. Use general FeynModel in case of doubt."
            )
        feynmodel = model_object
    elif model_class is not None:
        feynmodel = model_class()
    else:
        raise ValueError("model_object or model_class must be specified")
    for lorentz in model.all_lorentz:
        feynmodel.add_lorentz(Particle(**ufo_object_to_dict(lorentz, model=feynmodel)))
    for couplings in model.all_couplings:
        feynmodel.add_coupling(
            Particle(**ufo_object_to_dict(couplings, model=feynmodel))
        )
    for order in model.all_orders:
        feynmodel.add_order(Particle(**ufo_object_to_dict(order, model=feynmodel)))
    for function in model.all_functions:
        feynmodel.add_function(
            Particle(**ufo_object_to_dict(function, model=feynmodel))
        )
    for decay in model.all_decays:
        feynmodel.add_decay(Particle(**ufo_object_to_dict(decay, model=feynmodel)))
    for parameter in model.all_parameters:
        feynmodel.add_parameter(
            Particle(**ufo_object_to_dict(parameter, model=feynmodel))
        )
    for lorentz in model.all_lorentz:
        feynmodel.add_lorentz(Particle(**ufo_object_to_dict(lorentz, model=feynmodel)))
    for particle in model.all_particles:
        feynmodel.add_particle(
            Particle(**ufo_object_to_dict(particle, model=feynmodel))
        )

    for vertex in model.all_vertices:
        feynmodel.add_vertex(Vertex(**ufo_object_to_dict(vertex, model=feynmodel)))
    return feynmodel


# Load a UFO model and convert it to a FeynModel object
def load_ufo_model(model_path, model_name="imported_ufo_model", model_class=FeynModel):
    """Load a UFO model and convert it to a FeynModel object"""
    model = import_ufo_model(model_path, model_name)
    return ufo_to_feynmodel(model, model_class=model_class)
