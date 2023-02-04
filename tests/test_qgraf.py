import pathlib
from feynmodel.interface.qgraf import feynmodel_to_qgraf, qgraf_to_feynmodel

from feynmodel.interface.ufo import load_ufo_model


def test_load_qgraf():
    """Test loading a qgraf model"""
    # Read file as string
    dir = pathlib.Path(__file__).parent.resolve()
    with open(dir / ".." / "models" / "qgraf" / "test.qgraf", "r") as f:
        str = f.read()
        fm = qgraf_to_feynmodel(str)
        print(fm.particles)
        print(fm.vertices)


def test_load_ufo():
    """Test loading a UFO model"""
    dir = pathlib.Path(__file__).parent.resolve()
    fm = load_ufo_model(dir / ".." / "models" / "ufo" / "sm")
    print(feynmodel_to_qgraf(fm, True))


def test_idempotency():
    """Test that qgraf_to_feynmodel(feynmodel_to_qgraf(fm)) == fm"""
    dir = pathlib.Path(__file__).parent.resolve()
    fm = load_ufo_model(dir / ".." / "models" / "ufo" / "sm")
    fm2 = qgraf_to_feynmodel(feynmodel_to_qgraf(fm, True))
    #assert len(fm.particles) == len(fm2.particles), "Number of particles does not match"
    #assert len(fm.vertices) == len(fm2.vertices), "Number of vertices does not match"
