---
id: MidPlaneEdit-AddItems-Edge-ProjectEdgeToFace
title: MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: project an edge to face to get a new edge
---

## Description

Project an edge to face to get a new edge

## Syntax

```psj
MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace(crlEdges, crlFaces, bExtendEdge=True)
```

Ribbon: <menuselection>MidPlaneEdit &#187; AddItems &#187; Edge &#187; ProjectEdgeToFace</menuselection>

## Inputs

### `crlEdges`

- A _List of Cursor_ specifying the edge.
- This is a required input.

### `crlFaces`

- A _List of Cursor_ specifying the face.
- This is a required input.

### `bExtendEdge`

- A _Boolean_ specifying the extend edge.
- The default value is True.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace(crlEdges, crlFaces, bExtendEdge=True)
```
