import JPT
from macro_defs import *
from macroTypes import *

def Faces(dAngle=0.0, bIncludeStopFaces=False, iNumOfLayers=1, crlStartFaces=[] , crlStopFaces=[]):
    bIncludeStopFace_b = 1 if bIncludeStopFaces else 0
    strCmd = 'Geom_ShowAdjacent({0}, {1}, {2}, {3}, {4}, {5})'.format(
        dAngle,
        bIncludeStopFace_b,
        iNumOfLayers,
        0,
        crlStartFaces,
        crlStopFaces)
    return JPT.Exec(strCmd)

def Elements(dAngle=0.0, bIncludeStopElems=False, iNumOfLayers=1, crlStartElems=[], crlStopElems=[]):
    bIncludeStopElem_b = 1 if bIncludeStopElems else 0
    strCmd = 'Geom_ShowAdjacent_Elements({0}, {1}, {2}, {3}, {4}, {5})'.format(
        dAngle,
        bIncludeStopElem_b,
        iNumOfLayers,
        0,
        crlStartElems,
        crlStopElems)
    return JPT.Exec(strCmd)
