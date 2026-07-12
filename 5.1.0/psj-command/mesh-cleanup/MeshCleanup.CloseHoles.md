---
id: MeshCleanup-CloseHoles
title: MeshCleanup.CloseHoles()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: close holes
---

## Description

Close holes

## Syntax

```psj
MeshCleanup.CloseHoles(...)
```

Ribbon: <menuselection>MeshCleanup &#187; CloseHoles</menuselection>

## Inputs

### `crlEdges`

- A _List of Cursor_ specifying the edge.
- The default value is [].

### `dAreaMin`

- A _Double_ specifying the area minimum.
- The default value is 0.0.

### `dAreaMax`

- A _Double_ specifying the area maximum.
- The default value is 543210.0.

### `bMergeFace`

- A _Boolean_ specifying the merge face.
- The default value is False.

### `bMergeEdge`

- A _Boolean_ specifying the merge edge.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
# Prepare a model - a cylinder with holes 
Geometry.Part.Cylinder(
    bHollow=True, 
    dTopInnerRadius=0.003, 
    dBottomInnerRadius=0.003, 
    iPartColor=7829501
)

JPT.Exec('DeleteFace([7], 1)')

# Find hole edges
result = MeshCleanup.FindHoles()
flag, edge_list = JPT.MacroResultParser(result,["number","list_cursor"])

# Input edges to close hole
MeshCleanup.CloseHoles(
    crlEdges=edge_list, 
    dAreaMin=0.0, 
    dAreaMax=0.54321, 
    bMergeFace=False, 
    bMergeEdge=False
)
```
