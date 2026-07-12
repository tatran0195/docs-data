---
id: MeshEdit-FaceImprint
title: MeshEdit.FaceImprint()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: import Nastran bdf file
---

## Description

Import Nastran bdf file

## Syntax

```psj
MeshEdit.FaceImprint(crlFaces=[], bMeshCopy=False)
```

Ribbon: <menuselection>MeshEdit &#187; FaceImprint</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the faces.
- The default value is [].

### `bMeshCopy`

- A _Boolean_ specifying the mesh copy.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.FaceImprint(crlFaces=[], bMeshCopy=False)
```
