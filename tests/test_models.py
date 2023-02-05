def test_sm():
    """Test loading the Standard Model"""
    from feynmodel.model import sm

    assert sm is not None

    sm.SM()


def test_mssm():
    """Test loading the MSSM"""
    from feynmodel.model import mssm

    assert mssm is not None

    mssm.MSSM()
