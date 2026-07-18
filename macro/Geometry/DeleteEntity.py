import JPT
from macro_defs import *
from macroTypes import *

def Part(crlParts):
    strCmd = 'DeletePartCr({0})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]')
    return getBoolValue(JPT.Exec(strCmd))

def Edge(crlEdges):
    strCmd = 'DeleteEdgeCr({0})'.format(
        str(crlEdges) if crlEdges != [None] else '[0:0]')
    return getBoolValue(JPT.Exec(strCmd))

def Vertex(crlVertices):
    strCmd = 'DeleteVertexCr({0})'.format(
        str(crlVertices) if crlVertices != [None] else '[0:0]')
    return getBoolValueFromString(JPT.Exec(strCmd))

def Face(crlFaces, bIgnoreFaceOnSolidBody=True):
    bIgnoreFaceOnSolidBody_b = 1 if bIgnoreFaceOnSolidBody else 0
    strCmd = 'DeleteFaceCr({0}, {1})'.format(
        str(crlFaces) if crlFaces != [None] else '[0:0]',
        bIgnoreFaceOnSolidBody_b)
    return getBoolValue(JPT.Exec(strCmd))
