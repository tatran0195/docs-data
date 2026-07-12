---
id: Geometry-Part-Torus
title: Geometry.Part.Torus()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a donut body in a specific location. Its relative location is computed to the specified local coordinate system
---

## Description

Create a donut body in a specific location. Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Torus(...)
```

Macro: [CreateTorus](../../macro/geometry/CreateTorus)

Ribbon: <menuselection>Geometry &#187; Part &#187; Torus</menuselection>

## Inputs

### `dlOrigin`

- A _List of Double_ specifying the X, Y, and Z coordinates of the origin point (The center of the torus).
- The default value is [0.0,0.0,0.0].

### `dInnerRadius`

- A _Double_ specifying the radius of the inner circle of the torus in meter.
- The default value is 0.015.

### `dRingRadius`

- A _Double_ specifying the radius of the ring of the torus in meter.
- The default value is 0.02.

### `iCircumNodes`

- An _Integer_ specifying the number of nodes to be generated on the circumference of the ring of the torus.
- The default value is 20.

### `iRingNodes`

- An _Integer_ specifying the number of nodes to be generated on the cross-section of the ring of the torus.
- The default value is 20.

### `strName`

- A _String_ specifying the name of the creating part.
- The default value is "Torus_1".

### `iPartColor`

- An _Integer_ specifying the color of the creating part.
- The default value is 7105764.

### `crLocalCoordinate`

- A _Cursor_ specifying the local coordinate system.
- The default value is _None_.

## Return Code

The return value depends on the status of the creating process:

- _Cursor_: The torus is created successfully.
- _None_: The torus cannot be created.

## Sample Code

```psj {1}
torus = Geometry.Part.Torus(dlOrigin=[0.005, 0.005, 0.005], strName="Torus", iPartColor=7697908)
JPT.Debugger(torus)
```
