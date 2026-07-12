---
id: Tools-Coordinates-Offset
title: Tools.Coordinates.Offset()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a Coordinate System by offsetting with a specified value. Besides, it also be used to modify an existing Coordinate System
---

## Description

Create a Coordinate System by offsetting with a specified value. Besides, it also be used to modify an existing Coordinate System.

## Syntax

```psj
Tools.Coordinates.Offset(...)
```

Ribbon: <menuselection>Tools &#187; Coordinates &#187; Offset</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name.
- The default value is "CRect1".

### `iCoordType`

- An _Integer_ specifying the type of Coordinate system, which is one of the following:
  - If _iCoordType=0_: Rectangular Coordinate - which can be known as Cartesian Coordinate System (Oxyz)
  - If _iCoordType=1_: Cylindrical Coordinate - (r, φ, z) Coordinate System, where (r, φ, z) are (radial distance, azimuth angle, axial Coordinate or height z) respectively
  - If _iCoordType=2_: Spherical Coordinate - (r, θ, φ) Coordinate System, where (r, θ, φ) are (radial distance, azimuth angle, polar angle) respectively
- The default value is 0.

### `vecTranslate`

- A _Vector_ specifying the translation vector which contains position value in metre.
- The default value is [0.0,0.0,0.0].

### `bCreateNew`

- A _Boolean_ specifying the option to create a new Coordinate or not. This argument uses follow with `crEdit`, when `crEdit` is defined, the argument `bCreateNew` uses to allow creating a new one based on selected Coordinate System or just modified the selected Coordinate System.
  - If _True_: A new Coordinate will be created.
  - If _False_: The Coordinate specified in `crEdit` will be modified.
- The default value is True.

### `crRefCoord`

- A _Cursor_ specifying the coordinate reference system to offset the Coordinate specified in `crEdit`. The values specified in `vecTranslate` will be computed from this reference Coordinate.
- The default value is _None_ (Global Coordinate).

### `crEdit`

- A _Cursor_ specifying an existing Coordinate System to modify. If the `bCreateNew` is _False_, this specified Coordinate will be modified, while `bCreateNew` is True, a new Coordinate will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created Coordinate.

## Sample Code

````psj {6,7,8,9}
Geometry.Part.Cylinder()
Tools.Coordinates.ThreeNode(veclPoints=[[0.01, 0.01, 0.01], 
                                        [0.002, 0.002, 0.002], 
                                        [0.01, 0.001, 0.01]])

created_coord = Tools.Coordinates.Offset(strName="CRect2", 
                                         vecTranslate=[0.01, 
                                                       0.01, 
                                                       0.01])

JPT.Debugger(created_coord)
````
