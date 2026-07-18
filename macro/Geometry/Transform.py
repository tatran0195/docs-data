import JPT
from macro_defs import *
from macroTypes import *


def Rotation(crlParts, posCenter=[0, 0, 0], vecAxis=[1, 0, 0], dAngle=0, bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, iCopyCount=1, bMergeNode=False, dTol=1.0e-5, bCopyReference=True):
    CreateNewBody_b = 1 if bCreateNewPart else 0
    CopyLBC_b = 1 if bCopyLBC else 0
    CopyProperty_b = 1 if bCopyProperty else 0
    MergeNode_b = 1 if bMergeNode else 0
    dTol = JPT.ConvertFromMacroUnit(dTol, JPT.UnitType.Unit_Length, "mm")
    bCopyReference_b = 1 if bCopyReference else 0
    strCmd = 'RotateBody({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        posCenter,
        vecAxis,
        dAngle,
        CreateNewBody_b,
        CopyLBC_b,
        CopyProperty_b,
        iCopyCount,
        MergeNode_b,
        dTol,
        bCopyReference_b)
    return getBoolValueFromString(JPT.Exec(strCmd))


def Scaling(crlParts, dlScaleVector=[1.0, 1.0, 1.0], dlScaleCentre=[0.0, 0.0, 0.0], crCoordinate=None, bCreateNew=False, bCopyLBC=False, bCopyProperty=False, bUsePartCenter=True, bCopyReference=True):
    bCreateNew_b = 1 if bCreateNew else 0
    bCopyLBC_b = 1 if bCopyLBC else 0
    bCopyProperty_b = 1 if bCopyProperty else 0
    bUsePartCenter_b = 1 if bUsePartCenter else 0
    bCopyReference_b = 1 if bCopyReference else 0
    strCmd = 'ScaleBody({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        dlScaleVector,
        dlScaleCentre,
        str(crCoordinate) if crCoordinate is not None else '0:0',
        bCreateNew_b,
        bCopyLBC_b,
        bCopyProperty_b,
        bUsePartCenter_b,
        bCopyReference_b,)
    return getBoolValueFromString(JPT.Exec(strCmd))


def Mirror(crlParts, veclPoint=[[0.0, 0.0, 0.0]], dOffset=0.0, bCreateNewPart=True, bCopyLBC=False, bCopyProperty=False, bRemoveDupFace=True, bMergeNode=False, dTol=1e-05, bCopyReference=True):
    veclPoint = [[JPT.ConvertFromMacroUnit(
        v, JPT.UnitType.Unit_Length, "mm") for v in vec] for vec in veclPoint]
    dOffset = JPT.ConvertFromMacroUnit(dOffset, JPT.UnitType.Unit_Length, "mm")
    bCreateNewBody_b = 1 if bCreateNewPart else 0
    bCopyLBC_b = 1 if bCopyLBC else 0
    bCopyProperty_b = 1 if bCopyProperty else 0
    bRemoveDupFace_b = 1 if bRemoveDupFace else 0
    bMergeNode_b = 1 if bMergeNode else 0
    dTol = JPT.ConvertFromMacroUnit(dTol, JPT.UnitType.Unit_Length, "mm")
    bCopyReference_b = 1 if bCopyReference else 0
    strCmd = 'MirrorBody({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        veclPoint,
        dOffset,
        bCreateNewBody_b,
        bCopyLBC_b,
        bCopyProperty_b,
        bRemoveDupFace_b,
        bMergeNode_b,
        dTol,
        bCopyReference_b)
    return JPT.Exec(strCmd)


def Position(crlParts, dllPoints=[[0.0, 0.0, 0.0]], bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False):
    dllPoints = [[JPT.ConvertFromMacroUnit(
        v, JPT.UnitType.Unit_Length, "mm") for v in vec] for vec in dllPoints]
    bCreateNewPart_b = 1 if bCreateNewPart else 0
    bCopyLBC_b = 1 if bCopyLBC else 0
    bCopyProperty_b = 1 if bCopyProperty else 0
    strCmd = 'PositionBody({0}, {1}, {2}, {3}, {4})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        dllPoints,
        bCreateNewPart_b,
        bCopyLBC_b,
        bCopyProperty_b)
    return getBoolValueFromString(JPT.Exec(strCmd))


