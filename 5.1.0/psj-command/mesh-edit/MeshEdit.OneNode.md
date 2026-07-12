---
id: MeshEdit-OneNode
title: MeshEdit.OneNode()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: morphing one node
---

## Description

Morphing one node

## Syntax

```psj
MeshEdit.OneNode(crlNodes=[], crlFaceFixed=[], bOffsetvector=False, crCoord=None, dlOffset=[0, 1, 0], dOffset=1.0, iDistType=0, dDistStrong=10, dDistWeak=20)
```

Ribbon: <menuselection>MeshEdit &#187; OneNode</menuselection>

## Inputs

### `crlNodes`

- A _List of Cursor_ specifying the node.
- The default value is [].

### `crlFaceFixed`

- A _List of Cursor_ specifying the face fixed.
- The default value is [].

### `bOffsetvector`

- A _Boolean_ specifying the offsetvector.
- The default value is False.

### `crCoord`

- A _Cursor_ specifying the coordinate.
- The default value is None.

### `dlOffset`

- A _Double List_ specifying the offset.
- The default value is [0, 1, 0].

### `dOffset`

- A _Double_ specifying the offset.
- The default value is 1.0.

### `iDistType`

- An _Integer_ specifying the dist type.
- The default value is 0.

### `dDistStrong`

- A _Double_ specifying the dist strong.
- The default value is 10.

### `dDistWeak`

- A _Double_ specifying the dist weak.
- The default value is 20.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.OneNode(crlNodes=[], crlFaceFixed=[], bOffsetvector=False, crCoord=None, dlOffset=[0, 1, 0], dOffset=1.0, iDistType=0, dDistStrong=10, dDistWeak=20)
```
