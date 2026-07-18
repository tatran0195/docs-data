import JPT
from macro_defs import *
from macroTypes import *

def Circular(crlFaces=[], dAngle=360, dTol=0.0000001, iLayer=36, vecAxisPt=[0.0,0.0,0.0], vecAxisVect=[1.0,0.0,0.0], bInterfaceElem=False, bExtrusion=False, dTranslationExtrusion=0.0, dBDeleteOriginalParts=0.0):
    bInterfaceElem_b = 1 if bInterfaceElem else 0
    bExtrusion_b = 1 if bExtrusion else 0
    strCmd = 'HexSweepCircular({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9})'.format(
        crlFaces,
        dAngle,
        dTol,
        iLayer,
        vecAxisPt,
        vecAxisVect,
        bInterfaceElem_b,
        bExtrusion_b,
        dTranslationExtrusion,
        dBDeleteOriginalParts)
    return JPT.Exec(strCmd)

def FaceToFace(crSrcFace, crDstFace, bDeleteOriginalParts=True):
    bDeleteOriginalParts_b = 1 if bDeleteOriginalParts else 0
    strCmd = 'HexSweepFaceToFace({0}, {1}, {2})'.format(
        str(crSrcFace) if crSrcFace is not None else '0:0',
        str(crDstFace) if crDstFace is not None else '0:0',
        bDeleteOriginalParts_b)
    return JPT.Exec(strCmd)

def Layer(crlFaces=[], dFrontWidth=0.0, dBackWidth=0.0, iFrontLayers=1, iBackLayers=0, iBaseFaceType=0, iSeparate=0):
    strCmd = 'HexSweepLayer({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(
        crlFaces,
        dFrontWidth,
        dBackWidth,
        iFrontLayers,
        iBackLayers,
        iBaseFaceType,
        iSeparate)
    return JPT.Exec(strCmd)

def Linear(crlFaces=[], dLength=10, iLayer=10, dlSweepDirection=[], bInterfaceElemFlag=False, iLinearMethod=0, bDeleteOriginalParts=False, bDeleteTargetParts=False, iMethodBias=0, dFactor=2.0, iProgression=0):
    bInterfaceElemFlag_b = 1 if bInterfaceElemFlag else 0
    bDeleteOriginalParts_b = 1 if bDeleteOriginalParts else 0
    bDeleteTargetParts_b = 1 if bDeleteTargetParts else 0
    strCmd = 'HexSweepLinear({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10})'.format(
        crlFaces,
        dLength,
        iLayer,
        dlSweepDirection,
        bInterfaceElemFlag_b,
        iLinearMethod,
        bDeleteOriginalParts_b,
        bDeleteTargetParts_b,
        iMethodBias,
        dFactor,
        iProgression)
    return JPT.Exec(strCmd)

def Curve(crFace=None, crlEdges=[], crlRefEdge=[], dMeshSize=0.1):
    strCmd = 'SweepCloseLoopShape({0}, {1}, {2}, {3})'.format(
        str(crFace) if crFace is not None else '0:0',
        str(crlEdges) if crlEdges != [None] else '[0:0]',
        str(crlRefEdge) if crlRefEdge != [None] else '[0:0]',
        dMeshSize)
    return JPT.Exec(strCmd)

def FromMidPlane(crlParts=[], bRef=True):
    bRef_b = 1 if bRef else 0
    strCmd = 'Shell2Hex({0}, {1})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        bRef_b)
    return JPT.Exec(strCmd)
