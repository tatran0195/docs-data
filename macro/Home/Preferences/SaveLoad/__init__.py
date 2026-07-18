import JPT
from macro_defs import *


def CalculateTrescaStress(bUseTrescaStress=False):
    bFlag_b = 1 if bUseTrescaStress else 0
    strCmd = "SetCalculateTrescaStress({0})".format(bFlag_b)
    return getBoolValueFromString(JPT.Exec(strCmd))
