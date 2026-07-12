---
id: Geometry-Part-Frustum
title: Geometry.Part.Frustum()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a frustum body in a specific location. Its relative location is computed to the specified local coordinate system
---

## Description

Create a frustum body in a specific location.
Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Frustum(...)
```

Macro: [CreateCylinderFrustum](../../macro/geometry/CreateCylinderFrustum)

Ribbon: <menuselection>Geometry &#187; Part &#187; Frustum</menuselection>

## Inputs

### `dlOrigin`

- A _List of Double_ representing the X, Y, and Z coordinates of the origin point (The center of the frustum).
- The default value is [0,0,0].

### `dTopRadius`

- A _Double_ specifying the radius of the frustum in meter.
- The default value is 0.005.

### `dBottomRadius`

- A _Double_ specifying the radius in meters of the bottom end of the frustum.
- The default value is 0.01.

### `dHeight`

- A _Double_ specifying the height of the frustum..
- The default value is 0.02.

### `iCircularNodes`

- An _Integer_ specifying the number of nodes to be generated on the circle at both ends.
- The default value is 20.

### `iAxialNodes`

- An _Integer_ specifying the number of nodes in the axial direction of the cylinder.
- The default value is 20.

### `strName`

- A _String_ specifying the name of the newly created part.
- The default value is "Frustum_1".

### `iPartColor`

- An _Integer_ specifying the color of the newly created part.
- The default value is 7105764.

### `crLocalCoordinate`

- A _Cursor_ specifying the local coordinate system.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created part.

## Sample Code

```psj
created_frustum = Geometry.Part.Frustum(dTopRadius=0.003, iPartColor=14903267)
JPT.Debugger(created_frustum)
```
