---
id: Geometry-Edge-Spline
title: Geometry.Edge.Spline()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a spline curve-shaped edge onto a face. At least three nodes on the given faces are specified to create a spline that passes through those nodes
---

## Description

Create a spline curve-shaped edge onto a face. At least three nodes on the given faces are specified to create a spline that passes through those nodes.

## Syntax

```psj
Geometry.Edge.Spline(...)
```

Macro: [GeoImprintSplineS](../../macro/geometry/GeoImprintSplineS)

Ribbon: <menuselection>Geometry &#187; Edge &#187; Spline</menuselection>

## Inputs

### `dllPoints`

- A _List of Position_ specifying the point on the given faces that the spline must pass through.
- This is a required input.

### `crlFaces`

- A _List of Cursor_ specifying the target faces on which the spline edges are imprinted.
- This is a required input.

### `bBreakFace`

- A _Boolean_ specifying whether to break the given face where possible.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5,6,7,8,9}
Geometry.Part.Cube()

created_splines = Geometry.Edge.Spline(dllPoints=[[0.01, 0.003, 0.01],
                                                  [0.007, 0.003, 0.01],
                                                  [0.005, 0.004, 0.01], 
                                                  [0.004, 0.006, 0.01], 
                                                  [0.002, 0.007, 0.01], 
                                                  [0.0, 0.003, 0.01]],
                                       crlFaces=[Face(26)])
JPT.Debugger(created_splines)
```
