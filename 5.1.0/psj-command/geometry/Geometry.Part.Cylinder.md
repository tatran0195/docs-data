---
id: Geometry-Part-Cylinder
title: Geometry.Part.Cylinder()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a cylindrical body at a specific location. Its relative location is computed based on the specified local coordinate system
---

## Description

Create a cylindrical body at a specific location. Its relative location is computed based on the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Cylinder(...)
```

Ribbon: <menuselection>Geometry &#187; Part &#187; Cylinder</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of the newly created part.
- The default value is "Cylinder_1".

### `crLocalCoordinate`

- A _Cursor_ specifying the local coordinate system.
- The default value is _None_.

### `bHollow`

- A _Boolean_ specifying weather to hollow the created cylinder or not.
  - If _True_, the cylinder will have a hollow at the center with radius defined by `dTopInnerRadius` and `dBottomInnerRadius`.
  - If _False_, the cylinder will not have a hollow at the center.
- The default value is _False_.

### `bTapered`

- A _Boolean_ specifying weather to make the cylinder tapered (radius at two ends is different).
  - If _True_, the cylinder will be tapered with radius defined by `dBottomOuterRadius`.
  - If _False_, the cylinder will not be tapered.
- The default value is _False_.

### `dlOrigin`

- A _List of Double_ representing the X-, Y-, and Z-coordinates of the center of the cylinder.
- The default value is [0.0,0.0,0.0].

### `dTopInnerRadius`

- A _Double_ specifying the inner radius in meters of the top end of the cylinder.
- The default value is 0.001.

### `dTopOuterRadius`

- A _Double_ specifying the outer radius in meters of the top end of the cylinder.
- The default value is 0.01.

### `dBottomInnerRadius`

- A _Double_ specifying the inner radius in meters of the bottom end of the cylinder.
- The default value is 0.001.

### `dBottomOuterRadius`

- A _Double_ specifying the outer radius in meters of the bottom end of the cylinder.
- The default value is 0.01.

### `dHeight`

- A _Double_ specifying the height of the cylinder.
- The default value is 0.01.

### `iCircularNodes`

- An _Integer_ specifying the number of nodes to be generated on the circle at both ends.
- The default value is 36.

### `iAxialNodes`

- An _Integer_ specifying the number of nodes in the axial direction of the cylinder.
- The default value is 10.

### `iPartColor`

- An _Integer_ specifying the color of the newly created part.
- The default value is 7105764.

## Return Code

A _Cursor_ specifying the created part.

## Sample Code

```psj {1,2,3}
created_cylinder = Geometry.Part.Cylinder(dlOrigin=[0.005, 0.005, 0.005],
                                          strName="Cylinder_2", 
                                          iPartColor=7463537)

JPT.Debugger(created_cylinder)
```
