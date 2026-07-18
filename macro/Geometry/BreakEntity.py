import JPT
from macro_defs import *
from macroTypes import *

def StlPart(crlParts, iMinNoOfFacet=0, iBreakMethod=0):
    strCmd = 'SeparateSTLPart({0}, {1}, {2})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        iMinNoOfFacet,
        iBreakMethod)
    return JPT.Exec(strCmd)

def Face(crlFaces):
    strCmd = 'BreakFace({0})'.format(
        str(crlFaces) if crlFaces != [None] else '[0:0]')
    return getListCursorValueByStr(JPT.Exec(strCmd))

def Edge(crlParts=[], crlFaces=[], crlEdges=[], crlNodes=[], bAutoByAngle=False, dEdgeAngle=60.0):
    bAutoByAngle_b = 1 if bAutoByAngle else 0
    dEdgeAngle = JPT.ConvertFromMacroUnit(dEdgeAngle, JPT.UnitType.Unit_Angle, "deg")
    strCmd = 'BreakEdgeCr({0}, {1}, {2}, {3}, {4}, {5})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        str(crlEdges) if crlEdges != [None] else '[0:0]',
        str(crlNodes) if crlNodes != [None] else '[0:0]',
        bAutoByAngle_b,
        dEdgeAngle)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def Part(crlParts):
    strCmd = 'SeparatePart({0})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]')
    return getListCursorValueByStr(JPT.Exec(strCmd))
