import JPT
from macro_defs import *
from macroTypes import *

def DelCircChamfer(crlParts, dMaxThick=0.1, dMinThick=2):
    strCmd = 'DelCircChamfer({0}, {1}, {2})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        dMaxThick,
        dMinThick)
    return JPT.Exec(strCmd)

def Fillet(crlParts=[], crlFaces=[], dMinAngle=1.0, dMaxAngle=10.0, dMinFaceWidth=1.0, dMaxFaceWidth=10.0, dMinCurveRadius=0.0, dMaxCurveRadius=171, dScale=1.0):
    dMinAngle = JPT.ConvertFromMacroUnit(dMinAngle, JPT.UnitType.Unit_Length, "mm")
    dMaxAngle = JPT.ConvertFromMacroUnit(dMaxAngle, JPT.UnitType.Unit_Length, "mm")
    dMinFaceWidth = JPT.ConvertFromMacroUnit(dMinFaceWidth, JPT.UnitType.Unit_Length, "mm")
    dMaxFaceWidth = JPT.ConvertFromMacroUnit(dMaxFaceWidth, JPT.UnitType.Unit_Length, "mm")
    dMinCurveRadius = JPT.ConvertFromMacroUnit(dMinCurveRadius, JPT.UnitType.Unit_Length, "mm")
    dMaxCurveRadius = JPT.ConvertFromMacroUnit(dMaxCurveRadius, JPT.UnitType.Unit_Length, "mm")
    strCmd = 'FindFeatureFillet({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        dMinAngle,
        dMaxAngle,
        dMinFaceWidth,
        dMaxFaceWidth,
        dMinCurveRadius,
        dMaxCurveRadius,
        dScale)
    return JPT.Exec(strCmd)

def Faces(crlParts,iFaceType=0, bCylinder=True, bDisc=False, bFourCorners=True, dMinThickness=0.1, dMaxThickness=2.0, crlFaces=[]):
    bCylinder_b = 1 if bCylinder else 0
    bDisc_b = 1 if bDisc else 0
    bFourCorners_b = 1 if bFourCorners else 0
    strCmd = 'Geom_FindFeatures({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        1,
        iFaceType,
        '[0:0]',
        bCylinder_b,
        bDisc_b,
        bFourCorners_b,
        dMinThickness,
        dMaxThickness,
        1.0,
        2.0,
        str(crlFaces) if crlFaces != [None] else '[0:0]')
    return JPT.Exec(strCmd)

def Edges(crlParts ,iEdgeType=0, crlEdges=[], dDiameterMin=1.0, dDiameterMax=2.0, crlFaces=[]):
    strCmd = 'Geom_FindFeatures({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        2,
        iEdgeType,
        str(crlEdges) if crlEdges != [None] else '[0:0]',
        0,
        0,
        0,
        0.1,
        2.0,
        dDiameterMin,
        dDiameterMax,
        str(crlFaces) if crlFaces != [None] else '[0:0]')
    return JPT.Exec(strCmd)

def Edge(crlParts=[], iEdgeType=0, crlEdges=[], dDiameterMin=1.0, dDiameterMax=2.0, crlFaces=[]):
    strCmd = 'GeometryFindFeatureEdge({0}, {1}, {2}, {3}, {4}, {5})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        iEdgeType,
        str(crlEdges) if crlEdges != [None] else '[0:0]',
        dDiameterMin,
        dDiameterMax,
        str(crlFaces) if crlFaces != [None] else '[0:0]')
    return getListCursorValueByStr(JPT.Exec(strCmd))

def Face(crlParts=[], crlFaces=[], iType=0, bCylinder=True, bDisc=False, bFourCorners=True, dMinThickness=0.1, dMaxThickness=2.0, dMinFaceWidth=0.1, dMaxFaceWidth=10.0, dMinCurveRadius=0.1, dMaxCurveRadius=10, dAngleMin=0.0, dAngleMax=171.0, bConvex=True, bConcave=False):
    bCylinder_b = 1 if bCylinder else 0
    bDisc_b = 1 if bDisc else 0
    bFourCorners_b = 1 if bFourCorners else 0
    bConvex_b = 1 if bConvex else 0
    bConcave_b = 1 if bConcave else 0
    strCmd = 'GeometryFindFeatureFace({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        iType,
        bCylinder_b,
        bDisc_b,
        bFourCorners_b,
        dMinThickness,
        dMaxThickness,
        dMinFaceWidth,
        dMaxFaceWidth,
        dMinCurveRadius,
        dMaxCurveRadius,
        dAngleMin,
        dAngleMax,
        bConvex_b,
        bConcave_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))
