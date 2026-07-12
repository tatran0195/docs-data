---
id: MeshEdit-CreateElement-Penta
title: MeshEdit.CreateElement.Penta()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create penta element
---

## Description

Create penta element

## Syntax

```psj
MeshEdit.CreateElement.Penta(iParentEntityId=0, crlElems=[])
```

Ribbon: <menuselection>MeshEdit &#187; CreateElement &#187; Penta</menuselection>

## Inputs

### `iParentEntityId`

- An _Integer_ specifying the parent entity ID.
- The default value is 0.

### `crlElems`

- A _List of Cursor_ specifying the element.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.CreateElement.Penta(iParentEntityId=0, crlElems=[])
```
