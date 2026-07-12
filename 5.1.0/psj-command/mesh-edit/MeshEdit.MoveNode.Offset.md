---
id: MeshEdit-MoveNode-Offset
title: MeshEdit.MoveNode.Offset()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: MeshEdit MoveNode MoveNodeOffset
---

## Description

MeshEdit MoveNode MoveNodeOffset

## Syntax

```psj
MeshEdit.MoveNode.Offset(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, crCoord=None, crlNodes=[])
```

Ribbon: <menuselection>MeshEdit &#187; MoveNode &#187; Offset</menuselection>

## Inputs

### `dDeltaX`

- A _Double_ specifying the delta x.
- The default value is 0.0.

### `dDeltaY`

- A _Double_ specifying the delta y.
- The default value is 0.0.

### `dDeltaZ`

- A _Double_ specifying the delta z.
- The default value is 0.0.

### `crCoord`

- A _Cursor_ specifying the coordinate.
- The default value is None.

### `crlNodes`

- A _List of Cursor_ specifying the node.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.Offset(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, crCoord=None, crlNodes=[])
```
