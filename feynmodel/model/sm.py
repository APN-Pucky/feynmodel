from feynmodel.feyn_model import FeynModel
from feynmodel.interface.ufo import ufo_to_feynmodel
import ufo_sm


class SM(FeynModel):
    def __init__(self):
        FeynModel.__init__(self, "Standard Model")
        ufo_to_feynmodel(ufo_sm, self)
