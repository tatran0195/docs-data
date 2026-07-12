---
id: Geometry-ExtractSurfaces
title: Geometry.ExtractSurfaces()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a new part by recursively finding adjacent surfaces are at an angle of less than or equal to the specified angle
---

## Description

Create a new part by recursively finding adjacent surfaces are at an angle of less than or equal to the specified angle.

## Syntax

```psj
Geometry.ExtractSurfaces(...)
```

Ribbon: <menuselection>Geometry &#187; Extract Surfaces</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the starting faces using for the extracting process.
- This is a required input.

### `dFaceAngle`

- A _Double_ specifying the limit angle used for spreading from the selected faces to the adjacent faces in degree.
- If _dFaceAngle=-1_, only the selected faces will be extracted.
- The default value is 60.0.

### `strName`

- A _String_ specifying the name of the part(s) which will be created after executing the function.
- The default value is "ExtractFace_1".

### `bMergePart`

- A _Boolean_ specifying whether to merge the created parts into a single part or not.
- The default value is _False_.

## Return Code

A _List of Cursor_ specifying the created parts.

## Sample Code

```psj {5,6,7,8}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0],
                   strName="Cube_2",
                   iPartColor=6409934)
bodies = Geometry.ExtractSurfaces([Face(52, 26)],
                                  dFaceAngle=-1.0,
                                  strName="ExtractFace_4",
                                  bMergePart=True)
JPT.Debugger(bodies)
```
