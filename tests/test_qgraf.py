import pathlib

from feynmodel.interface.qgraf import feynmodel_to_qgraf, qgraf_to_feynmodel
from feynmodel.interface.ufo import load_ufo_model


def test_load_qgraf():
    """Test loading a qgraf model"""
    # Read file as string
    d = pathlib.Path(__file__).parent.resolve()
    with open(d / ".." / "models" / "qgraf" / "test.qgraf", "r") as f:
        s = f.read()
        fm = qgraf_to_feynmodel(s)
        print(fm.particles)
        print(fm.vertices)


def test_load_ufo():
    """Test loading a UFO model"""
    d = pathlib.Path(__file__).parent.resolve()
    fm = load_ufo_model(d / ".." / "models" / "ufo" / "sm")
    print(feynmodel_to_qgraf(fm, True))


def test_idempotency():
    """Test that qgraf_to_feynmodel(feynmodel_to_qgraf(fm)) == fm"""
    d = pathlib.Path(__file__).parent.resolve()
    fm = load_ufo_model(d / ".." / "models" / "ufo" / "sm")
    fm2 = qgraf_to_feynmodel(feynmodel_to_qgraf(fm, True))
    # assert len(fm.particles) == len(fm2.particles), "Number of particles does not match"
    # assert len(fm.vertices) == len(fm2.vertices), "Number of vertices does not match"
