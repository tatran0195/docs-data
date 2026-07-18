import JPT
from macro_defs import *
from macroTypes import *


def Nastran(
    strPath,
    iImportType=1,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
    bReadLoadAndConstraint=False,
    bReadConnection=False,
    bReadNX=False,
):
    dFaceAngle = JPT.ConvertFromMacroUnit(
        dFaceAngle, JPT.UnitType.Unit_Angle, "deg")
    dEdgeAngle = JPT.ConvertFromMacroUnit(
        dEdgeAngle, JPT.UnitType.Unit_Angle, "deg")
    bReadLoadAndConstraint_b = 1 if bReadLoadAndConstraint else 0
    bReadConnection_b = 1 if bReadConnection else 0
    bReadNX_b = 1 if bReadNX else 0
    strCmd = "CmdImportTSVBdfPost({0}, {1}, {2}, {3}, {4}, {5}, {6})".format(
        '"' + strPath + '"',
        iImportType,
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
        bReadLoadAndConstraint_b,
        bReadConnection_b,
        bReadNX_b,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def Abaqus(
    strPath,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
    iImportType=1,
):
    dFaceAngle = JPT.ConvertFromMacroUnit(
        dFaceAngle, JPT.UnitType.Unit_Angle, "deg")
    dEdgeAngle = JPT.ConvertFromMacroUnit(
        dEdgeAngle, JPT.UnitType.Unit_Angle, "deg")
    strCmd = "ImportInpToPost({0}, {1}, {2}, {3})".format(
        '"' + strPath + '"',
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
        iImportType,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def ADVC(
    strPath,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
):
    dFaceAngle = JPT.ConvertFromMacroUnit(
        dFaceAngle, JPT.UnitType.Unit_Angle, "deg")
    dEdgeAngle = JPT.ConvertFromMacroUnit(
        dEdgeAngle, JPT.UnitType.Unit_Angle, "deg")
    strCmd = "ImportAdxToPost({0}, {1}, {2})".format(
        '"' + strPath + '"',
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def MappedMeshFile(
    strPath,
    iImportType=1,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
):
    dFaceAngle = JPT.ConvertFromMacroUnit(
        dFaceAngle, JPT.UnitType.Unit_Angle, "deg")
    dEdgeAngle = JPT.ConvertFromMacroUnit(
        dEdgeAngle, JPT.UnitType.Unit_Angle, "deg")
    strCmd = "ImportMappedMeshFileDat({0}, {1}, {2}, {3})".format(
        '"' + strPath + '"',
        iImportType,
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
    )
    return getBoolValueFromString(JPT.Exec(strCmd))
