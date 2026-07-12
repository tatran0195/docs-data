---
id: Geometry-Edge-Circle
title: Geometry.Edge.Circle()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Imprint circular edges onto the specified face
---

## Description

Imprint circular edges onto the specified face.

## Syntax

```psj
Geometry.Edge.Circle(...)
```

Macro: [ImprintCircleS](../../macro/geometry/ImprintCircleS)

Ribbon: <menuselection>Geometry &#187; Edge &#187; Circle</menuselection>

## Inputs

### `veclPositions`

- A _List of Position_ specifying points on faces where the circle will be imprinted.
- This is a required input.

### `crlTargetFace`

- A _List of Cursor_ specifying the target faces on which the edges are imprinted.
- This is a required input.

### `dInRadius`

- A _Double_ specifying inner circle's radius. This argument is to be used when the value of _iNoOfLayer_ argument is greater than 1. Possible values are _0.0_ ≤ _dInRadius_ ≤ _dOutRadius_. The unit is fixed to [mm] unit.
- The default value is 1.

### `dOutRadius`

- A _Double_ specifying outer circle's radius. The unit is fixed to [mm] unit.
- The default value is 4.

### `iNoOfLayer`

- An _Integer_ specifying number of layers to be imprinted from circle center.
- The default value is 1.

### `iNoOfDiv`

- An _Integer_ specifying the number of segments in which the circle will be divided equally.
- The default value is 30.

### `bBreakFace`

- A _Boolean_ specifying whether to break the given faces where possible.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the created circle edges.

## Sample Code

```psj {3-6}
Geometry.Part.Cube()

circle_lines = Geometry.Edge.Circle(veclPositions=[[0.006666666666666666, 0.005555555555555556, 0.01], 
                                                [0.002222222222222222, 0.006666666666666666, 0.01]], 
                                                crlTargetFace=[Face(26)], 
                                                dOutRadius=2.0)
JPT.Debugger(circle_lines)
```
