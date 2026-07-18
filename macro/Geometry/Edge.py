import JPT
from macro_defs import *
from macroTypes import *

def Line(dllPoints, crlFaces, bBreakFace=True):
    bBreakFace_b = 1 if bBreakFace else 0
    strCmd = 'ImprintLineS({0}, {1}, {2})'.format(
        dllPoints,
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        bBreakFace_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def Spline(dllPoints, crlFaces, bBreakFace=True):
    bBreakFace_b = 1 if bBreakFace else 0
    strCmd = 'GeoImprintSplineS({0}, {1}, {2})'.format(
        dllPoints,
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        bBreakFace_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def PlanarLine(dllPoints, crlFaces, crLocalCoordinate=None, iAxisPlane=0, bBreakFace=True):
    bBreakFace_b = 1 if bBreakFace else 0
    strCmd = 'ImprintPlannarLineS({0}, {1}, {2}, {3}, {4})'.format(
        dllPoints,
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        str(crLocalCoordinate) if crLocalCoordinate is not None else '0:0',
        iAxisPlane,
        bBreakFace_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def Circle(veclPositions, crlTargetFace, dInRadius=1, dOutRadius=4, iNoOfLayer=1, iNoOfDiv=30, bBreakFace=True):
    dInRadius = JPT.ConvertFromMacroUnit(dInRadius, JPT.UnitType.Unit_Length, "mm")
    dOutRadius = JPT.ConvertFromMacroUnit(dOutRadius, JPT.UnitType.Unit_Length, "mm")
    bBreakFace_b = 1 if bBreakFace else 0
    strCmd = 'ImprintCircleS({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(
        veclPositions,
        str(crlTargetFace) if crlTargetFace != [None] else '[0:0]',
        dInRadius,
        dOutRadius,
        iNoOfLayer,
        iNoOfDiv,
        bBreakFace_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def PerpendicularLineOfEdge(crlNodes, crlFaces, dOffsetDistance=0.0, bBreakFace=True):
    bBreakFace_b = 1 if bBreakFace else 0
    strCmd = 'ImprintPerpendicularLine({0}, {1}, {2}, {3})'.format(
        str(crlNodes) if crlNodes != [None] else '[0:0]',
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        dOffsetDistance,
        bBreakFace_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def ExtendLine(crlEdges, iMethod=0, iEnd=0, iNoFittingPoints=3, iDiv=2, bBreakFace=True):
    bBreakFace_b = 1 if bBreakFace else 0
    strCmd = 'ImprintExtendLine({0}, {1}, {2}, {3}, {4}, {5})'.format(
        str(crlEdges) if crlEdges != [None] else '[0:0]',
        iMethod,
        iEnd,
        iNoFittingPoints,
        iDiv,
        bBreakFace_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def ElementEdges(crplElemEdges, bBreakEdge=True):
    bBreakEdge_b = 1 if bBreakEdge else 0
    strCmd = 'CreateEdgeByElemEdge({0}, {1})'.format(
        str(crplElemEdges),
        bBreakEdge_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def Angle(crplElemEdges, dEdgeAngle=135.0, bCurvature=False, bBreakFace=True):
    bCurvature_b = 1 if bCurvature else 0
    bBreakFace_b = 1 if bBreakFace else 0
    strCmd = 'CreateEdgeByElemEdgeAngle({0}, {1}, {2}, {3})'.format(
        str(crplElemEdges),
        dEdgeAngle,
        bCurvature_b,
        bBreakFace_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def NodeShortestPath(crFirstNode, crSecondNode, bBreakFace=True):
    bBreakFace_b = 1 if bBreakFace else 0
    strCmd = 'CreateEdgeBy2NodeShortestPath({0}, {1}, {2})'.format(
        str(crFirstNode) if crFirstNode is not None else '0:0',
        str(crSecondNode) if crSecondNode is not None else '0:0',
        bBreakFace_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def OffsetLine(crlFaces, crlEdges, bBreakFace=True, dOffsetDistance=0.0, iLayerNumber=1, bMerge=True, bExtend=True, iOffsetMethod=0, dlOffsetDistance=[], iImprintMethod=2):
    bBreakFace_b = 1 if bBreakFace else 0
    bMerge_b = 1 if bMerge else 0
    bExtend_b = 1 if bExtend else 0
    bAutoCollapse_b = 0
    strCmd = 'ImprintOffsetLineS({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10})'.format(
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        str(crlEdges) if crlEdges != [None] else '[0:0]',
        bBreakFace_b,
        dOffsetDistance,
        iLayerNumber,
        bMerge_b,
        bExtend_b,
        iOffsetMethod,
        dlOffsetDistance,
        bAutoCollapse_b,
        iImprintMethod)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def SplineFreeEdges(crlNodes, iEnableArc=0, crPart=None, strBarName=""):
    strCmd = 'CreateEdgeSpline({0}, {1}, {2}, {3})'.format(
        str(crlNodes) if crlNodes != [None] else '[0:0]',
        iEnableArc,
        str(crPart) if crPart is not None else '0:0',
        '"' + strBarName + '"')
    return JPT.Exec(strCmd)

def ClosedLine(veclPositions, crlTargetFace, bBreakFace=True):
    bBreakFace_b = 1 if bBreakFace else 0
    strCmd = 'ImprintCloseLineS({0}, {1}, {2})'.format(
        veclPositions,
        str(crlTargetFace) if crlTargetFace != [None] else '[0:0]',
        bBreakFace_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def PerpendicularCylinderLine(crlNodes, crlFaces, iMethod=0, dOffset=0.0, bOppositeSide=False, bBreakFace=True):
    bOppositeSide_b = 1 if bOppositeSide else 0
    bBreakFace_b = 1 if bBreakFace else 0
    strCmd = 'ImprintPerpendicularCylinderLineS({0}, {1}, {2}, {3}, {4}, {5})'.format(
        str(crlNodes) if crlNodes != [None] else '[0:0]',
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        iMethod,
        dOffset,
        bOppositeSide_b,
        bBreakFace_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def IntersectionLine(crlFaces=[], bBreakFace=True):
    bBreakFace_b = 1 if bBreakFace else 0
    strCmd = 'Imprint_Intersection_LineS({0}, {1})'.format(
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        bBreakFace_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def ProjectLine(crlEdges=[], crlFaces=[], crlNodes=[], bBreakFace=True, iType=0, bCheckGap=False, dGap=0.0):
    bBreakFace_b = 1 if bBreakFace else 0
    bCheckGap_b = 1 if bCheckGap else 0
    strCmd = 'Imprint_Projection_LineS({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(
        str(crlEdges) if crlEdges != [None] else '[0:0]',
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        str(crlNodes) if crlNodes != [None] else '[0:0]',
        bBreakFace_b,
        iType,
        bCheckGap_b,
        dGap)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def PerpendicularLineToEdge(crNode=None, crEdge=None, crlFaces=[], bBreakFace=True, bExtend=True, bAuto=False, dLimitAngle=135.0):
    bBreakFace_b = 1 if bBreakFace else 0
    bExtend_b = 1 if bExtend else 0
    bAuto_b = 1 if bAuto else 0
    strCmd = 'ImprintPerpendicularLine2({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(
        str(crNode) if crNode is not None else '0:0',
        str(crEdge) if crEdge is not None else '0:0',
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        bBreakFace_b,
        bExtend_b,
        bAuto_b,
        dLimitAngle)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def LineInBetween(crlEdges, crlFaces, iNumLine=1, bBreakFace=True, bExtend=True):
    bBreakFace_b = 1 if bBreakFace else 0
    bExtend_b = 1 if bExtend else 0
    strCmd = 'ImprintMiddleLine({0}, {1}, {2}, {3}, {4})'.format(
        str(crlEdges) if crlEdges != [None] else '[0:0]',
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        iNumLine,
        bBreakFace_b,
        bExtend_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))
