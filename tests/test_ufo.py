import pathlib

from feynmodel.interface.ufo import load_ufo_model


def test_load_ufo():
    """Test loading a UFO model"""
    dir = pathlib.Path(__file__).parent.resolve()
    fm = load_ufo_model(dir / ".." / "models" / "ufo" / "sm")
