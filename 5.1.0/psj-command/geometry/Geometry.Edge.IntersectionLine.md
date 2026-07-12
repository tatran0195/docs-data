---
id: Geometry-Edge-IntersectionLine
title: Geometry.Edge.IntersectionLine()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create edge at the intersection line of the two selected faces
---

## Description

Create edge at the intersection line of the two selected faces.

## Syntax

```psj
Geometry.Edge.IntersectionLine(...)
```

Ribbon: <menuselection>Geometry &#187; Edge &#187; Intersection Line</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the intersection faces.
- The default value is [].

### `bBreakFace`

- A _Boolean_ specifying whether to break the given faces where possible.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {6}
Geometry.Part.Cube()
Geometry.Face.Edges(crlEdges=[Edge(20, 10)], bCreatePart=True)
Geometry.Face.Edges(crlEdges=[Edge(18, 12)], bCreatePart=True)
Geometry.DeleteEntity.Part(crlParts=[Part(1)])

intersection_line = Geometry.Edge.IntersectionLine(crlFaces=[Face(27), Face(30)], bBreakFace=True)
JPT.Debugger(intersection_line)
```
