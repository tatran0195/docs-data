---
id: Geometry-BreakEntity-Face
title: Geometry.BreakEntity.Face()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Break the faces into separate units that are surrounded by edges
---

## Description

Break the faces into separate units that are surrounded by edges.

## Syntax

```psj
Geometry.BreakEntity.Face(...)
```

Macro: [BreakFace](../../macro/geometry/BreakFace)

Ribbon: <menuselection>Geometry &#187; Break Entity &#187; Face</menuselection>

## Inputs

### `crlFaces

- A _List of Cursor_ specifying faces to be separated.
- This is a required input.

## Return Code

A _List of Cursor_ specifying the faces after the break operation.

## Sample Code

```psj {8}
Geometry.Part.Cube()

Geometry.Edge.Line(dllPoints=[[0.01, 0, 0.01], 
                              [0, 0.01, 0.01]], 
                   crlFaces=[Face(26)],
                   bBreakFace=False)

faces = Geometry.BreakEntity.Face(crlFaces=[Face(26)])

JPT.Debugger(faces)
```
