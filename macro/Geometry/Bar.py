import JPT
from macro_defs import *
from macroTypes import *

def TwoNodes(crStartNode, crEndNode, strName="Bar_1", iMeshOption=0, iMeshCount=5, dMeshSize=0.0):
    strCmd = 'CreateBar({0}, {1}, {2}, {3}, {4}, {5})'.format(
        '"' + strName + '"',
        iMeshOption,
        iMeshCount,
        dMeshSize,
        str(crStartNode) if crStartNode is not None else '0:0',
        str(crEndNode) if crEndNode is not None else '0:0')
    return getCursorValueByStr(JPT.Exec(strCmd))

def Arc(crlNodes, crPart=None, strName="Bar_1"):
    strCmd = 'CreateBarArc({0}, {1}, {2})'.format(
        str(crlNodes) if crlNodes != [None] else '[0:0]',
        str(crPart) if crPart is not None else '0:0',
        '"' + strName + '"')
    return getCursorValueByStr(JPT.Exec(strCmd))

def Spline(crlNodes, crPart=None, strName="Bar_1"):
    strCmd = 'CreateBarSpline({0}, {1}, {2})'.format(
        str(crlNodes) if crlNodes != [None] else '[0:0]',
        str(crPart) if crPart is not None else '0:0',
        '"' + strName + '"')
    return getCursorValueByStr(JPT.Exec(strCmd))