def Translation(crlParts, dlTranslationVector=[0.0, 0.0, 0.0], crLocalCoordinate=None, bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, bCopyReference=False, iCopyCount=1):
    bCreateNewPart_b = 1 if bCreateNewPart else 0
    bCopyLBC_b = 1 if bCopyLBC else 0
    bCopyProperty_b = 1 if bCopyProperty else 0
    bCopyReference_b = 1 if bCopyReference else 0
    strCmd = 'TranslateBody({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        dlTranslationVector,
        str(crLocalCoordinate) if crLocalCoordinate is not None else '0:0',
        bCreateNewPart_b,
        bCopyLBC_b,
        bCopyProperty_b,
        bCopyReference_b,
        iCopyCount)
    return getListCursorValueByStr(JPT.Exec(strCmd))


def MatingFace(crlParts, crSrcFace, crDstFace, crSrcEdge=None, crDstEdge=None, crSrcNode=None, crDstNode=None, iFaceOpposite=0, dEdgeAngle=0, iEdgeOpposite=0, iAlignMethodType=0, iAdjustPointType=0, iAdjustProjectionType=0, dlAlignVector=[0, 0, 0], dlAdjustPoint=[0, 0, 0], dlAdjustVector=[0, 0, 0], bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, bIsPreview=False, crlCoordSyss=[], bCopyReference=True):
    dEdgeAngle = JPT.ConvertFromMacroUnit(
        dEdgeAngle, JPT.UnitType.Unit_Angle, "deg")
    m_bCreateNewBody_b = 1 if bCreateNewPart else 0
    m_bCopyLBC_b = 1 if bCopyLBC else 0
    m_bCopyProperty_b = 1 if bCopyProperty else 0
    m_isPreview_b = 1 if bIsPreview else 0
    bCopyReference_b = 1 if bCopyReference else 0
    strCmd = 'TransMatingFace({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        str(crSrcFace) if crSrcFace is not None else '0:0',
        str(crDstFace) if crDstFace is not None else '0:0',
        str(crSrcEdge) if crSrcEdge is not None else '0:0',
        str(crDstEdge) if crDstEdge is not None else '0:0',
        str(crSrcNode) if crSrcNode is not None else '0:0',
        str(crDstNode) if crDstNode is not None else '0:0',
        iFaceOpposite,
        dEdgeAngle,
        iEdgeOpposite,
        iAlignMethodType,
        iAdjustPointType,
        iAdjustProjectionType,
        dlAlignVector,
        dlAdjustPoint,
        dlAdjustVector,
        m_bCreateNewBody_b,
        m_bCopyLBC_b,
        m_bCopyProperty_b,
        m_isPreview_b,
        str(crlCoordSyss) if crlCoordSyss != [None] else '[0:0]',
        bCopyReference_b)
    return JPT.Exec(strCmd)


def CylinderFace(crSourceFace, crDestinationFace, bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, bCopyReference=False):
    bCreateNewPart_b = 1 if bCreateNewPart else 0
    bCopyLBC_b = 1 if bCopyLBC else 0
    bCopyProperty_b = 1 if bCopyProperty else 0
    bCopyReference_b = 1 if bCopyReference else 0
    strCmd = 'Transform_CylinderFace({0}, {1}, {2}, {3}, {4}, {5})'.format(
        str(crSourceFace) if crSourceFace is not None else '0:0',
        str(crDestinationFace) if crDestinationFace is not None else '0:0',
        bCreateNewPart_b,
        bCopyLBC_b,
        bCopyProperty_b,
        bCopyReference_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))


