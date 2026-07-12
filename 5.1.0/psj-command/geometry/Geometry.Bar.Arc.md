---
id: Geometry-Bar-Arc
title: Geometry.Bar.Arc()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create an arc-shaped bar part passing though the 3 selected nodes
---

## Description

Create an arc-shaped bar part passing though the 3 selected nodes.

## Syntax

```psj
Geometry.Bar.Arc(...)
```

Ribbon: <menuselection>Geometry &#187; Bar &#187; Arc (3 Nodes)</menuselection>

## Inputs

### `crlNodes`

- A _List of Cursor_ specifying three specified nodes to create arc.
- This is a required input.

### `crPart`

- A _Cursor_ specifying the part that the arc-shaped bar will belong to. If set none, a new bar part will be created.
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

newBar = Geometry.Bar.Arc(crlNodes=[Node(446, 451, 474)])
JPT.Debugger(newBar)
```
