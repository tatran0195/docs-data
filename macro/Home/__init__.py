import JPT
from macro_defs import *
from macroTypes import *


def ExportSTL(strFile="", crlParts=[], dScale=1, bBinaryFormat=False):
    bBinaryFormat_b = 1 if bBinaryFormat else 0
    strCmd = "ExportSTL({0}, {1}, {2}, {3})".format(
        '"' + strFile + '"',
        str(crlParts) if crlParts != [None] else "[0:0]",
        dScale,
        bBinaryFormat_b,
    )
    return JPT.Exec(strCmd)


def ExportGeometryBDF(
    strFileName,
    crlParts=[],
    bBigID=False,
    bUseUnit=True,
    bVert=True,
    bEdge=True,
    bFace=True,
    bSolid=True,
):
    bBigID_b = 1 if bBigID else 0
    bUseUnit_b = 1 if bUseUnit else 0
    bVert_b = 1 if bVert else 0
    bEdge_b = 1 if bEdge else 0
    bFace_b = 1 if bFace else 0
    bSolid_b = 1 if bSolid else 0
    strCmd = "ExportGeomBDF({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})".format(
        '"' + strFileName + '"',
        str(crlParts) if crlParts != [None] else "[0:0]",
        bBigID_b,
        bUseUnit_b,
        bVert_b,
        bEdge_b,
        bFace_b,
        bSolid_b,
    )
    return JPT.Exec(strCmd)


def ExportTSG(
    strFileName,
    crlParts=[],
    bBigID=False,
    bUseUnit=True,
    bVert=True,
    bEdge=True,
    bFace=True,
    bSolid=True,
):
    bBigID_b = 1 if bBigID else 0
    bUseUnit_b = 1 if bUseUnit else 0
    bVert_b = 1 if bVert else 0
    bEdge_b = 1 if bEdge else 0
    bFace_b = 1 if bFace else 0
    bSolid_b = 1 if bSolid else 0
    strCmd = "ExportTSG({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})".format(
        '"' + strFileName + '"',
        str(crlParts) if crlParts != [None] else "[0:0]",
        bBigID_b,
        bUseUnit_b,
        bVert_b,
        bEdge_b,
        bFace_b,
        bSolid_b,
    )
    return JPT.Exec(strCmd)


def ExportGeometrySurface(strFolderName, bUseUnit=True):
    if strFolderName == "":
        return False
    bUseUnit_b = 1 if bUseUnit else 0
    strCmd = "PostExportGeom({0}, {1})".format(
        '"' + strFolderName + '"', bUseUnit_b)
    return getBoolValueFromString(JPT.Exec(strCmd))


def ToImage(
    strImgPath,
    bWhiteBG=False,
    bTransparentBG=False,
    bFixedSize=False,
    iExportWidth=1200,
    iExportHeight=900,
    bAutoCapture=False,
    listAdjust=[0, 0, 0, 0],
):
    bWhiteBG_b = 1 if bWhiteBG else 0
    bTransparentBG_b = 1 if bTransparentBG else 0
    bFixedSize_b = 1 if bFixedSize else 0
    strCmd = ""
    if bAutoCapture:
        strCmd = "Capture_ToImageEx({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})".format(
            '"' + strImgPath + '"',
            bWhiteBG_b,
            bTransparentBG_b,
            bFixedSize_b,
            iExportWidth,
            iExportHeight,
            1 if bAutoCapture else 0,
            listAdjust,
        )
    else:
        strCmd = "Capture_ToImageEx({0}, {1}, {2}, {3}, {4}, {5})".format(
            '"' + strImgPath + '"',
            bWhiteBG_b,
            bTransparentBG_b,
            bFixedSize_b,
            iExportWidth,
            iExportHeight,
        )
    return getBoolValueFromString(JPT.Exec(strCmd))


def Find(strSearch="", strSelectedType="Part", bFindMatch=False):
    bFindMatch_b = 1 if bFindMatch else 0
    strCmd = "ViewFindEntities({0}, {1}, {2})".format(
        '"' + strSearch + '"', '"' + strSelectedType + '"', bFindMatch_b
    )
    return getListCursorValueByStr(JPT.Exec(strCmd))


def CopyToClipboard(
    bWhiteBG=False,
    bTransparentBG=False,
    bFixedSize=False,
    iWidth=1200,
    iHeight=900,
    bAutoCapture=False,
    listAdjust=[0, 0, 0, 0],
):
    bWhiteBG_b = 1 if bWhiteBG else 0
    bTransparentBG_b = 1 if bTransparentBG else 0
    bFixedSize_b = 1 if bFixedSize else 0
    strCmd = ""
    if bAutoCapture:
        strCmd = "Capture_CopyToClipboardEx({0}, {1}, {2}, {3}, {4}, {5}, {6})".format(
            bWhiteBG_b,
            bTransparentBG_b,
            bFixedSize_b,
            iWidth,
            iHeight,
            1 if bAutoCapture else 0,
            listAdjust,
        )
    else:
        strCmd = "Capture_CopyToClipboardEx({0}, {1}, {2}, {3}, {4})".format(
            bWhiteBG_b, bTransparentBG_b, bFixedSize_b, iWidth, iHeight
        )
    return getBoolValueFromString(JPT.Exec(strCmd))


