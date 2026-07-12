---
id: Geometry-LogoRemoval
title: Geometry.LogoRemoval()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Removal logos or bolts
---

## Description

This method is used to automatically remove faces that configure logos or bolts.

## Syntax

```psj
Geometry.LogoRemoval(crlStartFaces, crlStopFaces, iLayers=5, bMergeFaces=False)
```

Macro: [LogoRemoval](../../macro/geometry/LogoRemoval)

Ribbon: <menuselection>Geometry &#187; Logo Removal</menuselection>

## Inputs

### `crlStartFaces`

- A _List of Cursor_ specifying the faces of the logo or bolt to be removed.
- This is a required input.

### `crlStopFaces`

- A _List of Cursor_ specifying the faces adjacent to the geometry to be removed.
- This is a required input.

### `iLayers`

- An _Integer_ specifying the number of layers in the depth direction of the target faces when removing bolts.
- The default value is 5.

### `bMergeFaces`

- A _Boolean_ specifying whether the adjacent faces should be merged after the removal operation.
- The default value is _False_.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()

Geometry.Part.Cube(dlOrigin=[0.0045, 0.002, 0.0095], dlLength=[0.001, 0.006, 0.001])

Geometry.Part.Cube(dlOrigin=[0.003, 0.001, 0.0095], dlLength=[0.004, 0.001, 0.001])

Geometry.Part.Cube(dlOrigin=[0.003, 0.008, 0.0095], dlLength=[0.004, 0.001, 0.001])

Assemble.BooleanEx([Part(2, 3, 4)])

Geometry.MergeEntities.Faces(crlFaces=[Face(51, 52, 77, 78, 103, 104)])

Assemble.BooleanEx([Part(1, 2)], iBooleanType=1)

Geometry.LogoRemoval(crlStartFaces=[Face(51)], crlStopFaces=[Face(26)])
```
