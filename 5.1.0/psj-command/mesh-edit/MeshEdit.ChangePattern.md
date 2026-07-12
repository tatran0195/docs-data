---
id: MeshEdit-ChangePattern
title: MeshEdit.ChangePattern()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Change the mesh pattern of faces.
---

## Description

Change the mesh pattern of faces.

## Syntax

```psj
MeshEdit.ChangePattern(...)
```

Macro: [GeomEditChangePattern](../../macro/mesh-edit/GeomEditChangePattern)

Ribbon: <menuselection>MeshEdit &#187; ChangePattern</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the target faces.
- The default value is [].

### `iPatternType`

- An _Integer_ specifying the pattern type.
  - 0: Standard
  - 1: Union Jack
- The default value is 0.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj
# Prepare model and view
Geometry.Part.Cube(iPartColor=6409934)
JPT.Exec('ViewShowMesh(1)')
JPT.ViewFitToModel()

# Change pattern
MeshEdit.ChangePattern(crlFaces=[Face(22)], iPatternType=1)
```
