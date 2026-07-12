---
id: MeshEdit-RemoveSolidMesh
title: MeshEdit.RemoveSolidMesh()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Remove Solid Mesh
---

## Description

Remove Solid Mesh

## Syntax

```psj
MeshEdit.RemoveSolidMesh(crlParts=[], bConvFirst=False)
```

Ribbon: <menuselection>MeshEdit &#187; RemoveSolidMesh</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the part.
- The default value is [].

### `bConvFirst`

- A _Boolean_ specifying the conv first.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.RemoveSolidMesh(crlParts=[], bConvFirst=False)
```
