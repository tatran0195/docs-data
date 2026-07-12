---
id: MeshEdit-CreateNode-ProjectToPlane
title: MeshEdit.CreateNode.ProjectToPlane()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a node by projecting the selected node/floating node to the selected face
---

## Description

Create a node by projecting the selected node/floating node to the selected face.

## Syntax

```psj
MeshEdit.CreateNode.ProjectToPlane(...)
```

Macro: [MeshEditCreateNodeProjectNode](../../macro/mesh-edit/MeshEditCreateNodeProjectNode)

Ribbon: <menuselection>MeshEdit &#187; CreateNode &#187; ProjectToPlane</menuselection>

## Inputs

### `crlNodes`

- A _List of Cursor_ specifying the selected nodes.
- The default value is [].

### `crlFaces`

- A _List of Cursor_ specifying the face on which the node will project.
- The default value is [].

:::note Note
This version does not support multi-faces printing, so `crlFaces` should be specified with a single face for each operation.
:::

## Return Code

- A _List of Cursor_ specifying the imprinted nodes.

## Sample Code

```psj {7}
# Prepare model
Geometry.Part.Cube()
Meshing.GridMesh(listGridMesh=[GRID_MESH(crlFace=[Face(26)], crlCorner=[Node(6, 7, 8, 5)], 
                ilMeshCount=[5, 5], iShape=4, bOptimize=True)], bProjectToCad=True)

# Create plan projected node
newNode = MeshEdit.CreateNode.ProjectToPlane(crlNodes=[Node(501)], crlFaces=[Face(25)])
JPT.Debugger(newNode) # for checking the return value
```
