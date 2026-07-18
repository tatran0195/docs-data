import JPT
from macro_defs import *
from macroTypes import *


def Nastran(
    strPath="",
    strlPaths=[],
    iImportType=1,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
    bReadLoadAndConstraint=False,
    bReadConnection=False,
    bCreateResultsAtMidNode=False,
    bIsVibro=False,
    strPathSelectResultFile="",
):
    strPathStr = ""
    if strPath and not strlPaths:
        strPathStr = '"' + strPath + '"'
    elif not strPath and strlPaths:
        strPathStr = "[" + \
            ", ".join('"' + tok + '"' for tok in strlPaths) + "]"

    strCmd = "ImportNastran({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})".format(
        strPathStr,
        iImportType,
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
        1 if bReadLoadAndConstraint else 0,
        1 if bReadConnection else 0,
        1 if bCreateResultsAtMidNode else 0,
        1 if bIsVibro else 0,
        '"' + strPathSelectResultFile + '"',
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def Abaqus(
    strPath,
    iVersion,
    iImportType=1,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
    strSelectResultFilePath="",
):
    strCmd = "ImportAbaqus({0}, {1}, {2}, {3}, {4}, {5})".format(
        '"' + strPath + '"',
        iImportType,
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
        iVersion,
        strSelectResultFilePath
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def ADVC(
    strPath,
    iImportType=1,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
    bADVCProcessNameRule=False,
    bDisplayNAResult=False,
    strSelectResultFilePath="",
):
    strCmd = "ImportADVC({0}, {1}, {2}, {3}, {4}, {5}, {6})".format(
        '"' + strPath + '"',
        iImportType,
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
        1 if bADVCProcessNameRule else 0,
        1 if bDisplayNAResult else 0,
        strSelectResultFilePath
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def Universal(
    strPath,
    iImportType=1,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
):
    strCmd = "ImportUniversal({0}, {1}, {2}, {3})".format(
        '"' + strPath + '"',
        iImportType,
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def Ansys(
    strPath,
    iImportType=1,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
):
    strCmd = "ImportAnsysResult({0}, {1}, {2}, {3})".format(
        '"' + strPath + '"',
        iImportType,
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def OptishapeTS(
    strlPaths,
    iImportType=1,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
):
    strCmd = "ImportOptishapeTS({0}, {1}, {2}, {3})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        iImportType,
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def FrontISTR(
    strPath,
    iImportType=1,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
):
    strCmd = "ImportFrontISTR({0}, {1}, {2}, {3})".format(
        '"' + strPath + '"',
        iImportType,
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def Marc(
    strPath,
    iImportType=1,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
):
    strCmd = "ImportMarc({0}, {1}, {2}, {3})".format(
        '"' + strPath + '"',
        iImportType,
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def STDFile(
    strPath,
    iImportType=1,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
):
    strCmd = "ImportSTDFile({0}, {1}, {2}, {3})".format(
        '"' + strPath + '"',
        iImportType,
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def MuxWeld(
    strPath,
    iImportType=1,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
):
    strCmd = "ImportMuxWeld({0}, {1}, {2}, {3})".format(
        '"' + strPath + '"',
        iImportType,
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def LSDyna(
    strPath,
    iImportType=1,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
):
    strCmd = "ImportLSDyna({0}, {1}, {2}, {3})".format(
        '"' + strPath + '"',
        iImportType,
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def Permas(
    strPath,
    iImportType=1,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
):
    strCmd = "ImportPermas({0}, {1}, {2}, {3})".format(
        '"' + strPath + '"',
        iImportType,
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def SunShineUStar(
    strPath,
    iImportType=1,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
    bReadLoadAndConstraint=False,
    bReadConnection=False,
    bCreateResultsAtMidNode=False,
):
    strCmd = "ImportSunShineUStar({0}, {1}, {2}, {3}, {4}, {5}, {6})".format(
        '"' + strPath + '"',
        iImportType,
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
        1 if bReadLoadAndConstraint else 0,
        1 if bReadConnection else 0,
        1 if bCreateResultsAtMidNode else 0,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def Radioss(
    strlPaths,
    iImportType=1,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
    bReadLoadAndConstraint=False,
    bReadConnection=False,
    bCreateResultsAtMidNode=False,
):
    strCmd = "ImportRadioss({0}, {1}, {2}, {3}, {4}, {5}, {6})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        iImportType,
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
        1 if bReadLoadAndConstraint else 0,
        1 if bReadConnection else 0,
        1 if bCreateResultsAtMidNode else 0,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def WAON(
    strPath,
    strFPMFilePath,
    strResultFolderPath,
    iImportType=1,
    dFaceAngle=60.0,
    dEdgeAngle=60.0,
    bReadLoadAndConstraint=False,
    bReadConnection=False,
    bCreateResultsAtMidNode=False,
):
    strCmd = "CmdImportTSVWAONPost({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})".format(
        '"' + strPath + '"',
        '"' + strFPMFilePath + '"',
        '"' + strResultFolderPath + '"',
        iImportType,
        round(convertAngleFromDegToRad(dFaceAngle), 2),
        round(convertAngleFromDegToRad(dEdgeAngle), 2),
        1 if bReadLoadAndConstraint else 0,
        1 if bReadConnection else 0,
        1 if bCreateResultsAtMidNode else 0,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))
