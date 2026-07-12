---
id: MeshEdit-MoveNode-Absolute
title: MeshEdit.MoveNode.Absolute()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: move node absolute
---

## Description

Move node absolute

## Syntax

```psj
MeshEdit.MoveNode.Absolute(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, b1stCoord=True, b2ndCoord=True, b3rdCoord=True, crlNodes=[], crCoord=None)
```

Ribbon: <menuselection>MeshEdit &#187; MoveNode &#187; Absolute</menuselection>

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

### `b1stCoord`

- A _B1ST_COORD_ specifying the coordinate.
- The default value is True.

### `b2ndCoord`

- A _B2ND_COORD_ specifying the coordinate.
- The default value is True.

### `b3rdCoord`

- A _B3RD_COORD_ specifying the coordinate.
- The default value is True.

### `crlNodes`

- A _List of Cursor_ specifying the node.
- The default value is [].

### `crCoord`

- A _Cursor_ specifying the coordinate.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.Absolute(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, b1stCoord=True, b2ndCoord=True, b3rdCoord=True, crlNodes=[], crCoord=None)
```
