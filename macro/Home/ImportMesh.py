import JPT
from macro_defs import *
from macroTypes import *


# Old version
def NastranBdf(
    strlPaths,
    iImportType=2,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
    bReadNameComment=False,
    iCreateDup1DElemAnswer=-1,
):
    dFaceAngle = JPT.ConvertFromMacroUnit(dFaceAngle, JPT.UnitType.Unit_Angle, "deg")
    dEdgeAngle = JPT.ConvertFromMacroUnit(dEdgeAngle, JPT.UnitType.Unit_Angle, "deg")
    bReadNameComment_b = 1 if bReadNameComment else 0
    strCmd = "ImportBdf({0}, {1}, {2}, {3}, {4}, {5})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        iImportType,
        dFaceAngle,
        dEdgeAngle,
        bReadNameComment_b,
        iCreateDup1DElemAnswer,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def Nastran(
    strlPaths,
    iImportType=2,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
    bReadJPTComment=False,
    iCreateDup1DElemAnswer=-1,
    bReadHMComment=False,
):
    dFaceAngle = JPT.ConvertFromMacroUnit(dFaceAngle, JPT.UnitType.Unit_Angle, "deg")
    dEdgeAngle = JPT.ConvertFromMacroUnit(dEdgeAngle, JPT.UnitType.Unit_Angle, "deg")
    bReadJPTComment_b = 1 if bReadJPTComment else 0
    bReadHMComment_b = 1 if bReadHMComment else 0
    strCmd = "ImportBdf({0}, {1}, {2}, {3}, {4}, {5}, {6})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        iImportType,
        dFaceAngle,
        dEdgeAngle,
        bReadJPTComment_b,
        iCreateDup1DElemAnswer,
        bReadHMComment_b,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))

def FrontISTR(
    strlPaths,
    dFaceAngle=60.0,
    dEdgeAngle=60.0
):
    dFaceAngle = JPT.ConvertFromMacroUnit(dFaceAngle, JPT.UnitType.Unit_Angle, "deg")
    dEdgeAngle = JPT.ConvertFromMacroUnit(dEdgeAngle, JPT.UnitType.Unit_Angle, "deg")
    strCmd = "ImportPreFrontISTR({0}, {1}, {2})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        dFaceAngle,
        dEdgeAngle
    )
    return getBoolValueFromString(JPT.Exec(strCmd))

# Old version
def AnsysDat(strlPaths, dFaceAngle=60.0, dEdgeAngle=60.0):
    return Ansys(strlPaths, dFaceAngle=dFaceAngle, dEdgeAngle=dEdgeAngle)


def Ansys(strlPaths, dFaceAngle=60.0, dEdgeAngle=60.0):
    dFaceAngle = JPT.ConvertFromMacroUnit(dFaceAngle, JPT.UnitType.Unit_Angle, "deg")
    dEdgeAngle = JPT.ConvertFromMacroUnit(dEdgeAngle, JPT.UnitType.Unit_Angle, "deg")
    strCmd = "ImportAnsys({0}, {1}, {2})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        dFaceAngle,
        dEdgeAngle,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


# Old version
def ADVCADX(strlPaths, dFaceAngle=60.0, dEdgeAngle=60.0):
    return ADVC(strlPaths, dFaceAngle=dFaceAngle, dEdgeAngle=dEdgeAngle)


def ADVC(
        strlPaths, 
        dFaceAngle=60.0, 
        dEdgeAngle=60.0,
        iImportType=0,
        bReadCommentsForJupiter=False):
    dFaceAngle = JPT.ConvertFromMacroUnit(dFaceAngle, JPT.UnitType.Unit_Angle, "deg")
    dEdgeAngle = JPT.ConvertFromMacroUnit(dEdgeAngle, JPT.UnitType.Unit_Angle, "deg")
    bReadCommentsForJupiter_b = 1 if bReadCommentsForJupiter else 0
    strCmd = 'ImportAdxList({0}, {1}, {2}, {3}, {4})'.format(
        '[' + ', '.join('"' + tok + '"' for tok in strlPaths) + ']',
        dFaceAngle,
        dEdgeAngle,
        iImportType,
        bReadCommentsForJupiter_b
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


# Old version
def AbaqusINP(strlPaths, dFaceAngle=60.0, dEdgeAngle=60.0, iImportType=1):
    return Abaqus(
        strlPaths, dFaceAngle=dFaceAngle, dEdgeAngle=dEdgeAngle, iImportType=iImportType
    )


def Abaqus(strlPaths, dFaceAngle=60.0, dEdgeAngle=60.0, iImportType=1):
    dFaceAngle = JPT.ConvertFromMacroUnit(dFaceAngle, JPT.UnitType.Unit_Angle, "deg")
    dEdgeAngle = JPT.ConvertFromMacroUnit(dEdgeAngle, JPT.UnitType.Unit_Angle, "deg")
    strCmd = "ImportInp({0}, {1}, {2}, {3})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        dFaceAngle,
        dEdgeAngle,
        iImportType,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


# Old version
def LSDYNA(strlPaths, dFaceAngle=60.0, dEdgeAngle=60.0):
    return LsDyna(strlPaths, dFaceAngle=dFaceAngle, dEdgeAngle=dEdgeAngle)


def LsDyna(strlPaths, dFaceAngle=60.0, dEdgeAngle=60.0):
    dFaceAngle = JPT.ConvertFromMacroUnit(dFaceAngle, JPT.UnitType.Unit_Angle, "deg")
    dEdgeAngle = JPT.ConvertFromMacroUnit(dEdgeAngle, JPT.UnitType.Unit_Angle, "deg")
    strCmd = "ImportLsDyna({0}, {1}, {2})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        dFaceAngle,
        dEdgeAngle,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def Universal(strlPaths, dFaceAngle=60.0, dEdgeAngle=60.0):
    dFaceAngle = JPT.ConvertFromMacroUnit(dFaceAngle, JPT.UnitType.Unit_Angle, "deg")
    dEdgeAngle = JPT.ConvertFromMacroUnit(dEdgeAngle, JPT.UnitType.Unit_Angle, "deg")
    strCmd = "ImportUniversalMesh({0}, {1}, {2})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        dFaceAngle,
        dEdgeAngle,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def TSVPre(strImportPath="", strExportPath="", ilModelIndex=None, iMerge=None):
    if ilModelIndex is not None and iMerge is not None:
        Merge_b = 1 if iMerge else 0
        strCmd = "ImportVDB({0}, {1}, {2}, {3})".format(
            '"' + strImportPath + '"', '"' + strExportPath + '"', ilModelIndex, Merge_b
        )
    elif ilModelIndex is not None:
        strCmd = "ImportVDB({0}, {1}, {2})".format(
            '"' + strImportPath + '"', '"' + strExportPath + '"', ilModelIndex
        )
    else:
        strCmd = "ImportVDB({0}, {1})".format(
            '"' + strImportPath + '"', '"' + strExportPath + '"'
        )
    return getBoolValueFromString(JPT.Exec(strCmd))


def Marc(strPath, dFaceAngle=60.0, dEdgeAngle=60.0):
    dFaceAngle = JPT.ConvertFromMacroUnit(dFaceAngle, JPT.UnitType.Unit_Angle, "deg")
    dEdgeAngle = JPT.ConvertFromMacroUnit(dEdgeAngle, JPT.UnitType.Unit_Angle, "deg")
    strCmd = "ImportMarcMesh({0}, {1}, {2})".format(
        '"' + strPath + '"',
        dFaceAngle,
        dEdgeAngle,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))
