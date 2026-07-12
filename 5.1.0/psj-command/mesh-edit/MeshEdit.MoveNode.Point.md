---
id: MeshEdit-MoveNode-Point
title: MeshEdit.MoveNode.Point()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Move node(s) to an Face(Edge) Point position
---

## Description

Move node(s) to an Face(Edge) Point position

## Syntax

```psj
MeshEdit.MoveNode.Point(dX=0.0, dY=0.0, dZ=0.0, ilNodeList=[])
```

Ribbon: <menuselection>MeshEdit &#187; MoveNode &#187; Point</menuselection>

## Inputs

### `dX`

- A _Double_ specifying the x.
- The default value is 0.0.

### `dY`

- A _Double_ specifying the y.
- The default value is 0.0.

### `dZ`

- A _Double_ specifying the z.
- The default value is 0.0.

### `ilNodeList`

- A _List of Integer_ specifying the node list.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.Point(dX=0.0, dY=0.0, dZ=0.0, ilNodeList=[])
```
