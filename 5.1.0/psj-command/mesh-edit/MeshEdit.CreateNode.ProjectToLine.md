---
id: MeshEdit-CreateNode-ProjectToLine
title: MeshEdit.CreateNode.ProjectToLine()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a node by projecting the third selected node/floating node to the shortest distance of the two previously selected nodes/floating nodes
---

## Description

Create a node by projecting the third selected node/floating node to the shortest distance of the two previously selected nodes/floating nodes.

## Syntax

```psj
MeshEdit.CreateNode.ProjectToLine(crlTa)
```

Macro: [CreateNodeProjectToLine](../../macro/mesh-edit/CreateNodeProjectToLine)

Ribbon: <menuselection>MeshEdit &#187; CreateNode &#187; ProjectToLine</menuselection>

## Inputs

### `crlNodes`

- A _List of Cursor_ specifying the selected nodes.
- This is a required input.

## Return Code

- A _Cursor_ specifying the created floating node.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cube()

# Create line projected node
newNode = MeshEdit.CreateNode.ProjectToLine(crlNodes=[Node(7, 8, 76)])
JPT.Debugger(newNode) # for checking the return value
```
