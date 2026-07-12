---
id: MeshEdit-CreateNode-CenterOfSphere
title: MeshEdit.CreateNode.CenterOfSphere()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create node at the center sphere or the center of curvature of 4 nodes.
---

## Description

Create node at the center sphere or the center of curvature of 4 nodes.

## Syntax

```psj
MeshEdit.CreateNode.CenterOfSphere(...)
```

Macro: [MeshEditCreateNodeSphereCenter](../../macro/mesh-edit/MeshEditCreateNodeSphereCenter)

Ribbon: <menuselection>MeshEdit &#187; CreateNode &#187; CenterOfSphere</menuselection>

## Inputs

### `iNewNodeID`

- An _Integer_ specifying the new node ID.
- The default value is the maximum node ID + 1.

### `crlTargets`

- A _List of Cursor_ specifying the sphere face or 4 nodes.
- The default value is [].

## Return Code

- A _Cursor_ specifying the created floating node.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Sphere(iPartColor=6409934)

# Create center node of sphere
newNode = MeshEdit.CreateNode.CenterOfSphere(crlTargets=[Face(1)], iNewNodeID=383)
JPT.Debugger(newNode) # for checking the return value
```
