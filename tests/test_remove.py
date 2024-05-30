import pathlib

from feynmodel.interface.ufo import load_ufo_model


def test_remove_particle():
    """Test removing of a particle"""
    d = pathlib.Path(__file__).parent.resolve()
    fm = load_ufo_model(d / ".." / "models" / "ufo" / "sm")

    before_particles = len(fm.particles)
    before_vertices = len(fm.vertices)
    fm.remove_object(fm.get_particle(name="G0"))
    assert len(fm.particles) == before_particles - 1
    assert len(fm.vertices) < before_vertices

    assert fm.get_particle(name="G0") is None

    assert "G0" not in str([str(v.particles) for v in fm.vertices])
    assert "G0" not in str([str(v.particle) for v in fm.decays])


def test_remove_G__plus__():
    """Test removing of a particle"""
    d = pathlib.Path(__file__).parent.resolve()
    fm = load_ufo_model(d / ".." / "models" / "ufo" / "sm")

    before_particles = len(fm.particles)
    before_vertices = len(fm.vertices)
    fm.remove_object(fm.get_particle(name="G+"))
    # we also remove G__minus__ here, so we expect 2 particles to be removed
    assert len(fm.particles) == before_particles - 2
    assert len(fm.vertices) < before_vertices

    assert fm.get_particle(name="G+") is None

    assert "G+" not in str([str(v.particles) for v in fm.vertices])
    assert "G__plus__" not in str([str(v.particles) for v in fm.vertices])
    assert "G+" not in str([str(v.particle) for v in fm.decays])
    assert "G__plus__" not in str([str(v.particle) for v in fm.decays])