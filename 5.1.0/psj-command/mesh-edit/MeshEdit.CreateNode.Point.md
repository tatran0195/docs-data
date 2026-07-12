---
id: MeshEdit-CreateNode-Point
title: MeshEdit.CreateNode.Point()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a node by referring to the coordinate value of the arbitrary point
---

## Description

Create a node by referring to the coordinate value of the arbitrary point.

## Syntax

```psj
MeshEdit.CreateNode.Point(...)
```

Macro: [MeshEditCreateNodePoint](../../macro/mesh-edit/MeshEditCreateNodePoint)

Ribbon: <menuselection>MeshEdit &#187; CreateNode &#187; Point</menuselection>

## Inputs

### `iNewNodeID`

- An _Integer_ specifying the new node ID.
- The default value is the maximum node ID + 1.

### `posPoint`

- A _List of Double_ specifying the coordinates of the specified point.
- The default value is [0,0,0].

### `bImprint`

- A _Boolean_ specifying to imprint node to face.
- The default value is True.

### `crTarget`

- A _Cursor_ specifying the target on which to create the node. The target can be a face or an edge.
- The default value is None.

## Return Code

- A _Cursor_ specifying the created floating or imprinted node.

## Sample Code

```psj {5-7}
# Prepare model
Geometry.Part.Cube()

# Create node at point
newNode = MeshEdit.CreateNode.Point(iNewNodeID=490, 
                                    posPoint=[0.008331683464348316, 0.003326606005430222, 0.009999999776482582], 
                                    bImprint=False, crTarget=Face(26))
JPT.Debugger(newNode) # for checking the return value
```
