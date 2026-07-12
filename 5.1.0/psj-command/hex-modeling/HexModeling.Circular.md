---
id: HexModeling-Circular
title: HexModeling.Circular()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: A hexahedral mesh model is generated from a hollow axisymmetric model.
---

## Description

A hexahedral mesh model is generated from a hollow axisymmetric model.

## Syntax

```psj
HexModeling.Circular(...)
```

Ribbon: <menuselection>HexModeling &#187; Circular</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the face.
- The default value is [].

### `dAngle`

- A _Double_ specifying the angle.
- The default value is 360.

### `dTol`

- A _Double_ specifying the tolerance.
- The default value is 0.0000001.

### `iLayer`

- An _Integer_ specifying the layer.
- The default value is 36.

### `vecAxisPt`

- A _Vector_ specifying the axis point.
- The default value is [0.0,0.0,0.0].

### `vecAxisVect`

- A _Vector_ specifying the axis vector.
- The default value is [1.0,0.0,0.0].

### `bInterfaceElem`

- A _Boolean_ specifying the interface element.
- The default value is False.

### `bExtrusion`

- A _Boolean_ specifying the extrusion.
- The default value is False.

### `dTranslationExtrusion`

- A _Double_ specifying the translation extrusion.
- The default value is 0.0.

### `dBDeleteOriginalParts`

- A _Double_ specifying the delete original parts.
- The default value is 0.0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {26}
Geometry.Part.Cylinder(bHollow=True, dTopInnerRadius=0.003, dBottomInnerRadius=0.003, iCircularNodes=128)
Geometry.BodyCut.XXYYOnOnePoint(crPart=Part(1), posCutPoint=[0, 0.01, 0.01], iCuttingPlane=2)
Geometry.BodyCut.XXYYOnOnePoint(crPart=Part(1), posCutPoint=[-0.01, 0.01, 0])
Geometry.DeleteEntity.Part(crlParts=[Part(3, 5)])

Meshing.SetMeshAttribute(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE_MESH(dAvgElemSize=0.002,
        dGeomAngle=0.7853981634, iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, 
        bGeomApprox=True, 
        iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE_MESH(
        dAvgElemSize=0.002, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1,
         dAutoMergeTinyFacesAngle=0.5235987756, 
         bOutputQuadMesh=True, 
         bGeomApprox=True, 
         iNextEntityOffsetId=0))

HexModeling.Circular(crlFaces=[58], dAngle=90.0, iLayer=6, vecAxisVect=[0.0, -1.0, 0.0], dBDeleteOriginalParts=1.0)
```
