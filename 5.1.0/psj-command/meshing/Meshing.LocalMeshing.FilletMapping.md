---
id: Meshing-LocalMeshing-FilletMapping
title: Meshing.LocalMeshing.FilletMapping()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Select and mesh all the existing fillet faces
---

## Description

Select and mesh all the existing fillet faces.

## Syntax

```psj
Meshing.LocalMeshing.FilletMapping(...)
```

Ribbon: <menuselection>Meshing &#187; LocalMeshing &#187; FilletMapping</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the list of target parts to search for fillet faces.
- The default value is [].

### `crlFaces`

- A _List of Cursor_ specifying the list of target faces to search for fillet faces.
- The default value is [].

### `dMinArcLength`

- A _Double_ specifying the minimum length of fillet edge in meter. This is a search criterion.
- The default value is 0.0.

### `dMaxArcLength`

- A _Double_ specifying the maximum length of fillet edge in meter. This is a search criterion.
- The default value is 0.009.

### `dMinArcRadius`

- A _Double_ specifying the minimum radius of fillet edge in meter. This is a search criterion.
- The default value is 0.0.

### `dMaxArcRadius`

- A _Double_ specifying the maximum radius of fillet edge in meter. This is a search criterion.
- The default value is 1.0.

### `bConvex`

- A _Boolean_ to enable (_True_) or disable (_False_) the search for convex fillet.
- The default value is _True_.

### `bConcave`

- A _Boolean_ to enable (_True_) or disable (_False_) the search for concave fillet.
- The default value is _True_.

### `dLayerAngle`

- A _Double_ specifying the angle between each fillet layer in degrees.
- The default value is 30.

### `dAxisAspectRatio`

- A _Double_ specifying the ratio of the length to the width of a layer.
- The default value is 3.

### `dAxisMinSize`

- A _Double_ specifying the minimum size for each dimension of a layer cell, in meter.
- The default value is 0.001

### `bAxisMinSize`

- A _Boolean_ specifying whether to use min size criterion or not.
- The default value is _True_.

### `dAxisMaxSize`

- A _Double_ specifying the maximum size for each dimension of a layer cell, in meter.
- The default value is 0.003.

### `bAxisMaxSize`

- A _Boolean_ specifying whether to use max size criterion or not.
- The default value is _True_.

### `iAxisMinMeshCount`

- An _Integer_ specifying the minimum node count on each dimension of every fillet faces. If a fillet faces has a dimension whose node count is less than the criterion, map meshing on the face will be skipped.
- The default value is 1.

### `bAxisMinMeshCount`

- A _Boolean_ specifying whether to use min mesh count criterion or not.
- The default value is _True_.

### `iElementType`

- An _Integer_ specifying the type 2D element to be created. It can be one of the following:
  - 0: Tri3.
  - 1: Quad4.
- The default value is 0.

### `dSingleLayerLength`

- A _Double_ specifying the maximum length of the single layer in meter.
- The default value is 0.001.

### `bSingleLayerLength`

- A _Boolean_ specifying whether to use single layer length criterion or not.
- The default value is _True_.

### `dSingleLayerRadius`

- A _Double_ specifying the maximum radius of the single layer in meter.
- The default value is 0.001.

### `bSingleLayerRadius`

- A _Boolean_ specifying whether to use single layer radius criterion or not.
- The default value is _False_.

### `iMinNumLayer`

- An _Integer_ specifying the minimum number of layers to be created.
- The default value is 3.

### `bMinNumLayer`

- A _Boolean_ specifying whether to use single min number of layers criterion or not.
- The default value is _True_.

### `bCreateReference=False`

- A _Boolean_ specifying whether to create a reference part after meshing or not.
- The default value is _True_.

### `bRemeshTheEnd`

- A _Boolean_ specifying whether to use local remesh for ending position of fillet to fit with surrounding mesh size or not.
- The default value is _False_.

### `bSkipComplexFace`

- A _Boolean_ specifying whether to skip complex fillet faces or not.
- The default value is _False_.

## Return Code

A _List of Cursor_ specifying the meshed fillet faces, or None if failed.

## Sample Code

```psj {8,9}
Geometry.Part.Cube()
Geometry.MakeFillet(crlEdges=[Edge(18, 19, 15)])

fillet_faces = Meshing.LocalMeshing.SelectFillet(crlParts=[Part(1)], 
                                                 crlFaces=[])

fillet_meshing = \
Meshing.LocalMeshing.FilletMapping(crlFaces=[Face(*[int(str(_).split(":")[-1].strip()) 
                                                    for _ in fillet_faces])])

JPT.Debugger(fillet_meshing)
```
