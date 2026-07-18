import JPT
from macro_defs import *
from macroTypes import *


def Clipboard(iLeft=0, iTop=0, iRight=0, iBottom=0):
    strCmd = "Capture_Rectangular({0}, {1}, {2}, {3})".format(
        iLeft, iTop, iRight, iBottom
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def Single(strFrameName, iStartPointX, iStartPointY, iWidth, iHeight):
    args = [
        '"'+strFrameName+'"',
        str(iStartPointX),
        str(iStartPointY),
        str(iWidth+iStartPointX),
        str(iHeight+iStartPointY),
        "0",
    ]
    strCmd = "ViewMakeUserFrame({0})".format(
        ', '.join(arg for arg in args if arg))
    return getBoolValueFromString(JPT.Exec(strCmd))


def Multiple(strFrameName, iStartPointX, iStartPointY, iWidth, iHeight):
    args = [
        '"'+strFrameName+'"',
        str(iStartPointX),
        str(iStartPointY),
        str(iWidth+iStartPointX),
        str(iHeight+iStartPointY),
        "1",
    ]
    strCmd = "ViewMakeUserFrame({0})".format(
        ', '.join(arg for arg in args if arg))
    return getBoolValueFromString(JPT.Exec(strCmd))
