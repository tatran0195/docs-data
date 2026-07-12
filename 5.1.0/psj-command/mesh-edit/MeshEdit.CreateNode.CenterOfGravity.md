---
id: MeshEdit-CreateNode-CenterOfGravity
title: MeshEdit.CreateNode.CenterOfGravity()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: create node Center Of Gravity
---

## Description

Create node Center Of Gravity

## Syntax

```psj
MeshEdit.CreateNode.CenterOfGravity(...)
```

Ribbon: <menuselection>MeshEdit &#187; CreateNode &#187; CenterOfGravity</menuselection>

## Inputs

### `iCreationType`

- An _Integer_ specifying the creation type.
    - 0: Gravity
    - 1: Shape
- The default value is 1.

### `iNewNodeID`

- An _Integer_ specifying the new node ID.
- The default value is the maximum node ID + 1.

### `crlParts`

- A _List of Cursor_ specifying the selected part.
- The default value is [].

### `crlBarPart`

- A _List of Cursor_ specifying the selected bar part.
- The default value is [].

### `crlFaces`

- A _List of Cursor_ specifying the selected face.
- The default value is [].

## Return Code

- A _Cursor_ specifying the created floating node.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cube()

# Create center node of gravity
newNode = MeshEdit.CreateNode.CenterOfGravity(iNodeID=489, crlTargets=[Part(1)])
JPT.Debugger(newNode) # for checking the return value
```
