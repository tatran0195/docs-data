---
id: MidPlaneEdit-AddItems-Face-EFProject
title: MidPlaneEdit.AddItems.Face.EFProject()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Creat new face by project edge to destination face
---

## Description

Creat new face by project edge to destination face

## Syntax

```psj
MidPlaneEdit.AddItems.Face.EFProject(crlEdges, crlFaces, bMergeFace, bMergeEdge, dMergeEdgeAngle, bMultiEF)
```

Ribbon: <menuselection>MidPlaneEdit &#187; AddItems &#187; Face &#187; EFProject</menuselection>

## Inputs

### `crlEdges`

- A _List of Cursor_ specifying the edge.
- This is a required input.

### `crlFaces`

- A _List of Cursor_ specifying the face.
- This is a required input.

### `bMergeFace`

- A _Boolean_ specifying the merge face.
- This is a required input.

### `bMergeEdge`

- A _Boolean_ specifying the merge edge.
- This is a required input.

### `dMergeEdgeAngle`

- A _Double_ specifying the merge edge angle.
- This is a required input.

### `bMultiEF`

- A _Boolean_ specifying the multi edge and face .
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.AddItems.Face.EFProject(crlEdges, crlFaces, bMergeFace, bMergeEdge, dMergeEdgeAngle, bMultiEF)
```
