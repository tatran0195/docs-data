---
id: Geometry-Part-Wedge
title: Geometry.Part.Wedge()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a wedge shaped body in a specific location. This relative location is computed to the specified local coordinate system
---

## Description

Create a wedge shaped body in a specific location. This relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Wedge(...)
```

Macro: [CreateWedge](../../macro/geometry/CreateWedge)

Ribbon: <menuselection>Geometry &#187; Part &#187; Wedge</menuselection>

## Inputs

### `dlOrigin`

- A _List of Double_ representing the X-, Y-, and Z-coordinates of f the center of the wedge.
- The default value is [0.0,0.0,0.0].

### `dlLength`

- A _List of Double_ specifying length in meters in the X-, Y-, Z-axis direction.
- The default value is [0.01,0.01,0.01].

### `ilAxialNodes`

- A _List of Integer_ specifying the number of nodes along to each X-, Y-, Z-axis.
- The default value is [10,10,10].

### `strName`

- A _String_ specifying the name of the newly created part.
- The default value is "Wedge_1".

### `iPartColor`

- An _Integer_ specifying the color of the newly created part.
- The default value is 7105764.

### `crLocalCoordinate`

- A _Cursor_ specifying the local coordinate system.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the new wedge body.

## Sample Code

```psj {1}
wedge = Geometry.Part.Wedge(dlOrigin=[0.005, 0.005, 0.005], strName="Wedge", iPartColor=6409934)

JPT.Debugger(wedge)
```
