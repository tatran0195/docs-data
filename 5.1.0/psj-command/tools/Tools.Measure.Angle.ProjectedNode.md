---
id: Tools-Measure-Angle-ProjectedNode
title: Tools.Measure.Angle.ProjectedNode()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Measure the projection angle onto the coordinate system plane
---

## Description

Measure the projection angle onto the coordinate system plane.

## Syntax

```psj
Tools.Measure.Angle.ProjectedNode(...)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Angle &#187; ProjectedNode</menuselection>

## Inputs

### `crNode`

- A _Cursor_ specifying the node.
- This is a required input.

### `strTarget`

- A _String_ specifying the target projection plane (2D), or the three-dimensional space (3D) to refer to measure. This parameter can be one of the following:
  - If _strTarget="XY"_: Return the angle that will project on plane Oxy.
  - If _strTarget="YZ"_: Return the angle that will project on plane Oyz.
  - If _strTarget="ZX"_: Return the angle that will project on plane Ozx.
  - If _strTarget="Angle"_: Return the angle in 3D space.
  - If _strTarget="All"_: Return all the 4 angle values in a list, in order "Angle", "XY", "YZ", "ZX".
- The default value is "All".

### `iPrecision`

- An _Integer_ specifying the precision.
- The default value is 6.

### `crCoord`

- A _Cursor_ specifying the coordinate system.
- The default value is _None_.

## Return Code

A _List of Double_ specifying the projected angles.

## Sample Code

```psj {2}
Geometry.Part.Cube(strName="Cube_2", iPartColor=7697908)
angle = Tools.Measure.Angle.ProjectedNode(crNode=Node(461))
JPT.Debugger(angle)
```
