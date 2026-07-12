---
id: MeshEdit-Face
title: MeshEdit.Face()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Make Mesh deformation
---

## Description

Make Mesh deformation

## Syntax

```psj
MeshEdit.Face(crlFaces, crlFaceFixed, iOffsetType=0, crCoord=None, dlOffset=[1.0, 0.0, 0.0], dOffset=0, iDistType=0, dDistStrong=10, dDistWeak=20, iNodeIdPick=-1, dlPickForMacro=[])
```

Ribbon: <menuselection>MeshEdit &#187; Face</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the face.
- This is a required input.

### `crlFaceFixed`

- A _List of Cursor_ specifying the face fixed.
- This is a required input.

### `iOffsetType`

- An _Integer_ specifying the offset type.
- The default value is 0.

### `crCoord`

- A _Cursor_ specifying the coordinate.
- The default value is None.

### `dlOffset`

- A _Double List_ specifying the offset.
- The default value is [1.0, 0.0, 0.0].

### `dOffset`

- A _Double_ specifying the offset.
- The default value is 0.

### `iDistType`

- An _Integer_ specifying the dist type.
- The default value is 0.

### `dDistStrong`

- A _Double_ specifying the dist strong.
- The default value is 10.

### `dDistWeak`

- A _Double_ specifying the dist weak.
- The default value is 20.

### `iNodeIdPick`

- An _Integer_ specifying the node ID pick.
- The default value is -1.

### `dlPickForMacro`

- A _Double List_ specifying the pick for macro.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.Face(crlFaces, crlFaceFixed, iOffsetType=0, crCoord=None, dlOffset=[1.0, 0.0, 0.0], dOffset=0, iDistType=0, dDistStrong=10, dDistWeak=20, iNodeIdPick=-1, dlPickForMacro=[])
```
