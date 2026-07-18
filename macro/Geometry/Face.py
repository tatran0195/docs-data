import JPT
from macro_defs import *
from macroTypes import *


def FourEdges(crlEdges):
    strCmd = 'CreateFaceFromFourEdges({0})'.format(
        str(crlEdges) if crlEdges != [None] else '[0:0]')
    return getCursorValueByStr(JPT.Exec(strCmd))


def FromMesh(crFace):
    strCmd = 'CreateFaceFromMeshFace([{0}])'.format(
        str(crFace) if crFace != [None] else '0:0')
    return getCursorValueByStr(JPT.Exec(strCmd))


def CreateSmoothFace(
        bInterPoration,
        crlTargets,
        iElemGeneration,
        dGradation,
        iEnableFaceSmooth,
        crTargetPart
):
    InterPoration_b = 1 if bInterPoration else 0
    strCmd = 'CreateSmoothFace({0}, {1}, {2}, {3}, {4}, {5})'.format(
        InterPoration_b,
        str(crlTargets) if crlTargets != [None] else '[0:0]',
        iElemGeneration,
        dGradation,
        iEnableFaceSmooth,
        str(crTargetPart) if crTargetPart is not None else '0:0')
    return JPT.Exec(strCmd)


def Edges(
        crlEdges,
        crlParts=[],
        crlNodes=[],
        bSharedFace=False,
        bSmoothFace=False,
        bCreatePart=False,
        bImproved=False,
        bBarsOnly=False,
        bOnlyOnePart=True,
        bIncludeMidNodes=False
):
    bSharedFace_b = 1 if bSharedFace else 0
    bSmoothFace_b = 1 if bSmoothFace else 0
    bCreatePart_b = 1 if bCreatePart else 0
    bImproved_b = 1 if bImproved else 0
    bBarsOnly_b = 1 if bBarsOnly else 0
    bOnlyOnePart_b = 1 if bOnlyOnePart else 0
    bIncludeMidNodes_b = 1 if bIncludeMidNodes else 0
    strCmd = 'CreateFaceFromEdges({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9})'.format(
        str(crlEdges) if crlEdges != [None] else '[0:0]',
        str(crlParts) if crlParts != [None] else '[0:0]',
        str(crlNodes) if crlNodes != [None] else '[0:0]',
        bSharedFace_b,
        bSmoothFace_b,
        bCreatePart_b,
        bImproved_b,
        bBarsOnly_b,
        bOnlyOnePart_b,
        bIncludeMidNodes_b)
    return getCursorValueByStr(JPT.Exec(strCmd))


def Elements(crlElems, bSharedFace=False):
    bSharedFace_b = 1 if bSharedFace else 0
    strCmd = 'CreateFaceByElem({0}, {1})'.format(
        str(crlElems) if crlElems != [None] else '[0:0]',
        bSharedFace_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))


def ExtendFace(
        crEdge,
        crFace=None,
        crRefFace=None,
        crFirstNode=None,
        crSecondNode=None,
        crElemEdge=[],
        extendFaceDirection=EXTEND_FACE_DIRECTION(),
        extendFaceMesh=EXTEND_FACE_MESH(),
        extendFaceOption=EXTEND_FACE_OPTION()
):
    extendFaceDirectionStr = extendFaceDirection.toNativeStr(False, True)
    extendFaceMeshStr = extendFaceMesh.toNativeStr(False)
    extendFaceOptionStr = extendFaceOption.toNativeStr(False)
    strCmd = 'ExtendFace({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})'.format(
        str(crEdge) if crEdge != None else '0:0',
        str(crFace) if crFace != None else '0:0',
        str(crRefFace) if crRefFace != None else '0:0',
        str(crFirstNode) if crFirstNode != None else '0:0',
        str(crSecondNode) if crSecondNode != None else '0:0',
        str(crElemEdge) if crElemEdge != [] else '0:0-0:0',
        extendFaceDirectionStr,
        extendFaceMeshStr,
        extendFaceOptionStr,
    )
    return getCursorValueByStr(JPT.Exec(str(strCmd)))
    ...


def SmoothFace(
        crlTargets,
        iElementGeneration=0,
        dGradation=1,
        bFaceSmooth=True,
        crlTargetParts=[],
        bInterpolation=False,
):
    strCmd = 'CreateSmoothFaceGUI({0}, {1}, {2}, {3}, {4}, {5})'.format(
        str(crlTargets) if crlTargets != [] else '[]',
        iElementGeneration,
        dGradation,
        1 if bFaceSmooth else 0,
        str(crlTargetParts) if crlTargetParts != [] else '[]',
        1 if bInterpolation else 0,
    )
    return getCursorValueByStr(JPT.Exec(strCmd))
    ...
