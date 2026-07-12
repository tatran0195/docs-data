---
id: Geometry-Transform-CylinderFace
title: Geometry.Transform.CylinderFace()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Transform to matching two cylindrical surfaces
---

## Description

Translate two parts such that the specified two cylindrical surfaces concentric.

## Syntax

```psj
Geometry.Transform.CylinderFace(...)
```

Ribbon: <menuselection>Geometry &#187; Transform &#187; Cylinder Face</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the cylinder part.
- This is a required input.

### `veclPoint`

- A _List of Vector_ specifying the points to define the matching plane from source and target.
  It contains the position of six points, the first three points define the source face, the others define the target face.
- The default value is [[0.0, 0.0, 0.0]].

### `bCreateNewPart`

- A _Boolean_ specifying whether to keep the original part and create a new part after the transform operation.
- The default value is _False_.

### `bCopyLBC`

- A _Boolean_ specifying whether to copy load boundary condition from original part to transformed one.
  This argument will be ignored if _bCreateNewPart=False_.
- The default value is _False_.

### `bCopyProperty`

- A _Boolean_ specifying whether to copy property from original part to transformed one.
  This argument will be ignored if _bCreateNewPart=False_.
- The default value is _False_.

## Return Code

No return value.

## Sample Code

```psj {3}
Geometry.Part.Cylinder()
Geometry.Part.Cylinder(dlOrigin=[0.02, 0.0, 0.0], strName="Cylinder_2", iPartColor=6812659)
Geometry.Transform.CylinderFace(crlParts=[Part(1), Part(2)], veclPoint=[[0, 0, 0], [0, -1000, 0],
    [10, 0, 0], [0, 10, 0], [0, -990, 0], [10.0, 10, 10]], bCreateNewPart=True)
```
