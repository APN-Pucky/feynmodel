from feynmodel.feyn_model import FeynModel
from feynmodel.interface.ufo import ufo_to_feynmodel
import ufo_mssm


class SM(FeynModel):
    def __init__(self):
        FeynModel.__init__(self, "Minimal Supersymmetric Standard Model")
        ufo_to_feynmodel(ufo_mssm, self)
