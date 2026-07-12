---
id: Geometry-Edge-ElementEdges
title: Geometry.Edge.ElementEdges()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create edges from the selected element edges
---

## Description

Create edges from the selected element edges.

## Syntax

```psj
Geometry.Edge.ElementEdges(...)
```

Macro: [CreateEdgeByElemEdge](../../macro/geometry/CreateEdgeByElemEdge)

Ribbon: <menuselection>Geometry &#187; Edge &#187; Element Edges</menuselection>

## Inputs

### `crplElemEdges`

- A _List of Pairs of Cursor_ specifying the element edges to be converted to edge.
- This is a required input.

### `bBreakEdge`

- A _Boolean_ specifying whether to break the faces which the given element edges lie on where possible.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube()

created_edges = Geometry.Edge.ElementEdges(crplElemEdges=[CursorPair(Node(443), Node(452)), 
                                                          CursorPair(Node(444), Node(445)), 
                                                          CursorPair(Node(454), Node(463))])
JPT.Debugger(created_edges)
```
