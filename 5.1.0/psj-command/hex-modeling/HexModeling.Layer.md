---
id: HexModeling-Layer
title: HexModeling.Layer()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) in the normal direction.
---

## Description

Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) in the normal direction.

## Syntax

```psj
HexModeling.Layer(...)
```

Ribbon: <menuselection>HexModeling &#187; Layer</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the face.
- The default value is [].

### `dFrontWidth`

- A _Double_ specifying the front width.
- The default value is 0.0.

### `dBackWidth`

- A _Double_ specifying the back width.
- The default value is 0.0.

### `iFrontLayers`

- An _Integer_ specifying the front layers.
- The default value is 1.

### `iBackLayers`

- An _Integer_ specifying the back layers.
- The default value is 0.

### `iBaseFaceType`

- An _Integer_ specifying the base face type.
- The default value is 0.

### `iSeparate`

- An _Integer_ specifying the separate.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {8-9}
Geometry.Part.Cube()
Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE_MESH(dAvgElemSize=0.002, dGeomAngle=0.7853981634, 
        iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, bGeomApprox=True, iNextEntityOffsetId=0))
Geometry.DeleteEntity.Face(crlFaces=[Face(24, 22, 25, 23, 21)])
HexModeling.Layer(crlFaces=[26], dFrontWidth=0.001, dBackWidth=0.0015, iFrontLayers=3, 
                iBackLayers=2, iBaseFaceType=1)
```
