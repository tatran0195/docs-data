import JPT
from macro_defs import *
from macroTypes import *


def CADTrim(crlFaces=[], crlParts=[], dTrimSize=1.0, dTrimAngle=15.0):
    dTrimSize = JPT.ConvertFromMacroUnit(
        dTrimSize, JPT.UnitType.Unit_Length, "mm")
    dTrimAngle = JPT.ConvertFromMacroUnit(
        dTrimAngle, JPT.UnitType.Unit_Angle, "deg")
    strCmd = 'GeometryCADTrim({0}, {1}, {2}, {3})'.format(
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        str(crlParts) if crlParts != [None] else '[0:0]',
        dTrimSize,
        dTrimAngle)
    return JPT.Exec(strCmd)


def StitchEdge(crlMaster, crlSlave, dTolerance=0.3, bKeepSlave=True):
    dTolerance = JPT.ConvertFromMacroUnit(
        dTolerance, JPT.UnitType.Unit_Length, "mm")
    bKeepSlave_b = 1 if bKeepSlave else 0
    strCmd = 'StitchEdge({2}, {3}, {0}, {1})'.format(
        str(crlMaster) if crlMaster != [None] else '[0:0]',
        str(crlSlave) if crlSlave != [None] else '[0:0]',
        dTolerance,
        bKeepSlave_b)
    return JPT.Exec(strCmd)


def LogoRemoval(crlStartFaces, crlStopFaces, iLayers=5, bMergeFaces=False):
    merge_faces_b = 1 if bMergeFaces else 0
    strCmd = 'LogoRemoval({0}, {1}, {2}, {3})'.format(
        str(crlStartFaces) if crlStartFaces != [None] else '[0:0]',
        str(crlStopFaces) if crlStopFaces != [None] else '[0:0]',
        iLayers,
        merge_faces_b)
    return JPT.Exec(strCmd)


def ShellAsm(crlPartK=[], crlFaceK=[], dTol=0.2, iElemType=0, bSkipTiny=False):
    bSkipTiny_b = 1 if bSkipTiny else 0
    strCmd = 'ShellAsm({0}, {1}, {2}, {3}, {4})'.format(
        crlPartK,
        crlFaceK,
        dTol,
        iElemType,
        bSkipTiny_b)
    return JPT.Exec(strCmd)


def SquareUpFillet(crlFaces):
    strCmd = 'SquareUpFillet({0})'.format(
        str(crlFaces) if crlFaces != [None] else '[0:0]')
    return JPT.Exec(strCmd)


def MakeFillet(crlEdges, dRadius=1.0):
    dRadius = JPT.ConvertFromMacroUnit(dRadius, JPT.UnitType.Unit_Length, "mm")
    strCmd = 'MakeFillet({0}, {1})'.format(
        str(crlEdges) if crlEdges != [None] else '[0:0]',
        dRadius)
    return JPT.Exec(strCmd)

def CreateROnBar(crlEdges, dRadius=0.0):
    dRadius = JPT.ConvertFromMacroUnit(dRadius, JPT.UnitType.Unit_Length, "mm")
    strCmd = 'Create_R_On_Bar({0}, {1})'.format(
        str(crlEdges) if crlEdges != [None] else '[0:0]',
        dRadius)
    return getCursorValueByStr(JPT.Exec(strCmd))

def MakeFacePlanar(dlPlanePt1=[0.0, 0.0, 0.0], dlPlanePt2=[0.0, 0.0, 0.0], dlPlanePt3=[0.0, 0.0, 0.0], ilFaceIds=[], iMergeFace=0):
    strCmd = 'MakeFacePlanar({0}, {1}, {2}, {3}, {4})'.format(
        dlPlanePt1,
        dlPlanePt2,
        dlPlanePt3,
        ilFaceIds,
        iMergeFace)
    return JPT.Exec(strCmd)


def AdjustHalfCylinder(poslPoint=[], crlFaces=[], crCoord=None, iAxisPlane=0, bDivideFace=True, crlParts=[], bMergeEdge=True):
    bDivideFace_b = 1 if bDivideFace else 0
    bMergeEdge_b = 1 if bMergeEdge else 0
    strCmd = 'MeshEditAdjustHalfCylinderCoordinateCr({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(
        poslPoint,
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        str(crCoord) if crCoord is not None else '0:0',
        iAxisPlane,
        bDivideFace_b,
        str(crlParts) if crlParts != [None] else '[0:0]',
        bMergeEdge_b)
    return getBoolValueFromString(JPT.Exec(strCmd))


