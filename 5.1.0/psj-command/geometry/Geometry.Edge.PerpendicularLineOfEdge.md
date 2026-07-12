---
id: Geometry-Edge-PerpendicularLineOfEdge
title: Geometry.Edge.PerpendicularLineOfEdge()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create an edge perpendicular to the line defined by two nodes in the selected faces
---

## Description

Create a perpendicular edge to the line defined by two nodes in the selected facs.

## Syntax

```psj
Geometry.Edge.PerpendicularLineOfEdge(...)
```

Macro: [ImprintPerpendicularLine](../../macro/geometry/ImprintPerpendicularLine)

Ribbon: <menuselection>Geometry &#187; Edge &#187; Perpendicular Line Of Edge</menuselection>

## Inputs

### `crlNodes`

- A _List of Cursor_ specifying 2 nodes in order from the screen to determine the direction. The first node is the origin of the offset amount. The imprint line is defined perpendicular to this direction.
- This is a required input.

### `crlFaces`

- A _List of Cursor_ specifying the target faces on which the edges are imprinted.
- This is a required input.

### `dOffsetDistance`

- A _Double_ specifying the offset distance.
- The default value is 0.

### `bBreakFace`

- A _Boolean_ specifying whether to break the given faces where possible.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the new created edge.

## Sample Code

```psj {3,4,5,6,7,8,9}
Geometry.Part.Cube(iPartColor=6215639)

created_edges = Geometry.Edge.PerpendicularLineOfEdge(crlNodes=[Node(344, 339)], 
                                                     crlFaces=[Face(24, 
                                                                    22, 
                                                                    26, 
                                                                    25, 
                                                                    21, 
                                                                    23)])
JPT.Debugger(created_edges)
```
