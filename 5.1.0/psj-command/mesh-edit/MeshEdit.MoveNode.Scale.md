---
id: MeshEdit-MoveNode-Scale
title: MeshEdit.MoveNode.Scale()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Move node scale
---

## Description

Move node scale

## Syntax

```psj
MeshEdit.MoveNode.Scale(crlNodes=[], crlNodesOrigin=[], crCoord=None, posDeltaXYZ=[10.0, 10.0, 10.0])
```

Ribbon: <menuselection>MeshEdit &#187; MoveNode &#187; Scale</menuselection>

## Inputs

### `crlNodes`

- A _List of Cursor_ specifying the node.
- The default value is [].

### `crlNodesOrigin`

- A _List of Cursor_ specifying the node original.
- The default value is [].

### `crCoord`

- A _Cursor_ specifying the coordinate.
- The default value is None.

### `posDeltaXYZ`

- A _Position_ specifying the delta x y z.
- The default value is [10.0, 10.0, 10.0].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.Scale(crlNodes=[], crlNodesOrigin=[], crCoord=None, posDeltaXYZ=[10.0, 10.0, 10.0])
```
