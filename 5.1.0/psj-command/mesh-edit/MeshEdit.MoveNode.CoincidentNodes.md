---
id: MeshEdit-MoveNode-CoincidentNodes
title: MeshEdit.MoveNode.CoincidentNodes()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Coincident Nodes
---

## Description

Coincident Nodes

## Syntax

```psj
MeshEdit.MoveNode.CoincidentNodes(crlNodes=[], dTol=0.01, bDesOrder=False)
```

Ribbon: <menuselection>MeshEdit &#187; MoveNode &#187; CoincidentNodes</menuselection>

## Inputs

### `crlNodes`

- A _List of Cursor_ specifying the node.
- The default value is [].

### `dTol`

- A _Double_ specifying the tolerance.
- The default value is 0.01.

### `bDesOrder`

- A _Boolean_ specifying the des order.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.CoincidentNodes(crlNodes=[], dTol=0.01, bDesOrder=False)
```
