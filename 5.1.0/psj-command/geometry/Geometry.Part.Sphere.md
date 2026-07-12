---
id: Geometry-Part-Sphere
title: Geometry.Part.Sphere()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a sphere body in a specific location. Its relative location is computed to the specified local coordinate system
---

## Description

Create a sphere body in a specific location.
Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Sphere(...)
```

Macro: [CreateSphere](../../macro/geometry/CreateSphere)

Ribbon: <menuselection>Geometry &#187; Part &#187; Sphere</menuselection>

## Inputs

### `dlOrigin`

- A _List of Double_ representing the X, Y, and Z coordinates of the origin point (The center of the sphere).
- The default value is [0,0,0].

### `dRadius`

- A _Double_ specifying the radius of the sphere in meter.
- The default value is 0.005.

### `iLatitudeDivisions`

- An _Integer_ specifying the number of nodes to be generated on the latitude direction.
- The default value is 20.

### `iLongitudeDivisions`

- An _Integer_ specifying the number of nodes to be generated on the longitudinal direction.
- The default value is 20.

### `strName`

- A _String_ specifying the name of the creating part.
- The default value is "Sphere_1".

### `iPartColor`

- An _Integer_ specifying the color of the creating part.
- The default value is 7105764.

### `crLocalCoordinate`

- A _Cursor_ specifying the local coordinate system.
- The default value is _None_.

## Return Code

The return value depends on the status of the creating process:

- _Cursor_: The sphere is created successfully.
- _None_: The sphere cannot be created.

## Sample Code

```psj {1}
sphere = Geometry.Part.Sphere(dlOrigin=[0.005, 0.0, 0.0], iPartColor=13259210)
JPT.Debugger(sphere)
```
