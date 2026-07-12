---
id: MeshEdit-AdjustOrientation
title: MeshEdit.AdjustOrientation()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Adjust the orientation (normal direction) of parts, faces, or elements.
---

## Description

Adjust the orientation (normal direction) of parts, faces, or elements.

## Syntax

```psj
MeshEdit.AdjustOrientation(...)
```

Macro: [GeomEditAdjustOrientation](../../macro/mesh-edit/GeomEditAdjustOrientation)

Ribbon: <menuselection>MeshEdit &#187; AdjustOrientation</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the target parts.
- The default value is [].

### `crlFaces`

- A _List of Cursor_ specifying the target faces.
- The default value is [].

### `crlElems`

- A _List of Cursor_ specifying the target elements.
- The default value is [].

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
MainWindow.RightClick.FlipElement(crlTargets=[Face(26)])
MainWindow.RightClick.FlipElement(crlTargets=[Elem(699, 702, 684, 701)])

# Adjust orientation
MeshEdit.AdjustOrientation(crlParts=[Part(1)], crlElems=[Elem(322)])

```
