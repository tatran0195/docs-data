---
id: Geometry-FindFeature-Face
title: Geometry.FindFeature.Face()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Find and select the specific faces according to their characteristic
---

## Description

Find and select the specific faces according to their characteristic.

## Syntax

```psj
Geometry.FindFeature.Face(...)
```

Ribbon: <menuselection>Geometry &#187; FindFeature &#187; Faces</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the parts to find the specific faces.
- This is a required input.

### `iFaceType`

- An _Integer_ specifying the specific type of Faces.
  - If _iFaceType=0_, find and select the faces that are bounded by four corners.
  - If _iFaceType=1_, find and select the planar faces.
  - If _iFaceType=2_, find and select the faces of the cylindrical surface.
  - If _iFaceType=3_, find and select the faces of the semi-cylindrical surface.
  - If _iFaceType=4_, find and select the disk-shaped faces.
  - If _iFaceType=5_, find and select the faces of map mesh.
  - If _iFaceType=6_, find and select the circular chamfer faces.
  - If _iFaceType=7_, find and select the fillet faces.
- The default value is 0.

### `bCylinder`

- A _Boolean_ specifying whether to find cylinder face of map mesh. This argument is to be used if _iOption=5_.
- The default value is _True_.

### `bDisc`

- A _Boolean_ specifying whether to find disk-shaped face of map mesh. This argument is to be used if _iOption=5_.
- The default value is _False_.

### `bFourCorners`

- A _Boolean_ specifying whether to find the faces that are bounded by four corners of map mesh. This argument is to be used if _iFaceType=5_.
- The default value is _True_.

### `dMinThickness`

- A _Double_ specifying the minimum thickness of the circular chamfer surface. This argument is to be used if _iFaceType=6_.
- The default value is 0.1.

### `dMaxThickness`

- A _Double_ specifying the maximum thickness of the circular chamfer surface. This argument is to be used if _iFaceType=6_.
- The default value is 2.0.

## Return Code

A _List cursor_ of faces if success, or _None_ if fail.

## Sample Code

```psj {2}
cube = Geometry.Part.Cube()
faces = Geometry.FindFeature.Face(crlParts=[cube])
JPT.Debugger(faces)
```
