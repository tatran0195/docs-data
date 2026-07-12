---
id: MeshEdit-RibThickness
title: MeshEdit.RibThickness()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Mesh Edit Morphing Rib Thickness
---

## Description

Mesh Edit Morphing Rib Thickness

## Syntax

```psj
MeshEdit.RibThickness(crlFaceMove=[], crlFaceFixed=[], dMove=3.00, dDistStrong=10.00, dDistWeak=20.00)
```

Ribbon: <menuselection>MeshEdit &#187; RibThickness</menuselection>

## Inputs

### `crlFaceMove`

- A _List of Cursor_ specifying the face move.
- The default value is [].

### `crlFaceFixed`

- A _List of Cursor_ specifying the face fixed.
- The default value is [].

### `dMove`

- A _Double_ specifying the move.
- The default value is 3.00.

### `dDistStrong`

- A _Double_ specifying the dist strong.
- The default value is 10.00.

### `dDistWeak`

- A _Double_ specifying the dist weak.
- The default value is 20.00.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.RibThickness(crlFaceMove=[], crlFaceFixed=[], dMove=3.00, dDistStrong=10.00, dDistWeak=20.00)
```
