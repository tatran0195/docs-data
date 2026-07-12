---
id: Geometry-Face-FromMesh
title: Geometry.Face.FromMesh()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a new geometric face from the specified mesh face
---

## Description

Create a new part entity containing the new geometric face from the specified mesh face.

## Syntax

```psj
Geometry.Face.FromMesh(...)
```

Macro: [CreateFaceFromMeshFace](../../macro/geometry/CreateFaceFromMeshFace)

Ribbon: <menuselection>Geometry &#187; Face &#187; Face from Mesh Face</menuselection>

## Inputs

### `crFace`

- A _Cursor_ specifying the mesh face that the new face is created base on.
- This is a required input.

## Return Code

A _Cursor_ specifying the new created face.

## Sample Code

```psj {3}
Geometry.Part.Cube()

created_face = Geometry.Face.FromMesh(crFace=Face(26))
JPT.Debugger(created_face)
```
