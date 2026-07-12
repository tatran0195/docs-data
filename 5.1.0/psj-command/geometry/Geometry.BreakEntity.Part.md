---
id: Geometry-BreakEntity-Part
title: Geometry.BreakEntity.Part()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Separate parts into separated units based on each closed geometries
---

## Description

Separate parts into separated units based on each closed geometries.

## Syntax

```psj
Geometry.BreakEntity.Part(...)
```

Ribbon: <menuselection>Geometry &#187; Break Entity &#187; Part</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying parts to be separated.
- This is a required input.

## Return Code

A _List of Cursor_ specifying the speparated bodies.

## Sample Code

```psj {11}
Geometry.Part.Cube(iPartColor=16147556)
Geometry.DeleteEntity.Face([Face(24, 22, 26, 21, 25)])
Geometry.Edge.Line(dllPoints=[[0, 0.0022, 0], 
                              [0, 0.0022, 0.01]], 
                   crlFaces=[Face(23)])
Geometry.Edge.Line(dllPoints=[[0, 0.0067, 0], 
                              [0, 0.0067, 0.01]], 
                   crlFaces=[Face(23)])
Geometry.DeleteEntity.Face([Face(23)])

bodies = Geometry.BreakEntity.Part(crlParts=[Part(1)])

JPT.Debugger(bodies)
```
