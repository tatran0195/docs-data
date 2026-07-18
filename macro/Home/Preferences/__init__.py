import JPT
from macro_defs import *
from macroTypes import *


def Export(strPath):
    strCmd = 'ExportPreferenceSettings({0})'.format(strPath)
    return getBoolValueFromString(JPT.Exec(strCmd))


def Import(strPath):
    strCmd = 'ImportPreferenceSettings({0})'.format(strPath)
    return getBoolValueFromString(JPT.Exec(strCmd))
