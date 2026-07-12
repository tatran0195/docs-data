---
id: Geometry-Part-Cube
title: Geometry.Part.Cube()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a cuboid body in a specific location. This relative location is computed to the specified local coordinate system
---

## Description

Create a cuboid body in a specific location. This relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Cube(...)
```

Macro: [CreateCube](../../macro/geometry/CreateCube)

Ribbon: <menuselection>Geometry &#10145; Part &#10145; Cube</menuselection>

## Inputs

### `dlOrigin`

- A _List of Double_ representing the X-, Y-, and Z-coordinates of the origin point.
- The default value is [0.0,0.0,0.0].

### `dlLength`

- A _List of Double_ specifying the cube length in meters in the X-, Y-, Z-axis direction.
- The default value is [0.01,0.01,0.01].

### `ilAxialNodes`

- A _List of Integer_ specifying the number of nodes along to each X-, Y-, Z-axis.
- The default value is [10,10,10].

### `strName`

- A _String_ specifying the name of the newly created part.
- The default value is "Cube_1".

### `iPartColor`

- An _Integer_ specifying the color of the newly created part.
- The default value is 7105764.

### `crLocalCoordinate`

- A _Cursor_ specifying the local coordinate system.
- The default value is _None_.

## Return Code

A _Cursor_ of cube if success, or _None_ if fail.

## Sample Code

```psj {1,2,3} 
created_cube = Geometry.Part.Cube(dlOrigin=[0.005, 0.005, 0.005], 
                                  strName="Cube_1", 
                                  iPartColor=13259210)
JPT.Debugger(created_cube)
```
