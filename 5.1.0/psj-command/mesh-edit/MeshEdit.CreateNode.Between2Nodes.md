---
id: MeshEdit-CreateNode-Between2Nodes
title: MeshEdit.CreateNode.Between2Nodes()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create node between two selected nodes
---

## Description

Create node between two selected nodes.

## Syntax

```psj
MeshEdit.CreateNode.Between2Nodes(...)
```

Macro: [MeshEditCreateNodeBetween2Nodes](../../macro/mesh-edit/MeshEditCreateNodeBetween2Nodes)

Ribbon: <menuselection>MeshEdit &#187; CreateNode &#187; Between2Nodes</menuselection>

## Inputs

### `iNewNodeID`

- An _Integer_ specifying the new node ID.
- The default value is the maximum node ID + 1.

### `iNumberOfNodes`

- An _Integer_ specifying the number of new nodes to be created between two target nodes.
- The default value is 0.

### `bImprint`

- A _Boolean_ specifying whether to imprint the creating node to face.
- The default value is False.

### `crlNodes`

- A _List of Cursor_ specifying two target nodes.
- The default value is [].

### `crlFaces`

- A _List of Cursor_ specifying the face on which the node will imprint.
- The default value is [].

:::note Note
This version does not support multi-faces printing, so `crlFaces` should be specified with a single face for each operation.
:::

## Return Code

- A _List of Cursor_ specifying the created floating or imprinted nodes.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cube()

# Create a node between two nodes
newNodes = MeshEdit.CreateNode.Between2Nodes(iNewNodeID=490, iNumberofNodes=2, crlNodes=[Node(6, 7)])
JPT.Debugger(newNodes) # for checking the return value
```
