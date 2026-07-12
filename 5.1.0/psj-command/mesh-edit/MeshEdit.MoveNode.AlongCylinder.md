---
id: MeshEdit-MoveNode-AlongCylinder
title: MeshEdit.MoveNode.AlongCylinder()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Move node along cylinder surface
---

## Description

Move node along cylinder surface

## Syntax

```psj
MeshEdit.MoveNode.AlongCylinder(crlFaces=[], crlNodes=[], dIrX=0, dIrY=0, dIrZ=0, dCircleX=0, dCircleY=0, dCircleZ=0, dRadius=0, dHeight=0)
```

Ribbon: <menuselection>MeshEdit &#187; MoveNode &#187; AlongCylinder</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the face.
- The default value is [].

### `crlNodes`

- A _List of Cursor_ specifying the node.
- The default value is [].

### `dIrX`

- A _Double_ specifying the direction x.
- The default value is 0.

### `dIrY`

- A _Double_ specifying the direction y.
- The default value is 0.

### `dIrZ`

- A _Double_ specifying the direction z.
- The default value is 0.

### `dCircleX`

- A _Double_ specifying the circle x.
- The default value is 0.

### `dCircleY`

- A _Double_ specifying the circle y.
- The default value is 0.

### `dCircleZ`

- A _Double_ specifying the circle z.
- The default value is 0.

### `dRadius`

- A _Double_ specifying the radius.
- The default value is 0.

### `dHeight`

- A _Double_ specifying the height.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.AlongCylinder(crlFaces=[], crlNodes=[], dIrX=0, dIrY=0, dIrZ=0, dCircleX=0, dCircleY=0, dCircleZ=0, dRadius=0, dHeight=0)
```
