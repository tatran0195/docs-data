---
id: MeshEdit-CreateNode-Node
title: MeshEdit.CreateNode.Node()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a node by referring to the coordinate value of the existing node
---

## Description

Create a node by referring to the coordinate value of the existing node.

## Syntax

```psj
MeshEdit.CreateNode.Node(...)
```

Macro: [MeshEditCreateNodeAtNode](../../macro/mesh-edit/MeshEditCreateNodeAtNode)

Ribbon: <menuselection>MeshEdit &#187; CreateNode &#187; Node</menuselection>

## Inputs

### `iNewNodeID`

- An _Integer_ specifying the new node ID.
- The default value is the maximum node ID + 1.

### `crTarget`

- A _Cursor_ specifying the target on which to create the node. The target can be a face or an edge.
- The default value is None.

## Return Code

- A _Cursor_ specifying the created floating node.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cube()

# Create node at node
newNode = MeshEdit.CreateNode.Node(iNewNodeId=489, crTarget=Node(480))
JPT.Debugger(newNode) # for checking the return value
```
