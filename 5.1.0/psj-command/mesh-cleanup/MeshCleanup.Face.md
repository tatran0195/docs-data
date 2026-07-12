---
id: MeshCleanup-Face
title: MeshCleanup.Face()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: change topology face
---

## Description

Change topology face

## Syntax

```psj
MeshCleanup.Face(crlFaces=[], crlParts=[], bCreateNewPart=False)
```

Ribbon: <menuselection>MeshCleanup &#187; Face</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the face.
- The default value is [].

### `crlParts`

- A _List of Cursor_ specifying the part.
- The default value is [].

### `bCreateNewPart`

- A _Boolean_ specifying the create new part.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Face(crlFaces=[], crlParts=[], bCreateNewPart=False)
```
