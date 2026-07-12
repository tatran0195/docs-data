---
id: Geometry-Edge-NodeShortestPath
title: Geometry.Edge.NodeShortestPath()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create an edge by converting the element edges on the shortest path between two nodes into edge
---

## Description

Create an edge using the shortest path of element edges between two nodes.

## Syntax

```psj
Geometry.Edge.NodeShortestPath(...)
```

Ribbon: <menuselection>Geometry &#187; Edge &#187; 2 Nodes Shortest Path</menuselection>

## Inputs

### `crFirstNode`

- A _Cursor_ specifying the first node.
- This is a required input.

### `crSecondNode`

- A _Cursor_ specifying the second node.
- This is a required input.

### `bBreakFace`

- A _Boolean_ specifying whether to break the face which the shortest edges lie on where possible.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube(iPartColor=6215639)

created_edges = Geometry.Edge.NodeShortestPath(crFirstNode=Node(79), 
                                               crSecondNode=Node(91), 
                                               bBreakFace=0)
JPT.Debugger(created_edges)
```
