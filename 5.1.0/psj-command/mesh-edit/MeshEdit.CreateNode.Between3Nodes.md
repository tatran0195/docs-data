---
id: MeshEdit-CreateNode-Between3Nodes
title: MeshEdit.CreateNode.Between3Nodes()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a center node of 3 selected nodes
---

## Description

Create a center node of 3 selected nodes.

## Syntax

```psj
MeshEdit.CreateNode.Between3Nodes(...)
```

Macro: [MeshEditCreateNodeBetween3Nodes](../../macro/mesh-edit/MeshEditCreateNodeBetween3Nodes)

Ribbon: <menuselection>MeshEdit &#187; CreateNode &#187; Between3Nodes</menuselection>

## Inputs

### `iNewNodeID`

- An _Integer_ specifying the new node ID.
- The default value is the maximum node ID + 1.

### `bImprint`

- A _Boolean_ specifying whether to imprint the creating node to face.
- The default value is False.

### `crlNodes`

- A _List of Cursor_ specifying three target nodes.
- The default value is [].

### `crlFaces`

- A _List of Cursor_ specifying the face on which the node will imprint.
- The default value is [].

:::note Note
This version does not support multi-faces printing, so `crlFaces` should be specified with a single face for each operation.
:::

## Return Code

- A _Cursor_ specifying the created floating or imprinted node.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cube()

# Create a node at the center of three nodes
newNode = MeshEdit.CreateNode.Between3Nodes(iNewNodeID=490, crlNodes=[Node(8, 7, 5)])
JPT.Debugger(newNode) # for checking the return value
```
