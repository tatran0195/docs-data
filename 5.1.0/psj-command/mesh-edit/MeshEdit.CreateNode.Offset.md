---
id: MeshEdit-CreateNode-Offset
title: MeshEdit.CreateNode.Offset()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a new node by offsetting a distance from the selected node or floating point
---

## Description

Create a new node by offsetting a distance from the selected node or floating point.

## Syntax

```psj
MeshEdit.CreateNode.Offset(...)
```

Macro: [CreateNodeOffset](../../macro/mesh-edit/CreateNodeOffset)

Ribbon: <menuselection>MeshEdit &#187; CreateNode &#187; Offset</menuselection>

## Inputs

### `vecOffset`

- A _List of Double_ specifying the offset vector.
- The default value is [].

### `iRepeat`

- An _Integer_ specifying the repeat times.
- The default value is 1.

### `crlNodes`

- A _List of Cursor_ specifying the selected nodes to create offset ones.
- The default value is [].

### `crCoord`

- A _Cursor_ specifying the coordinate.
- The default value is None.

## Return Code

- A _List of Cursor_ specifying the created floating nodes.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cube()

# Create offset node
newNode = MeshEdit.CreateNode.Offset(vecOffset=[0.003, 0.0, 0.0], crlNodes=[Node(7)])
JPT.Debugger(newNode) # for checking the return value
```