def FCircVertexAdjust(crlParts, bFullCylinder=False, bCylinderMoreThan90=False, dMinRadius=0.0):
    bFullCylinder_b = 1 if bFullCylinder else 0
    bCylinderMoreThan90_b = 1 if bCylinderMoreThan90 else 0
    strCmd = 'AdjustCircleVertex({0}, {1}, {2}, {3})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        bFullCylinder_b,
        bCylinderMoreThan90_b,
        dMinRadius)
    return getBoolValueFromString(JPT.Exec(strCmd))


def ExtractSurfaces(crlFaces, dFaceAngle=60.0, strName="ExtractFace_1", bMergePart=False):
    bMergePart_b = 1 if bMergePart else 0
    strCmd = 'MeshEditExtractSurfaces({0}, {1}, {2}, {3})'.format(
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        dFaceAngle,
        '"' + strName + '"',
        bMergePart_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))


def RemoveRibBoss(crlFaces, dGradiation=1.0, iContinuity=1):
    strCmd = 'Remove_Rib_Boss({0}, {1}, {2})'.format(
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        dGradiation,
        iContinuity)
    return JPT.Exec(strCmd)


def AdvancedShellAssembly(crlParts=[], crlFaces=[], iMeshType=0, bSelfIntersection=False, iMethod=3, dGapTol=2.1, bBreakFace=True, mEnableCross=False):
    _bSelfIntersection_b = 1 if bSelfIntersection else 0
    dGapTol = JPT.ConvertFromMacroUnit(dGapTol, JPT.UnitType.Unit_Length, "mm")
    _bBreakFace_b = 1 if bBreakFace else 0
    _mEnableCross_b = 1 if mEnableCross else 0
    strCmd = 'ShellAssyGeneral({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        iMeshType,
        _bSelfIntersection_b,
        iMethod,
        dGapTol,
        _bBreakFace_b,
        _mEnableCross_b)
    return JPT.Exec(strCmd)


def ExtractRefSurfaces(crlRefFaces, dFaceAngle=60.0, strName="ExtractFace_1", bIsMergePart=False):
    bIsMergePart_b = 1 if bIsMergePart else 0
    strCmd = 'MeshEditExtractRefSurfaces({0}, {1}, {2}, {3})'.format(
        str(crlRefFaces) if crlRefFaces != [None] else '[0:0]',
        dFaceAngle,
        '"' + strName + '"',
        bIsMergePart_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))


def ShipFormMorphing(crlFace=[], crlCornerNode=[], nNumOfSample=10, nControlPointCounts=[7, 7], dFlexsiableTol=0.02):
    strCmd = 'ShipHull({0}, {1}, {2}, {3}, {4})'.format(
        str(crlFace) if crlFace != [None] else '[0:0]',
        str(crlCornerNode) if crlCornerNode != [None] else '[0:0]',
        nNumOfSample,
        nControlPointCounts,
        dFlexsiableTol)
    return JPT.Exec(strCmd)


def MakeFaceSmoothFunc(crlFaces=[], iCycles=50, dFactor=0.3, bIncludeBoundaryEdge=False):
    bIncludeBoundaryEdge_b = 1 if bIncludeBoundaryEdge else 0
    strCmd = 'MakeFaceSmoothFunc({0}, {1}, {2}, {3})'.format(
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        iCycles,
        dFactor,
        bIncludeBoundaryEdge_b)
    return JPT.Exec(strCmd)


def ShapeSearch(
        crlParts,
        crlRefEdges=[],
        iGroupOption=0,
        strGroupName="",
        listShapeSearchOptions=[],
        bConvexOption=False,
        bConcaveOption=False,
):
    listShapeSearchOptionsStr = '[{0}]'.format(
        ", ".join(shapeSearch.toNativeStr() for shapeSearch in listShapeSearchOptions))
    strCmd = 'ShapeSearch({0}, {1}, {2}, {3}, {4}, {5})'.format(
        str(crlParts) if crlParts != [None] else '[]',
        str(crlRefEdges) if crlRefEdges != [None] else '[]',
        iGroupOption,
        '"' + strGroupName + '"',
        listShapeSearchOptionsStr,
        [1 if bConvexOption else 0, 1 if bConcaveOption else 0])
    return getListCursorValueByStr(JPT.Exec(strCmd))
