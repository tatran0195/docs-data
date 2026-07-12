---
id: Geometry-Bar-TwoNodes
title: Geometry.Bar.TwoNodes()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a Bar part from two selected nodes
---

## Description

Create a Bar part from two selected nodes.

## Syntax

```psj
Geometry.Bar.TwoNodes(...)
```

Macro: [CreateBar](../../macro/geometry/CreateBar)

Ribbon: <menuselection>Geometry &#187; Bar &#187; 2 Nodes</menuselection>

## Inputs

### `crStartNode`

- A _Cursor_ specifying the start node.
- This is a required input.

### `crEndNode`

- A _Cursor_ specifying the end node.
- This is a required input.

### `strName`

- A _String_ specifying the name of new part.
- The default value is "Bar_1".

### `iMeshOption`

- An _Integer_ specifying the option to generate element on Bar body.
    - If _iMeshOption=0_: The new Bar body has the number of 1D elements equal to _iMeshCount_.
    - If _iMeshOption=1_: The new Bar body has the size of 1D elements on the Bar body equal to _dMeshSize_.
- The default value is 0.

### `iMeshCount`

- An _Integer_ specifying the number of 1D elements on the Bar body. This argument should be specified when _iMeshOption=0_.
- The default value is 5.

### `dMeshSize`

- A _Double_ specifying the size of 1D elements on the Bar body. This argument should be specified when _iMeshOption=1_.
- The default value is 0.0.

## Return Code

A _Cursor_ specifying the created bar part.

## Sample Code

```psj {3}
Geometry.Part.Cube()

newBar = Geometry.Bar.TwoNodes(crStartNode=Node(5), crEndNode=Node(7))
JPT.Debugger(newBar)
```
