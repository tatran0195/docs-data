---
id: Geometry-Edge-PlanarLine
title: Geometry.Edge.PlanarLine()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create edges at the intersection of the given faces and a planar face defining by 3 points or axis plane
---

## Description

Create edges at the intersection of the given faces and a planar face defining by 3 points or axis plane.

## Syntax

```psj
Geometry.Edge.PlanarLine(...)
```

Macro: [ImprintPlannarLineS](../../macro/geometry/ImprintPlannarLineS)

Ribbon: <menuselection>Geometry &#187; Edge &#187; Planar Line</menuselection>

## Inputs

### `dllPoints`

- A _List of Position_ specifying the points which to define the planar face or the specific point that line passes through. Each point can be a Node, point on edge, or point on face. A valid value may one or three points on the list.
- This is a required input.

### `crlFaces`

- A _List of Cursor_ specifying the target faces on which the edges are imprinted.
- This is a required input.

### `crLocalCoordinate`

- A _Cursor_ specifying the local coordinate.
- The default value is _None_.

### `iAxisPlane`

- An _Integer_ specifying the reference axis plane. Possible values are 0, 1, 2 corresponding to XY, XZ, and YZ Plane. This option will only affect the functionality when there is a point in _dllPoints_ only.
- The default value is 0.

### `bBreakFace`

- A _Boolean_ specifying whether to break the given faces where possible.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube()

edges = Geometry.Edge.PlanarLine(dllPoints=[[0.01, 0.005, 0.006]], 
                                 crlFaces=[Face(24, 26)], 
                                 iAxisPlane=1)

JPT.Debugger(edges)
```
