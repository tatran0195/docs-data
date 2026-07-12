---
id: Geometry-Edge-ClosedLine
title: Geometry.Edge.ClosedLine()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Imprint closed lines onto face
---

## Description

This method imprints closed lines onto the given face.

## Syntax

```psj
Geometry.Edge.ClosedLine(...)
```

Macro: [ImprintCloseLineS](../../macro/geometry/ImprintCloseLineS)

Ribbon: <menuselection>Geometry &#187; Edge &#187; Closed Line</menuselection>

## Inputs

### `veclPositions`

- A _List of Position_ specifying points on the target faces.
- This is a required input.

### `crlTargetFace`

- A _List of Cursor_ specifying the target faces on which the edges are imprinted.
- This is a required input.

### `bBreakFace`

- A _Boolean_ specifying whether to break the given faces where possible.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3-7}
Geometry.Part.Cube()

closed_lines = Geometry.Edge.ClosedLine(veclPositions=[[0.0058, 0.0028, 0.01], 
                                        [0.0038, 0.0029, 0.01], 
                                        [0.0040, 0.0047, 0.01], 
                                        [0.0063, 0.0046, 0.01]],
                                         crlTargetsFace=[Face(26)])
JPT.Debugger(closed_lines)
```
