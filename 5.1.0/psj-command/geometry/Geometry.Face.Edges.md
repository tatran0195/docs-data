---
id: Geometry-Face-Edges
title: Geometry.Face.Edges()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a face using the given edges as the face's boundaries. It will create a face by creating the geometry consisting of the underlying surface, associated edges, and vertices. The planar surfaces and smooth surfaces are switched by changing the related arguments
---

## Description

Create a face using the given edges as the face's boundaries. It will create a face by creating the geometry consisting of the underlying surface, associated edges, and vertices. The planar surfaces and smooth surfaces are switched by changing the related arguments.

## Syntax

```psj
Geometry.Face.Edges(...)
```

Macro: [CreateFaceFromEdges](../../macro/geometry/CreateFaceFromEdges)

Ribbon: <menuselection>Geometry &#187; Face &#187; Edges</menuselection>

## Inputs

### `crlEdges`

- A _List of Cursor_ specifying the edges that bound the new face. Either _crlEdges_ or _crlNodes_ must be specified.

### `crlParts`

- A _List of Cursor_ specifying a given part to that the new face will belong.
- The default value is [].

### `crlNodes`

- A _List of Cursor_ specifying two nodes to define the direction in which the curved surface be created smoothly. If _crlNodes_ is specified, the curved surface will be smoother than the face created by bound edges only.
- The default value is [].

### `bSharedFace`

- A _Boolean_ specifying whether to create a shared face when the given edges are shared edges.
- The default value is _False_.

### `bSmoothFace`

- A _Boolean_ specifying whether to create a smooth face instead of planar face.
- The default value is _False_.

### `bCreatePart`

- A _Boolean_ specifying whether to stitch the newly created face to the new part. If _bSharedFace=True_, this argument will be ignored.
- The default value is _False_.

### `bImproved`

- A _Boolean_ specifying whether the newly created face is created with smooth direction. This argument does not affect the operation if _crlNodes_ is not specified.
- The default value is _False_.

### `bBarsOnly`

- A _Boolean_ indicating whether all of the selected edges are Bar part only.
- The default value is _False_.

### `bOnlyOnePart`

- A _Boolean_ indicating whether the newly created face is in the same new part. If _bCreatePart=False_, this argument will be ignored.
- The default value is _True_.

### `bIncludeMidNodes`

- A _Boolean_ specifying whether to include middle nodes when creating face.
- The default value is _False_.

## Return Code

A _Cursor_ specifying the new created face.

## Sample Code

```psj {3}
Geometry.Part.Cube()

created_face = Geometry.Face.Edges(crlEdges=[Edge(9, 19)])

JPT.Debugger(created_face)
```
