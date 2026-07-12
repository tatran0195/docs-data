---
id: Geometry-Edge-PerpendicularLineToEdge
title: Geometry.Edge.PerpendicularLineToEdge()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create an edge perpendicular to the selected edges through a specified point on the selected faces
---

## Description

Create an edge perpendicular to the selected edges through a specified point on the selected faces. The created edges can be started from the specified point or extend to the closest edge.

## Syntax

```psj
Geometry.Edge.PerpendicularLineToEdge(...)
```

Ribbon: <menuselection>Geometry &#187; Edge &#187; Perpendicular Line To Edge</menuselection>

## Inputs

### `crNode`

- A _Cursor_ specifying the start node of new edge. If _bAuto_ or scale is specified, this argument is ignored.
- The default value is _None_.

### `crEdge`

- A _Cursor_ specifying the edge that the new edge should be extended up to. If _bAuto_ or scale is specified, this argument is ignored.
- The default value is _None_.

### `crlFaces`

- A _List of Cursor_ specifying the target faces on which the edges are imprinted.
- This is a required input.

### `bBreakFace`

- A _Boolean_ specifying whether to break the given faces where possible.
- The default value is _True_.

### `bExtend`

- A _Boolean_ specifying whether to extend the new edge through the given node up to the closest edge object.
- The default value is _True_.

### `bAuto`

- A _Boolean_ specifying whether to specify the node and edge automatically from the pair of edges where the angle between them is equal or greater than the angle _dLimitAngle_ specified. The node in-between will be selected automatically, an imprinting line will be made from that node to the opposite edge of the given faces.
- The default value is _False_.

### `dLimitAngle`

- A _Double_ specifying the angle in degrees to limit the angle within which Edge entities should be considered. This argument is to be used when the _bAuto_ is _True_.
- The default value is 135.0.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cylinder()

created_edges = Geometry.Edge.PerpendicularLineToEdge(crNode=Node(250), 
                                                      crEdge=Edge(1), 
                                                      crlFaces=[Face(5)])
JPT.Debugger(created_edges)
```
