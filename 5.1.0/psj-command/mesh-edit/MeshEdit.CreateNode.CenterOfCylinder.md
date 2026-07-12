---
id: MeshEdit-CreateNode-CenterOfCylinder
title: MeshEdit.CreateNode.CenterOfCylinder()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a floating node at the center of the cylindrical surface in the longitudinal direction
---

## Description

Create a floating node at the center of the cylindrical surface in the longitudinal direction

## Syntax

```psj
MeshEdit.CreateNode.CenterOfCylinder(...)
```

Macro: [MeshEditCreateNodeCylindCenter](../../macro/mesh-edit/MeshEditCreateNodeCylindCenter)

Ribbon: <menuselection>MeshEdit &#187; CreateNode &#187; CenterOfCylinder</menuselection>

## Inputs

### `iNewNodeID`

- An _Integer_ specifying the new node ID.
- The default value is the maximum node ID + 1.

### `crlFaces`

- A _List of Cursor_ specifying the selected cylindrical faces.
- The default value is [].

## Return Code

- A _List of Cursor_ specifying the created floating nodes.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cylinder()

# Create center node of cylinder
newNode = MeshEdit.CreateNode.CenterOfCylinder(crlFaces=[Face(5)], iNewNodeID=363)
JPT.Debugger(newNode) # for checking the return value
```
