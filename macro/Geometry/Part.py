import JPT
from macro_defs import *
from macroTypes import *

def Cube(dlOrigin=[0.0, 0.0, 0.0], dlLength=[0.01, 0.01, 0.01], ilAxialNodes=[10, 10, 10], strName="Cube_1", iPartColor=7105764, crLocalCoordinate=None):
    strCmd = 'CreateCube({0}, {1}, {2}, {3}, {4}, {5})'.format(
        dlOrigin,
        dlLength,
        ilAxialNodes,
        '"' + strName + '"',
        iPartColor,
        str(crLocalCoordinate) if crLocalCoordinate is not None else '0:0')
    return getCursorValueByStr(JPT.Exec(strCmd))

def Wedge(dlOrigin=[0.0, 0.0, 0.0], dlLength=[0.01, 0.01, 0.01], ilAxialNodes=[10, 10, 10], strName="Wedge_1", iPartColor=7105764, crLocalCoordinate=None):
    strCmd = 'CreateWedge({0}, {1}, {2}, {3}, {4}, {5})'.format(
        dlOrigin,
        dlLength,
        ilAxialNodes,
        '"' + strName + '"',
        iPartColor,
        str(crLocalCoordinate) if crLocalCoordinate is not None else '0:0')
    return getCursorValueByStr(JPT.Exec(strCmd))

def Sphere(dlOrigin=[0.0, 0.0, 0.0], dRadius=0.005, iLatitudeDivisions=20, iLongitudeDivisions=20, strName="Sphere_1", iPartColor=7105764, crLocalCoordinate=None):
    strCmd = 'CreateSphere({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(
        dlOrigin,
        dRadius,
        iLatitudeDivisions,
        iLongitudeDivisions,
        '"' + strName + '"',
        iPartColor,
        str(crLocalCoordinate) if crLocalCoordinate is not None else '0:0')
    return getCursorValueByStr(JPT.Exec(strCmd))

def Torus(dlOrigin=[0.0, 0.0, 0.0], dInnerRadius=0.015, dRingRadius=0.02, iCircumNodes=20, iRingNodes=20, strName="Torus_1", iPartColor=7105764, crLocalCoordinate=None):
    strCmd = 'CreateTorus({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})'.format(
        dlOrigin,
        dInnerRadius,
        dRingRadius,
        iCircumNodes,
        iRingNodes,
        '"' + strName + '"',
        iPartColor,
        str(crLocalCoordinate) if crLocalCoordinate is not None else '0:0')
    return getCursorValueByStr(JPT.Exec(strCmd))

def Elems(crlElems, strPartName):
    strCmd = 'CreatePartFromElems({0}, {1})'.format(
        str(crlElems) if crlElems != [None] else '[0:0]',
        '"' + strPartName + '"')
    return JPT.Exec(strCmd)

def Cylinder(strName="Cylinder_1", crLocalCoordinate=None, bHollow=False, bTapered=False, dlOrigin=[0.0,0.0,0.0], dTopInnerRadius=0.001, dTopOuterRadius=0.01, dBottomInnerRadius=0.001, dBottomOuterRadius=0.01, dHeight=0.01, iCircularNodes=36, iAxialNodes=10, iPartColor=7105764):
    bHollow_b = 1 if bHollow else 0
    bTapered_b = 1 if bTapered else 0
    strCmd = 'CreateCylinderPart({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12})'.format(
        '"' + strName + '"',
        str(crLocalCoordinate) if crLocalCoordinate is not None else '0:0',
        bHollow_b,
        bTapered_b,
        dlOrigin,
        dTopInnerRadius,
        dTopOuterRadius,
        dBottomInnerRadius,
        dBottomOuterRadius,
        dHeight,
        iCircularNodes,
        iAxialNodes,
        iPartColor)
    return getCursorValueByStr(JPT.Exec(strCmd))

def Tube(strName="Tube_1", bTri=True, crlEdges=[], dRadius=0.01, dMeshSizeAxis=0.005, dWMeshSizeCirc=0.001, iNumCirc=36, iPartColor=7105764):
    bTri_b = 1 if bTri else 0
    strCmd = 'CreateTube({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})'.format(
        '"' + strName + '"',
        bTri_b,
        str(crlEdges) if crlEdges != [None] else '[0:0]',
        dRadius,
        dMeshSizeAxis,
        dWMeshSizeCirc,
        iNumCirc,
        iPartColor)
    return getListCursorValueByStr(JPT.Exec(strCmd))

def Trapezoid(dlOrigin=[0.0,0.0,0.0], dlLength=[0.01, 0.01, 0.01], dTopXLength=7.0, dRadius=0.0, ilAxialNodes=[10, 10, 10], strName="Trapezoid_1", iPartColor=7105764, crLocalCoordinate=None):
    dTopXLength = JPT.ConvertFromMacroUnit(dTopXLength, JPT.UnitType.Unit_Length, "mm")
    strCmd = 'CreateTrapezoid({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})'.format(
        dlOrigin,
        dlLength,
        dTopXLength,
        dRadius,
        ilAxialNodes,
        '"' + strName + '"',
        iPartColor,
        str(crLocalCoordinate) if crLocalCoordinate is not None else '0:0')
    return getCursorValueByStr(JPT.Exec(strCmd))

def Cone(dlOrigin=[0.0,0.0,0.0], dBottomRadius=0.01, dHeight=0.02, iCircularNodes=20, iAxialNodes=20, strName="Cone_1", iPartColor=7105764, crLocalCoordinate=None):
    strCmd = 'CreateCone({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})'.format(
        dlOrigin,
        dBottomRadius,
        dHeight,
        iCircularNodes,
        iAxialNodes,
        '"' + strName + '"',
        iPartColor,
        str(crLocalCoordinate) if crLocalCoordinate is not None else '0:0')
    return getCursorValueByStr(JPT.Exec(strCmd))

def Frustum(dlOrigin=[0.0,0.0,0.0], dTopRadius=0.003, dBottomRadius=0.01, dHeight=0.02, iCircularNodes=20, iAxialNodes=20, strName="Frustum_1", iPartColor=7105764, crLocalCoordinate=None):
    strCmd = 'CreateCylinderFrustum({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})'.format(
        dlOrigin,
        dTopRadius,
        dBottomRadius,
        dHeight,
        iCircularNodes,
        iAxialNodes,
        '"' + strName + '"',
        iPartColor,
        str(crLocalCoordinate) if crLocalCoordinate is not None else '0:0')
    return getCursorValueByStr(JPT.Exec(strCmd))