---
id: Geometry-Part-Trapezoid
title: Geometry.Part.Trapezoid()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a trapezoid body in a specific location. Its relative location is computed to the specified local coordinate system
---

## Description

Create a trapezoid body in a specific location.
Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Trapezoid(...)
```

Macro: [CreateTrapezoid](../../macro/geometry/CreateTrapezoid)

Ribbon: <menuselection>Geometry &#187; Part &#187; Trapezoid</menuselection>

## Inputs

### `dlOrigin`

- A _List of Double_ specifying the X, Y, and Z coordinates of the origin point (The center of the trapezoid).
- The default value is [0.0,0.0,0.0].

### `dlLength`

- A _List of Double_ specifying the trapezoid length in the X, Y, Z direction in meter.
- The default value is [0.01,0.01,0.01].

### `dTopXLength`

- A _Double_ specifying the length in the X-axis direction at top face.
- The default value is 7.0.

### `dRadius`

- A _Double_ specifying the radius in degrees of top face.
- The default value is 0.

### `ilAxialNodes`

- A _List of Integer_ specifying the number of nodes in X-, Y-, Z-axis direction, respectively.
- The default value is [10,10,10].

### `strName`

- A _String_ specifying the name of the creating part.
- The default value is "Trapezoid_1".

### `iPartColor`

- An _Integer_ specifying the color of the creating part.
- The default value is 7105764.

### `crLocalCoordinate`

- A _Cursor_ specifying the local coordinate system.
- The default value is _None_.

## Return Code

The return value depends on the status of the creating process:

- _Cursor_: The trapezoid is created successfully.
- _None_: The trapezoid cannot be created.

## Sample Code

```psj {1,2,3}
trapezoid = Geometry.Part.Trapezoid(dlLength=[0.02, 0.01, 0.01],
                                    strName="Trapezoid_5",
                                    iPartColor=7961077)
JPT.Debugger(trapezoid)
```
