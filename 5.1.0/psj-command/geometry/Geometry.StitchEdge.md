---
id: Geometry-StitchEdge
title: Geometry.StitchEdge()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Stitch Edges
---

## Description

This method stitches any gap between free edges that are slightly apart.

## Syntax

```psj
Geometry.StitchEdge(crlMaster, crlSlave, dTolerance=0.3, bKeepSlave=True)
```

Macro: [StitchEdge](../../macro/geometry/StitchEdge)

Ribbon: <menuselection>Geometry &#187; Stitch Edge</menuselection>

## Inputs

### `crlMaster`

- A _List of Cursor_ specifying master edges will be retained after operation.
- This is a required input.

### `crlSlave`

- A _List of Cursor_ specifying slave edges to be stitched.
- This is a required input.

### `dTolerance`

- A _Double_ specifying the stitch tolerance. The free edges are at a distance less than or equal to the specified value will be stitched.
- The default value is 0.3.

### `bKeepSlave`

- A _Boolean_ specifying whether to keep slave nodes after the stitch operation.
- The default value is _True_.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()

Geometry.Part.Cube(dlOrigin=[0.01, 0.01, 0.0], ilNodeCnt=[10, 10, 11], strName="Cube_2")

Geometry.StitchEdge(crlMaster=[Edge(15)], crlSlave=[Edge(39))
```
