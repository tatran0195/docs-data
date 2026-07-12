---
id: Geometry-ExtractRefSurface
title: Geometry.ExtractRefSurface()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a new part by recursively finding adjacent surfaces that are at an angle of less than or equal to the specified angle
---

## Description

Create a new part by recursively finding adjacent surfaces that are at an angle of less than or equal to the specified angle.

## Syntax

```psj
Geometry.ExtractRefSurface(...)
```

Ribbon: <menuselection>Geometry &#187; Extract Surfaces</menuselection>

## Inputs

### `crlRefFaces`

- A _List of Cursor_ specifying the faces to be extracted.
- This is a required input.

### `dFaceAngle`

- A _Double_ specifying the angle in degrees between the adjacent faces to be extracted. If _dFaceAngle=-1_, the selected faces are extracted only.
- The default value is 60.0.

### `strName`

- A _String_ specifying the original name of new parts. The final name is a concatenation of the original name and sequence number.
- The default value is "ExtractFace_1".

### `bMergePart`

- A _Boolean_ specifying whether to merge new parts into a single part.
- The default value is _False_.

## Return Code

A _List of Cursor_ specifying the created parts, or _None_ if fail.

## Sample Code

```psj {13,14,15,16,17}
cube1 = Geometry.Part.Cube()

cube2 = Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0], 
                           strName="Cube_2", 
                           iPartColor=6409934)

Assembly.RightClick.AddToReference(crSrcPart=cube1, 
                                   crDestPart=cube1)

Assembly.RightClick.AddToReference(crSrcPart=cube2, 
                                   crDestPart=cube2)

created_part = Geometry.ExtractRefSurfaces(crlRefFaces=[RefFace((52, 
                                                                 26))], 
                                           dFaceAngle=-1.0, 
                                           strName="ExtractFace_3",
                                           bIsMergePart=True)

JPT.Debugger(created_part)
```
