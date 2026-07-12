---
id: Geometry-Part-Cone
title: Geometry.Part.Cone()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a cone shaped body in a specific location. Its relative location is computed to the specified local coordinate system
---

## Description

Create a cone body in a specific location.
Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Cone(...)
```

Macro: [CreateCone](../../macro/geometry/CreateCone)

Ribbon: <menuselection>Geometry &#187; Part &#187; Cone</menuselection>

## Inputs

### `dlOrigin`

- A _List of Double_ specifying the X, Y, and Z coordinates of the origin point.
- The default value is [0.0,0.0,0.0].

### `dBottomRadius`

- A _Double_ specifying the radius of the bottom face in meter.
- The default value is 0.01.

### `dHeight`

- A _Double_ specifying the cone height in meter.
- The default value is 0.02.

### `iCircularNodes`

- An _Integer_ specifying the number of nodes to be generated on the arc.
- The default value is 20.

### `iAxialNodes`

- An _Integer_ specifying the number of nodes to be generated on the axial direction of the cylinder.
- The default value is 20.

### `strName`

- A _String_ specifying the name of the creating cone.
- The default value is "Cone_1".

### `iPartColor`

- An _Integer_ specifying the color of the newly created part.
- The default value is 7105764.

### `crLocalCoordinate`

- A _Cursor_ specifying the local coordinate system.
- The default value is _None_.

## Return Code

The return value depends on the status of the creating process:

- _Cursor_: The cone is created successfully.
- _None_: The cone cannot be created.

## Sample Code
```psj {1}
cone = Geometry.Part.Cone(dlOrigin=[0.005, 0.005, 0.005], iPartColor=7829501)
JPT.Debugger(cone)
```
