---
id: Geometry-BreakEntity-Edge
title: Geometry.BreakEntity.Edge()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Break an edge into separate units at the given points or specified angle
---

## Description

Break an edge into separate units at the given points or specified angle.

## Syntax

```psj
Geometry.BreakEntity.Edge(...)
```

Ribbon: <menuselection>Geometry &#187; Break Entity &#187; Edge</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying parts that the edges connecting to the faces will be divided. Either _crlParts_, _crlFaces_, or _crlEdges_ must be specified when _bAutoByAngle = True_.
- The default value is [].

### `crlFaces`

- A _List of Cursor_ specifying faces that the edges connecting to the faces will be divided. Either _crlParts_, _crlFaces_, or _crlEdges_ must be specified when _bAutoByAngle = True_.
- The default value is [].

### `crlEdges`

- A _List of Cursor_ specifying edges to be divided. Either _crlParts_, _crlFaces_, or _crlEdges_ must be specified when _bAutoByAngle = True_.
- The default value is [].

### `crlNodes`

- A _List of Cursor_ specifying the nodes at which edges pass through will be divided. This argument will be ignored if _bAutoByAngle = False_.
- The default value is [].

### `bAutoByAngle`

- A _Boolean_ specifying whether to divide by edge angle.
  - If _True_, edge will be divided at the position where its angle is not greater than the given _dEdgeAngle_.
- The default value is _False_.

### `dEdgeAngle`

- A _Double_ specifying the angle in degrees between line segments. If _bAutoByAngle_ is not specified, this argument is ignored.
- The default value is 60.0.

## Return Code

A _List of Cursor_ specifying the edges after the function is executed.

## Sample Code

```psj {3}
Geometry.Part.Cube(iPartColor=6215639)

edges = Geometry.BreakEntity.Edge(crlNodes=[Node(86, 83)])

JPT.Debugger(edges)
```
