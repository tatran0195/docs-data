import JPT
from macro_defs import *
from macroTypes import *


def Nastran(
    strlPaths,
    bMergeTree=True,
    bCreateResultAtMidNode=True,
):
    bMergeTree_b = 1 if bMergeTree else 0
    bCreateResultAtMidNode_b = 1 if bCreateResultAtMidNode else 0
    strCmd = "AddResultsNastran({0}, {1}, {2})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        bMergeTree_b,
        bCreateResultAtMidNode_b,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def Actran(
    strlPaths,
    bMergeTree=True,
):
    bMergeTree_b = 1 if bMergeTree else 0
    strCmd = "AddResultsActran({0}, {1})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        bMergeTree_b,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def Abaqus(
    strlPaths,
    bMergeTree=True,
    iVersion=2019,
    strPathSelectResultFile="",
):
    bMergeTree_b = 1 if bMergeTree else 0
    strCmd = "AddResultsAbaqus({0}, {1}, {2}, {3})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        bMergeTree_b,
        iVersion,
        '"' + strPathSelectResultFile + '"',
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def ADVC(
    strlPaths,
    bMergeTree=True,
    bADVCProcessNameRule=False,
    bDisplayNAResult=False,
    strPathSelectResultFile="",
):
    bMergeTree_b = 1 if bMergeTree else 0
    bADVCProcessNameRule_b = 1 if bADVCProcessNameRule else 0
    bDisplayNAResult_b = 1 if bDisplayNAResult else 0
    strCmd = "AddResultsADVC({0}, {1}, {2}, {3}, {4})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        bMergeTree_b,
        bADVCProcessNameRule_b,
        bDisplayNAResult_b,
        '"' + strPathSelectResultFile + '"',
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def Universal(
    strlPaths,
    bMergeTree=True,
):
    bMergeTree_b = 1 if bMergeTree else 0
    strCmd = "AddResultsUniversal({0}, {1})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        bMergeTree_b,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def MappedMeshResult(
    strlPaths,
    bMergeTree=True,
):
    bMergeTree_b = 1 if bMergeTree else 0
    strCmd = "AddResultsMappedMeshFile({0}, {1})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        bMergeTree_b,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def Sysnoise(
    strlPaths,
    bMergeTree=True,
):
    bMergeTree_b = 1 if bMergeTree else 0
    strCmd = "AddResultsSysnoise({0}, {1})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        bMergeTree_b,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def LSDyna(
    strlPaths,
    bMergeTree=True,
):
    bMergeTree_b = 1 if bMergeTree else 0
    strCmd = "AddResultsLSDyna({0}, {1})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        bMergeTree_b,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def Permas(
    strlPaths,
    bMergeTree=True,
):
    bMergeTree_b = 1 if bMergeTree else 0
    strCmd = "AddResultsPermas({0}, {1})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        bMergeTree_b,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def OptishapeTS(
    strlPaths,
    bMergeTree=True,
):
    bMergeTree_b = 1 if bMergeTree else 0
    strCmd = "AddResultsOptishapeTS({0}, {1})".format(
        "[" + ", ".join('"' + tok + '"' for tok in strlPaths) + "]",
        bMergeTree_b,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def UsersResult(
    strlPath,
    bExportLog=False,
):
    bExportLog_b = 1 if bExportLog else 0
    strCmd = "AddUserResultDefine({0}, {1})".format(
        '"' + strlPath + '"',
        bExportLog_b,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))
