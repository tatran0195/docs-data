---
id: MeshCleanup-Manual3D-CreateHex
title: MeshCleanup.Manual3D.CreateHex()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: create hex8 elements
---

## Description

Create hex8 elements

## Syntax

```psj
MeshCleanup.Manual3D.CreateHex(iParentEntityId=0, crlElems=[], iSeprateN=1)
```

Ribbon: <menuselection>MeshCleanup &#187; Manual3D &#187; CreateHex</menuselection>

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
MeshCleanup.Manual3D.CreateHex(iParentEntityId=0, crlElems=[], iSeprateN=1)
```
