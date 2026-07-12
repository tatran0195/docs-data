---
id: HexModeling-SolidElemInterface
title: HexModeling.SolidElemInterface()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: make solid element interface
---

## Description

Make solid element interface

## Syntax

```psj
HexModeling.SolidElemInterface(...)
```

Ribbon: <menuselection>HexModeling &#187; SolidElemInterface</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the face.
- The default value is [].

### `bFlip`

- A _Boolean_ specifying the flip.
- The default value is False.

### `crlElms`

- A _List of Cursor_ specifying the elms.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {9}
Geometry.Part.Cube()
Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE_MESH(dAvgElemSize=0.002, dGeomAngle=0.7853981634, 
        iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, bGeomApprox=True, iNextEntityOffsetId=0))
Geometry.DeleteEntity.Face(crlFaces=[Face(24, 22, 25, 23, 21)])
HexModeling.Linear(crlFaces=[Face(26)], dLength=0.01, iLayer=5, vecSweepDirection=[0.0, 0.0, 1.0])
HexModeling.SolidElemInterface(crlFaces=[Face(26)])
```
