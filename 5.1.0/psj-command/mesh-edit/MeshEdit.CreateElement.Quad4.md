---
id: MeshEdit-CreateElement-Quad4
title: MeshEdit.CreateElement.Quad4()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create element
---

## Description

Create element

## Syntax

```psj
MeshEdit.CreateElement.Quad4(iElemType=0, crParentEntity=None, crlNodes=[])
```

Ribbon: <menuselection>MeshEdit &#187; CreateElement &#187; Quad4</menuselection>

## Inputs

### `iElemType`

- An _Integer_ specifying the element type.
- The default value is 0.

### `crParentEntity`

- A _Cursor_ specifying the parent entity.
- The default value is None.

### `crlNodes`

- A _List of Cursor_ specifying the node.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.CreateElement.Quad4(iElemType=0, crParentEntity=None, crlNodes=[])
```
