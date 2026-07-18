import JPT
from macro_defs import *
from macroTypes import *

def XXYYOnOnePoint(crPart, posCutPoint=[0.0,0.0,0.0], iCuttingPlane=0, dOffsetDistance=0.0, bSplitOnly=False, bMakeSectionFace=True, bSharedFace=False, crLocalCoordinate=None, bSeparateFace=False):
    bSplitOnly_b = 1 if bSplitOnly else 0
    bMakeSectionFace_b = 1 if bMakeSectionFace else 0
    bSharedFace_b = 1 if bSharedFace else 0
    bSeparateFace_b = 1 if bSeparateFace else 0
    strCmd = 'CutBodyByPlane({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})'.format(
        str(crPart) if crPart is not None else '0:0',
        posCutPoint,
        iCuttingPlane,
        dOffsetDistance,
        bSplitOnly_b,
        bMakeSectionFace_b,
        bSharedFace_b,
        str(crLocalCoordinate) if crLocalCoordinate is not None else '0:0',
        bSeparateFace_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def BySurface(crlParts, crCutter, bSplitOnly=False, bMakeSectionFace=True, bSharedFace=False, bSeparateFace=False):
    bSplitOnly_b = 1 if bSplitOnly else 0
    bMakeSectionFace_b = 1 if bMakeSectionFace else 0
    bSharedFace_b = 1 if bSharedFace else 0
    bSeparateFace_b = 1 if bSeparateFace else 0
    strCmd = 'BodyCutBySurfaceS({0}, {1}, {2}, {3}, {4}, {5})'.format(
        str(crlParts) if crlParts != [None] else '[0:0]',
        str(crCutter) if crCutter is not None else '0:0',
        bSplitOnly_b,
        bMakeSectionFace_b,
        bSharedFace_b,
        bSeparateFace_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def By3Points(crPart, poslPoints=[[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]], dOffsetDistance=0.0, bSplitOnly=False, bMakeSectionFace=True, bSharedFace=False, bSeparateFace=False):
    bSplitOnly_b = 1 if bSplitOnly else 0
    bMakeSectionFace_b = 1 if bMakeSectionFace else 0
    bSharedFace_b = 1 if bSharedFace else 0
    bSeparateFace_b = 1 if bSeparateFace else 0
    strCmd = 'BodyCutBy3PointsS({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(
        str(crPart) if crPart is not None else '0:0',
        poslPoints,
        dOffsetDistance,
        bSplitOnly_b,
        bMakeSectionFace_b,
        bSharedFace_b,
        bSeparateFace_b)
    return getListCursorValueByStr(JPT.Exec(strCmd))
