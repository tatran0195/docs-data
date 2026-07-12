---
id: Geometry-FCircVertexAdjust
title: Geometry.FCircVertexAdjust()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Align the vertexes positions on the circles. Cylinder faces can also be split by 90 degree, for creating mapped mesh
---

## Description

Align the vertexes positions on the circles. Cylinder faces can also be split by 90 degree, for creating mapped mesh.

## Syntax

```psj
Geometry.FCircVertexAdjust(...)
```

Ribbon: <menuselection>Geometry &#187; FCirc Vertex Adjust</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the parts whose vertices will be adjusted.
- The default value is [].

### `bFullCylinder`

- A _Boolean_ specifying whether to divide the full cylinder faces by 90 degree or not. If _bFullCylinder=True_, the cylindrical surfaces and torus surfaces in the selected parts will be divided into four locations at each 90 degree. This splitting makes it easier to create a mapped mesh.
- The default value is _False_.

### `bCylinderMoreThan90`

- A _Boolean_ specifying whether to divide the cylinder faces more than 90 degree interior angle or not. The cylinder surfaces in the selected part with an internal angle of 90 degree or more will be divided at the 90 degree position if _bCylinderMoreThan90=True_.
- The default value is _False_.

### `dMinRadius`

- A _Double_ specifying the minimum radius of the cylinder faces to be split. Faces with radius less than the input value are kept.
- The default value is 0.0.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {7}
# Make a cylinder with 2 misaligned vertex
Geometry.Part.Cylinder()
Geometry.BreakEntity.Edge(crlNodes=[Node(66)])
Geometry.BreakEntity.Edge(crlNodes=[Node(51)])

# Align vertex positions on 2 circles of the cylinder
adjust_status = Geometry.FCircVertexAdjust(crlParts=[Part(1)])

JPT.Debugger(adjust_status)
```
