# Convert a feynmodel to a qgraf model
# return the qgraf model as string

from feynmodel.feyn_model import FeynModel
from feynmodel.particle import Particle
from feynmodel.util import get_name
from feynmodel.vertex import Vertex


def get_particle_name(particle, use_pdg_names=False, anti=False):
    # neutral particles have the same name as their antiparticles
    # and PDG won't give us the negative pdgid
    if particle.name == particle.antiname:
        anti = False
    if use_pdg_names:
        if anti:
            return get_name(-particle.pdg_code, particle.antiname)
        else:
            return get_name(particle.pdg_code, particle.name)
    else:
        if anti:
            return particle.antiname
        else:
            return particle.name


def feynmodel_to_qgraf(
    feynmodel: FeynModel, use_pdg_names=False, include_antiparticles=False
):
    return_string = ""
    return_string + "* Particles\n"
    for p in feynmodel.particles:
        if include_antiparticles or p.pdg_code > 0:
            stat = ["-", "+", "+", "-", "+"][p.spin + 1]
            name = get_particle_name(p, use_pdg_names)
            antiname = get_particle_name(p, use_pdg_names, anti=True)
            return_string += f"[{name},{antiname},{stat}]\n"
    return_string + "* Vertices\n"
    for v in feynmodel.vertices:
        return_string += "["
        for p in v.particles:
            return_string += get_particle_name(p, use_pdg_names) + ","
        return_string = return_string[:-1] + "]\n"
    return return_string


def qgraf_to_feynmodel(qgraf_model: str):
    fm = FeynModel()
    for line in qgraf_model.splitlines():
        if line.startswith("*"):
            continue
        if "[" in line and "]" in line:
            content = line[line.index("[") + 1 : line.index("]")]
            contents = content.split(",")
            for i, _ in enumerate(contents):
                contents[i] = contents[i].strip()
            if contents[2] == "+" or contents[2] == "-":
                # particle
                fm.add_particle(
                    Particle(
                        name=contents[0], antiname=contents[1], statistics=contents[2]
                    )
                )
            else:
                # vertex
                fm.add_vertex(
                    Vertex(
                        name="_".join(contents),
                        particles=[
                            fm.get_particle(name=contents[i])
                            for i in range(0, len(contents))
                        ],
                    )
                )
    return fm
