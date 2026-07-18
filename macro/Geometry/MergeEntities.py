import JPT
from macro_defs import *
from macroTypes import *


def Faces(crlFaces, bMergeEdge=True, bRemoveNonBoundEdge=True, bHighSpeedProcessing=False):
    bMergeEdge_b = 1 if bMergeEdge else 0
    RemoveNonBoundEdge_b = 1 if bRemoveNonBoundEdge else 0
    bHighSpeedProcessing_b = 1 if bHighSpeedProcessing else 0
    strCmd = 'MergeFace_MergeEntities({0}, {1}, {2}, {3})'.format(
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        bMergeEdge_b,
        RemoveNonBoundEdge_b,
        bHighSpeedProcessing_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))


def TinyFacesMerge(strMethod="AUTO", crlTargets=[], dMinFaceWidth=0.0, dMaxFaceWidth=0.001, dFaceAngle=30, bReferLocalSetting=False, bCreateRefPart=False, crlRefPart=[], crlRefEdge=[]):
    bReferLocalSetting_b = 1 if bReferLocalSetting else 0
    bCreateRefPart_b = 1 if bCreateRefPart else 0
    strCmd = 'GeometryMergeEntitiesTinyFacesMerge_K({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})'.format(
        '"' + strMethod + '"',
        str(crlTargets) if crlTargets != [None] else '[0:0]',
        dMinFaceWidth,
        dMaxFaceWidth,
        dFaceAngle,
        bReferLocalSetting_b,
        bCreateRefPart_b,
        str(crlRefPart) if crlRefPart != [None] else '[0:0]',
        str(crlRefEdge) if crlRefEdge != [None] else '[0:0]')
    return getBoolValueFromString(JPT.Exec(strCmd))


def CBarParts(crlCBarPart=[]):
    strCmd = 'MergeCBarPart({0})'.format(
        str(crlCBarPart) if crlCBarPart != [None] else '[0:0]')
    return JPT.Exec(strCmd)


def Edges(crlEdges=[], bHighSpeedProcessing=False):
    bHighSpeedProcessing_b = 1 if bHighSpeedProcessing else 0
    strCmd = 'MergeEdge({0}, {1})'.format(
        str(crlEdges) if crlEdges != [None] else '[0:0]',
        bHighSpeedProcessing_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))


def Parts(crlParts, dMergeTolerance=1e-5, bRemoveSharedFace=True, bMergeReferences=False):
    dMergeTolerance = JPT.ConvertFromMacroUnit(
        dMergeTolerance, JPT.UnitType.Unit_Length, "mm")
    bRemoveSharedFace_b = 1 if bRemoveSharedFace else 0
    bMergeReferences_b = 1 if bMergeReferences else 0
    strCmd = 'MergePart({0}, {1}, {2}, {3})'.format(
        dMergeTolerance,
        bRemoveSharedFace_b,        
        str(crlParts) if crlParts != [None] else '[0:0]',
        bMergeReferences_b,)
    return getCursorValueByStr(JPT.Exec(strCmd))


def PartFaces(crlParts=[], crlFaces=[], bAngle=True, dTolAngle=20, bWidth=True, dTolWidth=0.2):
    bAngle_b = 1 if bAngle else 0
    bWidth_b = 1 if bWidth else 0
    dTolWidth = JPT.ConvertFromMacroUnit(
        dTolWidth, JPT.UnitType.Unit_Length, "mm")
    strCmd = 'MergeBodyFaceCr({0}, {1}, {2}, {3}, {4}, {5})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        bAngle_b,
        dTolAngle,
        bWidth_b,
        dTolWidth)
    return JPT.Exec(strCmd)


def MergeTinyFaces(crlTargets, strMode="SearchMode", dMinLength=0, dMaxLength=0, dLimitAngle=0, dMergeFaceAngle=60, bTinyFace=False, bLargeAngleFace=False):
    strCmd = 'NewTinyFacesMerge({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})'.format(
        '"' + strMode + '"',
        str(crlTargets) if crlTargets != [None] else '[0:0]',
        dMinLength,
        dMaxLength,
        dLimitAngle,
        dMergeFaceAngle,
        1 if bTinyFace else 0,
        1 if bLargeAngleFace else 0)
    return JPT.Exec(strCmd)
