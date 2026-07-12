---
id: Tools-Coordinates-Rotate
title: Tools.Coordinates.Rotate()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a Coordinate System by rotating with a specified value. Besides, it also be used to modify an existing Coordinate System
---

## Description

Create a Coordinate System by rotating with a specified value. Besides, it also be used to modify an existing Coordinate System.

## Syntax

```psj
Tools.Coordinates.Rotate(...)
```
Macro: [CreateCoordinateRotate](../../macro/tools/RotateCoordinate)

Ribbon: <menuselection>Tools &#187; Coordinates &#187; Rotate</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of the Coordinate.
- The default value is "CRect1".

### `iCoordType`

- An _Integer_ specifying the type of Coordinate system, which is one of the following:
  - If _iCoordType=0_: Rectangular Coordinate - which can be known as Cartesian Coordinate System (Oxyz)
  - If _iCoordType=1_: Cylindrical Coordinate - (r, φ, z) Coordinate System, where (r, φ, z) are (radial distance, azimuth angle, axial Coordinate or height z) respectively
  - If _iCoordType=2_: Spherical Coordinate - (r, θ, φ) Coordinate System, where (r, θ, φ) are (radial distance, azimuth angle, polar angle) respectively
- The default value is 0.

### `vecRotate`

- A _Vector_ specifying the rotation vector. Every component of this vector specified a degree to rotate the Coordinate about axis x, y, z, respectively. The unit of this argument is in degree (°).
- The default value is [0.0,0.0,0.0].

### `bCreateNew`

- A _Boolean_ specifying the option to create a new Coordinate or not. This argument uses follow with `crEdit`, when `crEdit` is defined, the argument `bCreateNew` uses to allow creating a new one based on selected Coordinate System or just modified the selected Coordinate System.
  - If _True_: A new Coordinate will be created.
  - If _False_: The Coordinate specified in `crEdit` will be modified.
- The default value is True.

### `crRefCoord`

- A _Cursor_ specifying the coordinate reference system to rotate the Coordinate specified in `crEdit`. The angles specified in `vecRotate` will be computed from this reference Coordinate.
- The default value is _None_ (Global Coordinate).

### `posCenterRot`

- A _Position_ specifying the position of rotation center.
- The default value is _None_.

### `crEdit`

- A _Cursor_ specifying an existing Coordinate System to modify. If the `bCreateNew` is _False_, this specified Coordinate will be modified, while `bCreateNew` is _True_, a new Coordinate will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created Coordinate.

## Sample Code

```psj {6,7,8,9,10}
Geometry.Part.Cube()
Tools.Coordinates.ThreeNode(crlNodes=[Node(7, 
                                           63, 
                                           87)])

created_coord = Tools.Coordinates.Rotate(vecRotate=[59.9886811502157, 0.0, 0.0], 
                                         bCreateNew=False,
                                         crRefCoord=Coord(1),
                                         posCenterRot=None, 
                                         crEdit=Coord(1))

JPT.Debugger(created_coord)
```
