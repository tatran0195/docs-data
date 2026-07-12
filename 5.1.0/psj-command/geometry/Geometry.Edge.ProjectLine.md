---
id: Geometry-Edge-ProjectLine
title: Geometry.Edge.ProjectLine()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create new edges by projecting the selected edges onto the selected faces
---

## Description

Create new edges by projecting the selected edges onto the selected faces.

## Syntax

```psj
Geometry.Edge.ProjectLine(...)
```

Ribbon: <menuselection>Geometry &#187; Edge &#187; Project Line</menuselection>

## Inputs

### `crlEdges`

- A _List of Cursor_ specifying the edges to be projected.
- This is a required input.

### `crlFaces`

- A _List of Cursor_ specifying the target faces on which the edges are imprinted.
- This is a required input.

### `crlNodes`

- A _List of Cursor_ specifying two nodes to define the projection direction. This argument must be specified if _iType=1_.
- The default value is [].

### `bBreakFace`

- A _Boolean_ specifying whether to break the given faces where possible.
- The default value is _True_.

### `iType`

- An _Integer_ specifying the method to be used to project onto target faces.
  - If _iType=0_, project along to the face normal direction for the target faces.
  - If _iType=1_, project along to the direction defined by two nodes specified by the _crlNodes_.
  - If _iType=2_, project onto the face closest to the selected edge.
- The default value is 0.

### `bCheckGap`

- A _Boolean_ whether to limit the projection distance to the input value.
- The default value is _False_.

### `dGap`

- A _Double_ specifying the gap value. This argument is to be used when _bCheckGap=True_.
- The default value is 0.0.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {5}
Geometry.Part.Cube(iPartColor=13064794)
line = Geometry.Edge.Line(dllPoints=[[0.004444444444444444, 0.01, 0.01], [0.007777777777777778, 0, 0.01]], 
                          crlFaces=[Face(26)])

project_lines = Geometry.Edge.ProjectLine(crlEdges=line, crlFaces=[Face(25)])
JPT.Debugger(project_lines)
```
