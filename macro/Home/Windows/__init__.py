import JPT
from macro_defs import *
from macroTypes import *


def TileBox(iMode):
    strCmd = ''
    if iMode == 1:
        strCmd = 'FrameLessBoxMode1()'
    elif iMode == 2:
        strCmd = 'FrameLessBoxMode2()'
    else:
        return False
    return getBoolValueFromString(JPT.Exec(strCmd))


def TileVertical(iMode):
    strCmd = ''
    if iMode == 0:
        strCmd = 'TileVertical()'
    elif iMode == 1:
        strCmd = 'FrameLessVerticalMode1()'
    elif iMode == 2:
        strCmd = 'FrameLessVerticalMode2()'
    elif iMode == 3:
        strCmd = 'FrameLessVerticalMode3()'
    elif iMode == 4:
        strCmd = 'FrameLessVerticalMode4()'
    elif iMode == 5:
        strCmd = 'FrameLessVerticalMode5()'
    elif iMode == 6:
        strCmd = 'FrameLessVerticalMode6()'
    elif iMode == 7:
        strCmd = 'FrameLessVerticalMode7()'
    else:
        return False
    return getBoolValueFromString(JPT.Exec(strCmd))


def TileHorizontal(iMode):
    strCmd = ''
    if iMode == 0:
        strCmd = 'TileHorizontal()'
    elif iMode == 1:
        strCmd = 'FrameLessHorizontalMode1()'
    elif iMode == 2:
        strCmd = 'FrameLessHorizontalMode2()'
    elif iMode == 3:
        strCmd = 'FrameLessHorizontalMode3()'
    elif iMode == 4:
        strCmd = 'FrameLessHorizontalMode4()'
    elif iMode == 5:
        strCmd = 'FrameLessHorizontalMode5()'
    elif iMode == 6:
        strCmd = 'FrameLessHorizontalMode6()'
    elif iMode == 7:
        strCmd = 'FrameLessHorizontalMode7()'
    else:
        return False
    return getBoolValueFromString(JPT.Exec(strCmd))


def FrameCancel():
    strCmd = 'FrameLessCancel()'
    return getBoolValueFromString(JPT.Exec(strCmd))
