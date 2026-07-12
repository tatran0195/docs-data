---
id: MeshCleanup-Manual3D-CreatePenta
title: MeshCleanup.Manual3D.CreatePenta()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create penta5 element
---

## Description

Create penta5 element

## Syntax

```psj
MeshCleanup.Manual3D.CreatePenta(iParentEntityId=0, crlElems=[])
```

Ribbon: <menuselection>MeshCleanup &#187; Manual3D &#187; CreatePenta</menuselection>

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
MeshCleanup.Manual3D.CreatePenta(iParentEntityId=0, crlElems=[])
```
