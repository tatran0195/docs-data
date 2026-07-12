---
id: MidPlaneEdit-Face-FaceExtendtoFace
title: MidPlaneEdit.Face.FaceExtendtoFace()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: add face by face extend to face
---

## Description

Add face by face extend to face

## Syntax

```psj
MidPlaneEdit.Face.FaceExtendtoFace(crlExtFaces, crlRefFaces, bMergeFace, bMergeEdge, dMergeEdgeAngle)
```

Ribbon: <menuselection>MidPlaneEdit &#187; Face &#187; FaceExtendtoFace</menuselection>

## Inputs

### `crlExtFaces`

- A _List of Cursor_ specifying the extend faces.
- This is a required input.

### `crlRefFaces`

- A _List of Cursor_ specifying the reference faces.
- This is a required input.

### `bMergeFace`

- A _Boolean_ specifying the merge face.
- This is a required input.

### `bMergeEdge`

- A _Boolean_ specifying the merge edge.
- This is a required input.

### `dMergeEdgeAngle`

- A _Double_ specifying the merge edge angle.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.Face.FaceExtendtoFace(crlExtFaces, crlRefFaces, bMergeFace, bMergeEdge, dMergeEdgeAngle)
```
