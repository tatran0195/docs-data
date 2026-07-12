---
id: Geometry-DeleteEntity-Vertex
title: Geometry.DeleteEntity.Vertex()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Delete the specified vertexes
---

## Description

Delete the specified vertexes.

## Syntax

```psj
Geometry.DeleteEntity.Vertex(...)
```

Ribbon: <menuselection>Geometry &#187; Delete Entity &#187; Vertex</menuselection>

## Inputs

### `crlVertices`

- A _List of Cursor_ specifying the vertexes to be deleted.
- This is a required input.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {6}
Geometry.Part.Cube()

Geometry.BreakEntity.Edge(crlEdges=[Edge(18)],
                          crlNodes=[Node(85)])

deleting_status = Geometry.DeleteEntity.Vertex(crlVertices=[Vertex(27)])

JPT.Debugger(deleting_status)
```
