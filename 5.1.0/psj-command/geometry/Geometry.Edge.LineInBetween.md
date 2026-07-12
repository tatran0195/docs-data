---
id: Geometry-Edge-LineInBetween
title: Geometry.Edge.LineInBetween()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create edges between two selected edges
---

## Description

Create edges between two selected edges.

## Syntax

```psj
Geometry.Edge.LineInBetween(...)
```

Macro: 

Ribbon: <menuselection>Geometry &#187; Edge &#187; LineInBetween</menuselection>

## Inputs

### `crlEdges`

- A _List of Cursor_ specifying the target edges.
- This is a required input.

### `crlFaces`

- A _List of Cursor_ specifying the target faces on which the edges are imprinted. 
- This is a required input.

### `iNumLine`

- An _Integer_ specifying the number of lines.
- The default value is 1

### `bBreakFace`

- A _Boolean_ specifying whether to break the given faces where possible.
- The default value is _True_.

### `bExtend`

- A _Boolean_ specifying whether to extend the offset edges to the nearest boundary edges.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3}
Geometry.Part.Cube(iPartColor=6484066)

between_lines = Geometry.Edge.LineInBetween(crlEdges=[Edge(20, 18)], crlFaces=[Face(26)], numLine=2)

JPT.Debugger(between_lines)
```


