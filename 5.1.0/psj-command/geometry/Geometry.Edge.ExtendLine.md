---
id: Geometry-Edge-ExtendLine
title: Geometry.Edge.ExtendLine()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Extend the specified edges to the specified boundary
---

## Description

Extend the specified edges to the specified boundary.

## Syntax

```psj
Geometry.Edge.ExtendLine(...)
```

Macro: [ImprintExtendLine](../../macro/geometry/ImprintExtendLine)

Ribbon: <menuselection>Geometry &#187; Edge &#187; Extend Line</menuselection>

## Inputs

### `crlEdges`

- A _List of Cursor_ specifying the edge to be extended.
- This is a required input.

### `iMethod`

- An _Integer_ specifying the extend method.
  - If _iMethod = 0_, following the direction of the last segments of the given Edge.
  - If _iMethod = 1_, attempting to retain the curvature direction of the given Edge.
- The default value is 0.

### `iEnd`

- An _Integer_ specifying the end position to extend the edge.
  - If _iEnd=0_, extend from its endpoints to the closest edge.
  - If _iEnd=1_, extend the given edge to boundary edges.
- The default value is 0.

### `iNoFittingPoints`

- An _Integer_ specifying number of fitting points. This argument is to be used when the _iMethod=1_.
- The default value is 3.

### `iDiv`

- An _Integer_ specifying division segments. This argument is to be used when the _iMethod=1_.
- The default value is 2.

### `bBreakFace`

- An _Boolean_ specifying whether to break the face which the given edge lies on where possible.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the extended edges.?

## Sample Code

```psj {5}
Geometry.Part.Cube(iPartColor=6215639)

Geometry.Edge.ElementEdges(crplElemEdges=[CursorPair(Node(453), Node(461))])

extended_edges = Geometry.Edge.ExtendLine(crlEdges=[Edge(27)], iEnd=1)

JPT.Debugger(extended_edges)
```
