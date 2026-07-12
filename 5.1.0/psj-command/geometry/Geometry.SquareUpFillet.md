---
id: Geometry-SquareUpFillet
title: Geometry.SquareUpFillet()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Square Up Fillet
---

## Description

This method turns fillet parts into rectangular angles.

## Syntax

```psj
Geometry.SquareUpFillet(crlFaces)
```

Macro: [SquareUpFillet](../../macro/geometry/SquareUpFillet)

Ribbon: <menuselection>Geometry &#187; Square Up Fillet</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying fillet faces to square up.
- This is a required input.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()

Geometry.MakeFillet(crlEdges=[Edge(19)])

Geometry.SquareUpFillet(crlFaces=[Face(27)])
```