def ThreePoints(crlTargetParts, poslOriginalPoints=[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], poslNextPoints=[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, bCopyReference=False):
    bCreateNewPart_b = 1 if bCreateNewPart else 0
    bCopyLBC_b = 1 if bCopyLBC else 0
    bCopyProperty_b = 1 if bCopyProperty else 0
    bCopyReference = 1 if bCopyReference else 0
    strCmd = 'Transform3Points({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(
        str(crlTargetParts) if crlTargetParts != [None] else '[0:0]',
        poslOriginalPoints,
        poslNextPoints,
        bCreateNewPart_b,
        bCopyLBC_b,
        bCopyProperty_b,
        bCopyReference)
    return getListCursorValueByStr(JPT.Exec(strCmd))


def AxisAlignment(crlTargetEdges, crlReferenceEdges, crlParts, bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, bCopyReference=True, iSolution=1, dTranslationLength=0.0):
    bCreateNewPart_b = 1 if bCreateNewPart else 0
    bCopyLBC_b = 1 if bCopyLBC else 0
    bCopyProperty_b = 1 if bCopyProperty else 0
    bCopyReference_b = 1 if bCopyReference else 0
    strCmd = 'TransformAxisAlignment({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})'.format(
        str(crlTargetEdges) if crlTargetEdges != [None] else '[0:0]',
        str(crlReferenceEdges) if crlReferenceEdges != [None] else '[0:0]',
        str(crlParts) if crlParts != [None] else '[0:0]',
        bCreateNewPart_b,
        bCopyLBC_b,
        bCopyProperty_b,
        bCopyReference_b,
        iSolution,
        dTranslationLength)
    return getListCursorValueByStr(JPT.Exec(strCmd))


def PlaneAlignment(crlTargetFaces, crlReferenceFaces, crlParts, bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, bCopyReference=True, iSolution=1, dTranslationLength=0.0, crCenterNode=None, crCenterEdge=None):
    bCreateNewPart_b = 1 if bCreateNewPart else 0
    bCopyLBC_b = 1 if bCopyLBC else 0
    bCopyProperty_b = 1 if bCopyProperty else 0
    bCopyReference_b = 1 if bCopyReference else 0
    strCmd = 'TransformPlaneAlignment({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10})'.format(
        str(crlTargetFaces) if crlTargetFaces != [None] else '[0:0]',
        str(crlReferenceFaces) if crlReferenceFaces != [None] else '[0:0]',
        str(crlParts) if crlParts != [None] else '[0:0]',
        bCreateNewPart_b,
        bCopyLBC_b,
        bCopyProperty_b,
        bCopyReference_b,
        iSolution,
        dTranslationLength,
        str(crCenterNode) if crCenterNode is not None else '0:0',
        str(crCenterEdge) if crCenterEdge is not None else '0:0')
    return getListCursorValueByStr(JPT.Exec(strCmd))

def OOBBAlignment(
    crReferencePart=None,
    crMovingPart=None,
    iPositionType=0,
    dlTranslation=[0.0, 0.0, 0.0],
    dlRotation=[0.0, 0.0, 0.0],
):
    strCmd = 'ALIGNMENTBYOOBB({0}, {1}, {2}, {3}, {4})'.format(
        str(crReferencePart) if crReferencePart is not None else '0:0',
        str(crMovingPart) if crMovingPart is not None else '0:0',
        iPositionType,
        dlTranslation,
        dlRotation)
    return getBoolValueFromString(JPT.Exec(strCmd))

def BestFit(crlStaticTarget, crlDynamicTarget, dError=0.00000001, iMaxCycle=400, iAlgorithmsType=0):
    strCmd = 'BestFitFunc({0}, {1}, {2}, {3}, {4})'.format(
        str(crlStaticTarget) if crlStaticTarget != [None] else '[0:0]',
        str(crlDynamicTarget) if crlDynamicTarget != [None] else '[0:0]',
        dError,
        iMaxCycle,
        iAlgorithmsType)
    return JPT.Exec(strCmd)