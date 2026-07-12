---
id: Geometry-Face-FourEdges
title: Geometry.Face.FourEdges()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a face using the given four edges as the face's boundaries. The given edges must form a closed profile and must not contain multiple loops
---

## Description

Create a face using the given four edges as the face's boundaries. The given edges must form a closed profile and must not contain multiple loops.

## Syntax

```psj
Geometry.Face.FourEdges(...)
```

Macro: [CreateFaceFromFourEdges](../../macro/geometry/CreateFaceFromFourEdges)

Ribbon: <menuselection>Geometry &#187; Face &#187; Edges2 (4 Edges)</menuselection>

## Inputs

### `crlEdges`

- A _List of Cursor_ specifying four edges that bound the new face. The edges must form a closed profile and must not contain multiple loops.
- This is a required input.

## Return Code

A _Cursor_ specifying the new created face.

## Sample Code

```psj {5}
Geometry.Part.Cube()

Geometry.DeleteEntity.Face(crlFaces=[Face(26)])

created_face = Geometry.Face.FourEdges(crlEdges=[Edge(17, 18, 19, 20)])

JPT.Debugger(created_face)
```
