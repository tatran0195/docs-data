---
id: Geometry-Edge-Line
title: Geometry.Edge.Line()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create edges based on the selected nodes
---

## Description

Create edges based on the selected nodes.

## Syntax

```psj
Geometry.Edge.Line(...)
```

Macro: [ImprintLineS](../../macro/geometry/ImprintLineS)

Ribbon: <menuselection>Geometry &#187; Edge &#187; Line</menuselection>

## Inputs

### `dllPoints`

- A _List of Position_ specifying points on the target faces.
- This is a required input.

### `crlFaces`

- A _List of Cursor_ specifying the target faces on which the edges are imprinted.
- This is a required input.

### `bBreakFace`

- A _Boolean_ specifying whether to break the given faces where possible.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4}
Geometry.Part.Cube(iPartColor=6215639)

lines = Geometry.Edge.Line(dllPoints=[[0.01, 0, 0.01], [0, 0.01, 0.01]], 
                            crlFaces=[Face(26)])

JPT.Debugger(lines)
```
