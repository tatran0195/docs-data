import JPT
from macro_defs import *
from macroTypes import *


def PropertyGroup():
    strCmd = 'CreatePropertyGroup(" ")'
    return getListCursorValueByStr(JPT.Exec(strCmd))


def Rename(strNewName, crItem):
    strCmd = 'RenameItem({0}, {1})'.format(
        '"' + strNewName + '"',
        str(crItem) if crItem is not None else '0:0')
    return getBoolValue(JPT.Exec(strCmd))


def DeleteGroup(crlGroups, bRemoveAll=False):
    bRemoveAll_b = 1 if bRemoveAll else 0
    strCmd = 'DeleteGroup({0}, {1})'.format(
        str(crlGroups) if crlGroups != [None] else '[0:0]',
        bRemoveAll_b)
    return getBoolValue(JPT.Exec(strCmd))


def CopyGroup(crlGroups, strlNames=[], crSubGroup=None, bKeepOriginalGroup=False):
    bKeepOriginalGroup_b = 1 if bKeepOriginalGroup else 0
    strCmd = 'CopyGroup({0}, {1}, {2}, {3})'.format(
        str(crlGroups) if crlGroups != [None] else '[0:0]',
        '[' + ', '.join('"' + tok + '"' for tok in strlNames) + ']',
        str(crSubGroup) if crSubGroup is not None else '0:0',
        bKeepOriginalGroup_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))


def AddSubGroup(crSubGroupSelected=None):
    strCmd = ''
    if JPT.CheckLicense("JPT_BASE") or JPT.CheckLicense("JPT_POST") or JPT.CheckLicense("JPT_DESIGNER"):
        strCmd = 'AddSupGroupEx({0})'.format(
            str(crSubGroupSelected) if crSubGroupSelected is not None else '0:0')
    else:
        strCmd = 'AddSupGroup({0})'.format(
            str(crSubGroupSelected) if crSubGroupSelected is not None else '0:0')
    return getCursorValueByStr(JPT.Exec(strCmd))


def CreateMatGroup():
    strCmd = 'CreateMaterialGroup(" ")'
    return getListCursorValueByStr(JPT.Exec(strCmd))


def ImportGroup(
        strlPaths,
        crParentGroup=None,
):
    strCmd = 'ImportGroup({0}, {1})'.format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        str(crParentGroup) if crParentGroup is not None else '0:0',
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def ExportGroup(
        crlTargets,
        strlPaths,
        iEncode=-1,
        bWithBOM=False
):
    bWithBOM_b = 1 if bWithBOM else 0
    strCmd = 'ExportGroup({0}, {1}, {2}, {3})'.format(
        str(crlTargets) if crlTargets != [None] else '[0:0]',
        '[' + ', '.join('"' + tok + '"' for tok in strlPaths) + ']',
        iEncode,
        bWithBOM_b,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def ExportSubGroup(
        strFolderPath="",
        crlSubGroups=[],
        crlGroups=[],
        iEncode=-1,
        bWithBOM=False
):
    bWithBOM_b = 1 if bWithBOM else 0
    strCmd = 'ExportSubGroup({0}, {1}, {2}, {3}, {4})'.format(
        '"' + strFolderPath + '"',
        str(crlSubGroups) if crlSubGroups != [None] else '[0:0]',
        str(crlGroups) if crlGroups != [None] else '[0:0]',
        iEncode,
        bWithBOM_b,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def ChangeMarkerColor(
        listGroupColors
):
    strData = ''
    for item in listGroupColors:
        strData += f'[{str(item[0])}, {item[1]}]'
        if item != listGroupColors[-1]:
            strData += ', '
    strData = '[' + strData + ']'
    strCmd = 'ChangeMarkerColor({0})'.format(
        strData,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))
