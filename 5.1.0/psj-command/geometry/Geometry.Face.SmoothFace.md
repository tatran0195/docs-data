---
id: Geometry-Face-SmoothFace
title: Geometry.Face.SmoothFace()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create geometric face from given boundaries set by selected edges.
---

## Description

Create geometric face from given boundaries set by selected edges.
This function can create curved surface if selected edges are curved.

## Syntax

```psj
Geometry.Face.SmoothFace(...)
```

Macro: CreateSmoothFaceGUI

Ribbon: <menuselection>Geometry &#187; Face &#187; SmoothFace</menuselection>

## Inputs

### `crlTargets`

- A _List of Cursor_ specifying boundary edges.
- This is a required input.

### `iElementGeneration`

- An _Integer_ specifying element type.
  - 0: TRI
  - 1: QUAD 
- The default value is 0.

### `dGradation`

- A _Double_ specifying gradation factor.
- The default value is 1.

### `bFaceSmooth`

- A _Boolean_ specifying connection continuity.
  - _False_: G0
  - _True_: G1 
- The default value is _True_.

### `crlTargetParts`

- A _List of Cursor_ specifying a part that the created face belongs to. If _crlTargetParts_ is empty then creating the new part.
- The default value is [].

### `bInterpolation`

- A _Boolean_ specifying whether to make facet sizes or mesh sizes uniform.
- The default value is _False_.

## Return Code

A _Cursor_ specifying the new created face.

## Sample Code

```psj {9}
Geometry.Part.Sphere()
Geometry.Edge.Angle(
    [CursorPair(Node(146), Node(147)), 
    CursorPair(Node(148), Node(168)), 
    CursorPair(Node(267), Node(268)), 
    CursorPair(Node(224), Node(244))])
Geometry.DeleteEntity.Face(crlFaces=[Face(2)])

created_face = Geometry.Face.SmoothFace(crlTargets=[Edge(3)])
JPT.Debugger(created_face)
```
