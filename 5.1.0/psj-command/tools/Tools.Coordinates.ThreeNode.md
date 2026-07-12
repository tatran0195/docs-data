---
id: Tools-Coordinates-ThreeNode
title: Tools.Coordinates.ThreeNode()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a Coordinate System by selecting 3 nodes
---

## Description

Create a Coordinate System by selecting 3 nodes.

## Syntax

```psj
Tools.Coordinates.ThreeNode(...)
```

Ribbon: <menuselection>Tools &#187; Coordinates &#187; ThreeNode</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of the Coordinate system.
- The default value is "CRect1".

### `iCoordType`

- An _Integer_ specifying the type of Coordinate system, which is one of the following:
  - If _iCoordType=0_: Rectangular Coordinate - which can be known as Cartesian Coordinate System (Oxyz)
  - If _iCoordType=1_: Cylindrical Coordinate - (r, φ, z) Coordinate System, where (r, φ, z) are (radial distance, azimuth angle, axial Coordinate or height z) respectively
  - If _iCoordType=2_: Spherical Coordinate - (r, θ, φ) Coordinate System, where (r, θ, φ) are (radial distance, azimuth angle, polar angle) respectively
- The default value is 0.

### `iOrder`

- An _Integer_ specifying the order of nodes or points when selecting the origin and axes of the Coordinate. This parameter can be one of the following:
  - If _iOrder=0_: O.Z.ZX Plane - Select in the order of Origin, a point on the Z-axis and a point on the ZX plane.
  - If _iOrder=1_: O.X.ZX Plane - Select in the order of Origin, a point on the X-axis and a point on the ZX plane.
  - If _iOrder=2_: O.Y.XY Plane - Select in the order of Origin, a point on the Y-axis and a point on the XY plane.
  - If _iOrder=3_: O.X.XY Plane - Select in the order of Origin, a point on the X-axis and a point on the XY plane.
  - If _iOrder=4_: O.Z.YZ Plane - Select in the order of Origin, a point on the Z-axis and a point on the YZ plane.
  - If _iOrder=5_: O.Y.YZ Plane - Select in the order of Origin, a point on the Y-axis and a point on the YZ plane.
- The default value is 0.

### `crlNodes`

- A _List of Cursor_ specifying the nodes to create the Coordinate.
- If the `veclPoints` is not defined, this argument will be a required input. If this parameter is not defined, `veclPoints` must be defined.

### `veclPoints`

- A _List of Vector_ specifying the points to create the Coordinate. This parameter can be used only when `crlNodes` is not defined, otherwise node selection will be prioritized.
- The default value is [].

### `crRefCoord`

- A _Cursor_ specifying the coordinate reference system to create user Coordinate. The positions specified in `crlNodes` (or `veclPoints`) will be computed from this reference Coordinate.
- The default value is _None_ (Global Coordinate System).

### `crEdit`

- A _Cursor_ specifying an existing Coordinate. If this parameter is used, the specified Coordinate will be modified. If it is left _None_, a new Coordinate will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created Coordinate.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube()

created_coord = Tools.Coordinates.ThreeNode(crlNodes=[Node(7, 
                                                           93, 
                                                           477)])

JPT.Debugger(created_coord)
```