def FullScreen():
    strCmd = "ShowFullScreen()"
    return JPT.Exec(strCmd)


def Synchronize():
    strCmd = "SetSynchronize()"
    return getBoolValueFromString(JPT.Exec(strCmd))


def EXPORT_UNIVERSAL(strFileName, crlParts=[], UnitLengthType=0):
    strCmd = "EXPORT_UNIVERSAL({0}, {1}, {2})".format(
        '"' + strFileName + '"',
        str(crlParts) if crlParts != [None] else "[0:0]",
        UnitLengthType,
    )
    return JPT.Exec(strCmd)


def ExportVTFx(
    strPath="",
    iModelType=1,
    bExcludeBarPart=False,
    bSurfaceElementOnly=False,
    iData2D=0,
    lSelectedResults=[],
    lSelectedResultDataOps=[],
    bDisplayPostAddTrescaStress=False,
    iCurUnitLength=0,
    iCurUnitTime=0,
    iCurUnitMass=0,
    iCurUnitForce=0,
    iCurUnitAngle=1,
    iCurUnitTemperature=1,
    iCurUnitPressure=1,
    iCurUnitDisplacement=0,
    bSetDefaultResult=False,
):
    bExcludeBarPart_b = 1 if bExcludeBarPart else 0
    bSurfaceElementOnly_b = 1 if bSurfaceElementOnly else 0
    if isNativeParamList(lSelectedResults, eval("PostResultKey")):
        lSelectedResults = [PostResultKey().fromList(tok)
                            for tok in lSelectedResults]
    lSelectedResults_ = (
        "["
        + ", ".join(
            [
                (
                    "{{{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}}}".format(
                        tok.iAnalysisType,
                        tok.iResultSet,
                        tok.iTimeStep,
                        tok.iResultType,
                        tok.iResultPos,
                        '"' + tok.strResultName + '"',
                        '"' + tok.strResultCompName + '"',
                        lSelectedResultDataOps[i].iResultLocation if i < len(lSelectedResultDataOps) else 0,
                        lSelectedResultDataOps[i].iOptionConversion if i < len(lSelectedResultDataOps) else 0,
                    )
                )
                for i, tok in enumerate(lSelectedResults)
            ]
        )
        + "]"
    )
    bDisplayPostAddTrescaStress_b = 1 if bDisplayPostAddTrescaStress else 0
    bSetDefaultResult_b = 1 if bSetDefaultResult else 0

    strCmd = "ExportVTFxFile({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13})".format(
        '"' + strPath + '"',
        iModelType,
        bExcludeBarPart_b,
        bSurfaceElementOnly_b,
        iData2D,
        lSelectedResults_,
        bDisplayPostAddTrescaStress_b,
        iCurUnitLength,
        iCurUnitTime,
        iCurUnitMass,
        iCurUnitForce,
        iCurUnitAngle,
        iCurUnitTemperature,
        iCurUnitPressure,
        iCurUnitDisplacement,
        bSetDefaultResult_b,
    )
    return getBoolValueFromString(JPT.Exec(strCmd))


def ExportResultToTXT(
    strFileName,
    iSpliterType=0,
    bAppend=False,
    crlJobs=[],
    ilAnalysisTypes=[],
    ilResultSets=[],
    ilTimeSteps=[],
    ilResultTypes=[],
    ilResultPos=[],
    strlResultNames=[],
    strlCompNames=[],
    strlNames=[],
    strlTypes=[],
    crlEdit=[],
):
    if strFileName == "":
        return False
    args = [
        '"' + strFileName + '"',
        str(iSpliterType),
        "1" if bAppend else "0",
        str(crlJobs),
        str(ilAnalysisTypes),
        str(ilResultSets),
        str(ilTimeSteps),
        str(ilResultTypes),
        str(ilResultPos),
        getStringListStr(strlResultNames),
        getStringListStr(strlCompNames),
        getStringListStr(strlNames),
        getStringListStr(strlTypes),
        str(crlEdit) if crlEdit != [None] else "[0:0]",
    ]
    strCmd = "PostExportToTxt({0})".format(
        ", ".join(arg for arg in args if arg))
    return getBoolValue(JPT.Exec(strCmd))


def ToPPTX(bAutoCapture=False, listAdjust=[0, 0, 0, 0]):
    strCmd = ""
    if bAutoCapture:
        strCmd = "Capture_ToPPT({0}, {1})".format(
            1 if bAutoCapture else 0,
            listAdjust,
        )
    else:
        strCmd = "Capture_ToPPT()"
    return JPT.Exec(strCmd)


def ExportPV(iGroupType=0, strFileName=""):
    strCmd = 'Export_Post_Viewer_File({0}, {1})'.format(
        iGroupType,
        '"' + strFileName + '"',
    )
    return getBoolValueFromString(JPT.Exec(strCmd))

def ToPPTX_3DModel():
    strCmd = "Capture_3DModel_ToPPT()"
    return JPT.Exec(strCmd)

def ExportGLB(strFileName=""):
    strCmd = 'ExportGLB_Direct({0})'.format(
        '"' + strFileName + '"',
    )
    return getBoolValueFromString(JPT.Exec(strCmd))
