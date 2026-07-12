---
id: HexModeling-Curve
title: HexModeling.Curve()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) along a specified curve.
---

## Description

Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) along a specified curve.

## Syntax

```psj
HexModeling.Curve(...)
```

Ribbon: <menuselection>HexModeling &#187; Curve</menuselection>

## Inputs

### `crFace`

- A _Cursor_ specifying the face.
- The default value is None.

### `crlEdges`

- A _List of Cursor_ specifying the edge.
- The default value is [].

### `crlRefEdge`

- A _List of Cursor_ specifying the reference edge.
- The default value is [].

### `dMeshSize`

- A _Double_ specifying the mesh size.
- The default value is 0.1.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {28}
Geometry.Part.Cube()
Geometry.Bar.Spline(crlNodes=[Node(1, 8, 7)], strName="Bar_2")
Geometry.Part.Cylinder(dTopOuterRadius=0.001, dBottomOuterRadius=0.001, iPartColor=6409934)

Geometry.DeleteEntity.Face(crlFaces=[Face(32, 34)])
Geometry.DeleteEntity.Part(crlParts=[Part(1)])

Meshing.SetMeshAttribute(crlParts=[Part(3)], 
    surfaceMesh=SURFACE_MESH(
        dAvgElemSize=0.002, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, bGeomApprox=True, 
        iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(
    crlParts=[Part(3)], 
    surfaceMesh=SURFACE_MESH(
        dAvgElemSize=0.002, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, 
        bGeomApprox=True, 
        iNextEntityOffsetId=0))

HexModeling.Curve(crFace=Face(33), crlEdges=[Edge(27)], dMeshSize=0.002)
```
