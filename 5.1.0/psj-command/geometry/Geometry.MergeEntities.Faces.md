---
id: Geometry-MergeEntities-Faces
title: Geometry.MergeEntities.Faces()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Merge the selected faces into a single face
---

## Description

Merge the selected faces into a single face.

## Syntax

```psj
Geometry.MergeEntities.Faces(...)
```

Ribbon: <menuselection>Geometry &#187; Merge Entities &#187; Faces</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the faces using for merging.
- This is a required input.

### `bMergeEdge`

- A _Boolean_ whether to merge edges between faces to be a continuously edges or not.
- The default value is _True_.

### `bRemoveNonBoundEdge`

- A _Boolean_ whether to remove the edges which are not a boundary edge.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying a list of faces after executing the function.

## Sample Code

```psj {8}
Geometry.Part.Cube()
Geometry.Edge.Line(dllPoints=[[0.005, 0, 0.01],
                              [0.006, 0.01, 0.01]],
                   crlFaces=[Face(26)])
Geometry.Edge.Line(dllPoints=[[0.002, 0.002, 0.01],
                              [0.003, 0.005, 0.01]],
                   crlFaces=[Face(26)])
merged_faces = Geometry.MergeEntities.Faces(crlFaces=[Face(26, 28)])
JPT.Debugger(merged_faces)
```
