---
id: MidPlaneEdit-Manual-MidByPair
title: MidPlaneEdit.Manual.MidByPair()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Midplane Manual MidByPair
---

## Description

Midplane Manual MidByPair

## Syntax

```psj
MidPlaneEdit.Manual.MidByPair(crlBaseFaces, crlPairFaces, crlRefFaces, crPart, bMergeFaces, bExtendFaces, bHideFaces, dExtendTol, dMergeEdgesAngle, dStitchFaces)
```

Ribbon: <menuselection>MidPlaneEdit &#187; Manual &#187; MidByPair</menuselection>

## Inputs

### `crlBaseFaces`

- A _List of Cursor_ specifying the base faces.
- This is a required input.

### `crlPairFaces`

- A _List of Cursor_ specifying the pair faces.
- This is a required input.

### `crlRefFaces`

- A _List of Cursor_ specifying the reference faces.
- This is a required input.

### `crPart`

- A _Cursor_ specifying the part.
- This is a required input.

### `bMergeFaces`

- A _Boolean_ specifying the merge faces.
- This is a required input.

### `bExtendFaces`

- A _Boolean_ specifying the extend faces.
- This is a required input.

### `bHideFaces`

- A _Boolean_ specifying the hide faces.
- This is a required input.

### `dExtendTol`

- A _Double_ specifying the extend tolerance.
- This is a required input.

### `dMergeEdgesAngle`

- A _Double_ specifying the merge edges angle.
- This is a required input.

### `dStitchFaces`

- A _Double_ specifying the stitch faces.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.Manual.MidByPair(crlBaseFaces, crlPairFaces, crlRefFaces, crPart, bMergeFaces, bExtendFaces, bHideFaces, dExtendTol, dMergeEdgesAngle, dStitchFaces)
```
