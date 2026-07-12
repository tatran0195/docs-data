---
id: Geometry-Transform-Mirror
title: Geometry.Transform.Mirror()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Mirror body
---

## Description

This method mirrors existing part geometry across a plane to create new geometry.

## Syntax

```psj
Geometry.Transform.Mirror(crlParts, veclPoint=[[0.0, 0.0, 0.0]], dOffset=0.0, bCreateNewPart=True,
    bCopyLBC=False, bCopyProperty=False, bRemoveDupFace=True, bMergeNode=False, dTol=1e-05)
```

Macro: [MirrorBody](../../macro/geometry/MirrorBody)

Ribbon: <menuselection>Geometry &#187; Transform &#187; Mirror</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the parts to mirror.
- This is a required input.

### `veclPoint`

- A _List of Vector_ specifying the X-, Y-, and Z-coordinates of three-points to define the mirror plane.
- The default value is [[0.0, 0.0, 0.0]].

### `dOffset`

- A _Double_ specifying the offset amount from the mirror plane.
- The default value is 0.0.

### `bCreateNewPart`

- A _Boolean_ specifying whether or not the mirrored part should be moved to a new part and keep the original part as is.
- The default value is _True_.

### `bCopyLBC`

- A _Boolean_ specifying whether to copy all load boundary condition from original part to mirrored part. This argument will be ignored if _bCreateNewPart=False_.
- The default value is _False_.

### `bCopyProperty`

- A _Boolean_ specifying whether to copy all property from original part to mirrored part. This argument will be ignored if _bCreateNewPart=False_.
- The default value is _False_.

### `bRemoveDupFace`

- A _Boolean_ specifying whether to remove the faces which overlap the mirrored with the original part. This argument will be ignored if _bCreateNewPart=False_.
- The default value is _True_.

### `bMergeNode`

- A _Boolean_ specifying whether to merge nodes of mirrored part and the original part are at a distance of less than or equal to the specified value.
- The default value is _False_.

### `dTol`

- A _Double_ specifying the maximum distance of the coupling nodes. This argument will be ignored if _bMergeNode=False_.
- The default value is 1e-05.

### `bCopyReference`

- A _Boolean_ specifying whether to copy references from the existing part to the created parts or not.
- The default value is _False_.
  
## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Wedge()

Geometry.Transform.Mirror(crlParts=[Part(1)], veclPoint=[[0.012, 0, 0], [0, 0.012, 0], [0.012, 0, 1]])
```
