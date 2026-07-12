---
id: Geometry-MergeEntities-PartFaces
title: Geometry.MergeEntities.PartFaces()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Merge Faces in Part
---

## Description

This method merges adjacent faces of the given part by recursively finding adjacent faces that are at an angle of less than or equal to the specified angle or face width is not greater than the specified value. The operation will ignore the specified preserved faces.

## Syntax

```psj
Geometry.MergeEntities.PartFaces(crlParts=[], crlFaces=[], bAngle=True, dTolAngle=20, bWidth=True,
    dTolWidth=0.2)
```

Ribbon: <menuselection>Geometry &#187; Merge Entities &#187; Part Faces</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the target parts that faces need merging belong to.
- The default value is [].

### `crlFaces`

- A _List of Cursor_ specifying the preserved faces not to be merged.
- The default value is [].

### `bAngle`

- A _Boolean_ specifying whether to find the adjacent faces by face angle.
- The default value is _True_.

### `dTolAngle`

- A _Double_ specifying the maximum allowable angle between two adjacent faces. If _bAngle_ is specified, the adjacent faces that are at an angle of less than or equal to will be merged.
- The default value is 20.0.

### `bWidth`

- A _Boolean_ specifying whether to find the adjacent faces by face width.
- The default value is _True_.

### `dTolWidth`

- A _Double_ specifying the maximum allowable face width. If _bWidth_ is specified, the faces that have a width less than or equal to will be merged to an adjacent face.
- The default value is 0.2.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Trapezoid(dTopXLength=5.0)

Geometry.MergeEntities.PartFaces(crlParts=[Part(1)], dTolAngle=89.0, bWidth=False)
```
