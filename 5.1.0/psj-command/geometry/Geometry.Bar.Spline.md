---
id: Geometry-Bar-Spline
title: Geometry.Bar.Spline()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a spline-curve bar part passing though the selected nodes
---

## Description

Create a spline-curve bar part passing though the selected nodes.

## Syntax

```psj
Geometry.Bar.Spline(...)
```

Ribbon: <menuselection>Geometry &#187; Bar &#187; Spline</menuselection>

## Inputs

### `crlNodes`

- A _List of Cursor_ specifying either a series of nodes (interpolation points) through which the curve passes. At least three nodes must be specified.
- This is a required input.

### `crPart`

- A _Cursor_ specifying the part that the spline bar will belong to. If set none, a new bar part will be created.
- The default value is _None_.

### `strName`

- A _String_ specifying the name of new bar part.
- The default value is "Bar_1".

## Return Code

A _Cursor_ specifying the created entity.
    - If _crPart_ = _None_ then return a cursor of new created bar part.
    - If _crPart_ is specified then return a cursor of new created edge.

## Sample Code

```psj {3}
Geometry.Part.Cube()

newBar = Geometry.Bar.Spline(crlNodes=[Node(440, 463, 443, 474)])
JPT.Debugger(newBar)
```
