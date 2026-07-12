---
id: MeshEdit-CreateNode-CircleCenter
title: MeshEdit.CreateNode.CircleCenter()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a node/floating node at the center of the selected circular edge
---

## Description

Create a node/floating node at the center of the selected circular edge.

## Syntax

```psj
MeshEdit.CreateNode.CircleCenter(...)
```

Macro: [CreateNodeEdgeCenter](../../macro/mesh-edit/CreateNodeEdgeCenter)

Ribbon: <menuselection>MeshEdit &#187; CreateNode &#187; CircleCenter</menuselection>

## Inputs

### `crlEdges`

- A _List of Cursor_ specifying the circular edge.
- This is a required input.

### `iNewNodeID`

- An _Integer_ specifying the new node ID.
- The default value is the maximum node ID + 1.

### `bImprint`

- A _Boolean_ specifying whether to imprint the creating node to face.
- The default value is False.

### `crFace`

- A _Cursor_ specifying the face on which the node will imprint.
- The default value is [].

## Return Code

- A _List of Cursor_ specifying the created floating or imprinted node.

## Sample Code

```psj {7}
# Prepare model
Geometry.Part.Cube()
Geometry.Edge.Circle(veclPositions=[[0.005555555555555556, 0.005555555555555556, 0.01]], 
                                    crlTargetFace=[Face(26)], dOutRadius=1.5)

# Create center node of circle
newNode = MeshEdit.CreateNode.CircleCenter(crlEdges=[Edge(55)], iNewNodeID=540)
JPT.Debugger(newNode) # for checking the return value
```
