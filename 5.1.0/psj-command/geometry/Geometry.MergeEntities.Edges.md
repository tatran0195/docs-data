---
id: Geometry-MergeEntities-Edges
title: Geometry.MergeEntities.Edges()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Merge all the selected edges into uninterrupted edges
---

## Description

Merge all the selected edges into uninterrupted edges.

## Syntax

```psj
Geometry.MergeEntities.Edges(...)
```

Ribbon: <menuselection>Geometry &#187; Merge Entities &#187; Edges</menuselection>

## Inputs

### `crlEdges`

- A _List of Cursor_ specifying the edges to be merged.
- This is a required input.

## Return Code

A _List of Cursor_ specifying the merged edges.

## Sample Code

```psj {4,5,6,7,8,9,10,11,12,13,14,15,16,17,18}
Geometry.Part.Cube()
Geometry.BreakEntity.Edge(crlNodes=[Node(95, 92, 90)])

merged_edges = Geometry.MergeEntities.Edges(crlEdges=[Edge(9, 
                                                           10, 
                                                           11, 
                                                           12, 
                                                           13, 
                                                           14, 
                                                           15, 
                                                           16, 
                                                           17, 
                                                           18, 
                                                           20, 
                                                           28, 
                                                           32, 
                                                           34, 
                                                           35)])

JPT.Debugger(merged_edges)
```
