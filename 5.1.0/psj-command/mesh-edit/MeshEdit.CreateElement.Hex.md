---
id: MeshEdit-CreateElement-Hex
title: MeshEdit.CreateElement.Hex()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: create hex8 elements
---

## Description

Create hex8 elements

## Syntax

```psj
MeshEdit.CreateElement.Hex(iParentEntityId=0, crlElems=[], iSeprateN=1)
```

Ribbon: <menuselection>MeshEdit &#187; CreateElement &#187; Hex</menuselection>

## Inputs

### `iParentEntityId`

- An _Integer_ specifying the parent entity ID.
- The default value is 0.

### `crlElems`

- A _List of Cursor_ specifying the element.
- The default value is [].

### `iSeprateN`

- An _Integer_ specifying the seprate n.
- The default value is 1.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.CreateElement.Hex(iParentEntityId=0, crlElems=[], iSeprateN=1)
```
