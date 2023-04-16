import pathlib

from feynmodel.interface.ufo import load_ufo_model


def test_load_ufo_by_path():
    """Test loading a UFO model by path"""
    d = pathlib.Path(__file__).parent.resolve()
    fm = load_ufo_model(d / ".." / "models" / "ufo" / "sm")


def test_load_ufo_by_name():
    """Test loading a UFO model by name"""
    fm = load_ufo_model("ufo_sm")
