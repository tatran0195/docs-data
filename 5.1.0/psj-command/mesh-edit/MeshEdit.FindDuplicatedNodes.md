---
id: MeshEdit-FindDuplicatedNodes
title: MeshEdit.FindDuplicatedNodes()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Find nodes with overlapping positions.
---

## Description

Find nodes with overlapping positions.

## Syntax

```psj
MeshEdit.FindDuplicatedNodes(...)
```

Macro: FindDuplicatedNodes

Ribbon: <menuselection>MeshEdit &#187; FindDuplicatedNodes &#187; Find</menuselection>

## Inputs

### `crlTargets`

- A _List of Cursor_ specifying target entities to search duplicate nodes among them.
- The default value is [].

### `dTolerance`

- A _Double_ specifying torelance to search nodes duplication.
- The default value is 1e-5.

### `bCreateGroup`

- A _Bool_ specifying flag to create group of detected nodes.
- The default value is False.

### `bSelect`

- A _Bool_ specifying flag to select detected nodes.
- The default value is False.

### `bPreview`

- A _Bool_ specifying flag to display preview after execution.
- The default value is False.

## Return Code

A _List of CursorStr_ specifying the detected nodes.

## Sample Code

```psj {9-11}
# Preapre model
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(
    dlLength=[0.0105, 0.011, 0.01], 
    strName="Cube_2", 
    iPartColor=7961077)

# Find duplication
dupnodes=MeshEdit.FindDuplicatedNodes(
    crlTargets=[Part(1, 2)], 
    bSelect=True)

print(f"{len(dupnodes)} nodes are duplicated")
print(f"nodes' id:{[i.getID() for i in dupnodes]}")
```

