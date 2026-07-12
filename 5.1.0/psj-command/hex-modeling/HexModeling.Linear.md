---
id: HexModeling-Linear
title: HexModeling.Linear()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) in a specified direction.
---

## Description

Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) in a specified direction.

## Syntax

```psj
HexModeling.Linear(...)
```

Ribbon: <menuselection>HexModeling &#187; Linear</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the face.
- The default value is [].

### `dLength`

- A _Double_ specifying the length.
- The default value is 10.

### `iLayer`

- An _Integer_ specifying the layer.
- The default value is 10.

### `vecSweepDirection`

- A _Vector_ specifying the sweep direction.
- The default value is [].

### `bInterfaceElemFlag`

- A _Boolean_ specifying the interface element flag.
- The default value is False.

### `iLinearMethod`

- An _Integer_ specifying the linear method.
- The default value is 0.

### `bDeleteOriginalParts`

- A _Boolean_ specifying the delete original parts.
- The default value is False.

### `bDeleteTargetParts`

- A _Boolean_ specifying the delete target parts.
- The default value is False.

### `iMethodBias`

- An _Integer_ specifying the method bias.
- The default value is 0.

### `dFactor`

- A _Double_ specifying the factor.
- The default value is 2.0.

### `iProgression`

- An _Integer_ specifying the progression.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {8}
Geometry.Part.Cube()
Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE_MESH(dAvgElemSize=0.002, dGeomAngle=0.7853981634, 
        iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, bGeomApprox=True, iNextEntityOffsetId=0))
Geometry.DeleteEntity.Face(crlFaces=[Face(24, 22, 25, 23, 21)])
HexModeling.Linear(crlFaces=[Face(26)], dLength=0.01, vecSweepDirection=[0.0, 0.0, 1.0])
```
