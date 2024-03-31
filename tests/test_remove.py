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
