---
id: MeshEdit-CreateNode-IntersectionNode
title: MeshEdit.CreateNode.IntersectionNode()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create floating nodes at the intersection of a part or face with edges or a line segment defined by 2 nodes
---

## Description

Create floating nodes at the intersection of a part or face with edges or a line segment defined by 2 nodes

## Syntax

```psj
MeshEdit.CreateNode.IntersectionNode(...)
```

Macro: [CreateNodeIntersectionNode](../../macro/mesh-edit/CreateNodeIntersectionNode)

Ribbon: <menuselection>MeshEdit &#187; CreateNode &#187; IntersectionNode</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the face.
- This is a required input.

### `crlParts`

- A _List of Cursor_ specifying the part.
- This is a required input.

### `crEdge`

- A _Cursor_ specifying the edge.
- This is a required input.

### `crlNodes`

- A _List of Cursor_ specifying two nodes to make line.
- This is a required input.

## Return Code

- A _List of Cursor_ specifying the created floating nodes.

## Sample Code

```psj {7-8}
# Prepare model
Geometry.Part.Cube(iPartColor=7697908)
MeshEdit.CreateNode.Offset(vecOffset=[0.003, 0.0, 0.0], crlNodes=[Node(324)])
MeshEdit.CreateNode.Offset(vecOffset=[-0.003, 0.0, 0.0], crlNodes=[Node(259)])

# Create Intersection Node
newNode = MeshEdit.CreateNode.IntersectionNode(crlFaces=[Face(24, 23)], crlParts=[], crlEdges=[], 
                                                crlNodes=[Node(489, 490)])
JPT.Debugger(newNode) # for checking the return value
```
