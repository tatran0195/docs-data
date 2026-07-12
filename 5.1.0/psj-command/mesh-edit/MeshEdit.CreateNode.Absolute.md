---
id: MeshEdit-CreateNode-Absolute
title: MeshEdit.CreateNode.Absolute()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a node by inputting the direct coordinate value
---

## Description

Create a node by inputting the direct coordinate value.

## Syntax

```psj
MeshEdit.CreateNode.Absolute(...)
```

Macro: [CreateNode](../../macro/mesh-edit/CreateNode)

Ribbon: <menuselection>MeshEdit &#187; CreateNode &#187; Absolute</menuselection>

## Inputs

### `dlCoordinate`

- A _List of Double_ specifying the node coordinate.
- The default value is [].

### `iNewNodeID`

- An _Integer_ specifying the new node ID.
- The default value is the maximum node ID + 1.

## Return Code

- A _Cursor_ specifying the created floating node.

## Sample Code

```psj {2}
# Create an absolute node
newNode = MeshEdit.CreateNode.Absolute(dlCoordinate=[0.01, 0.0, 0.0], iNewNodeID=489)
JPT.Debugger(newNode) # for checking the return value
```
