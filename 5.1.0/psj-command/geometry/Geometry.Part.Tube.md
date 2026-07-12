---
id: Geometry-Part-Tube
title: Geometry.Part.Tube()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a tubular body around specific edge(s)
---

## Description

Create a tubular body around specific edge(s).

## Syntax

```psj
Geometry.Part.Tube(...)
```

Ribbon: <menuselection>Geometry &#187; Part &#187; Tube</menuselection>

## Inputs

### `crlEdges`

- A _List of Cursor_ specifying edges which will be the center axis of the created tube.
- This is a required input.

### `strName`

- A _String_ specifying the name of the newly created part.
- The default value is "Tube_1".

### `bTri`

- A _Boolean_ specifying the mesh type of newly created part.
  - If _True_, Tri3 element will be used.
  - If _False_, Quad4 element will be used.
- The default value is _True_.

### `dRadius`

- A _Double_ specifying the radius of the tube.
- The default value is 0.01.

### `dMeshSizeAxis`

- A _Double_ specifying the mesh size of the center axis.
- The default value is 0.005.

### `dWMeshSizeCirc`

- A _Double_ specifying the mesh size of the circle at both ends (circumference).
  - If this parameter is used, [`iCircularNodes`](#icircularnodes) will be ignored (equal to -1).
- The default value is 0.001.

### `iCircularNodes`

- An _Integer_ specifying the number of nodes to be generated on the circle at both ends (circumference).
  - If this parameter is used, [`dWMeshSizeCirc`](#dwmeshsizecirc) will be ignored (equal to -1.0).
- The default value is 36.

## Return Code

A _Cursor_ specifying the created part.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

created_tube = Geometry.Part.Tube(strName="Tube_1", 
                                  crlEdges=[Edge(19)])

JPT.Debugger(created_tube)
```
