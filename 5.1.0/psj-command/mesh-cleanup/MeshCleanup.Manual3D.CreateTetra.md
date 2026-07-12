---
id: MeshCleanup-Manual3D-CreateTetra
title: MeshCleanup.Manual3D.CreateTetra()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: create element Tet
---

## Description

Create element Tet

## Syntax

```psj
MeshCleanup.Manual3D.CreateTetra(iParentEntityId=0, crlNodes=[], crlElems=[])
```

Ribbon: <menuselection>MeshCleanup &#187; Manual3D &#187; CreateTetra</menuselection>

## Inputs

### `iParentEntityId`

- An _Integer_ specifying the parent entity ID.
- The default value is 0.

### `crlNodes`

- A _List of Cursor_ specifying the node.
- The default value is [].

### `crlElems`

- A _List of Cursor_ specifying the element.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual3D.CreateTetra(iParentEntityId=0, crlNodes=[], crlElems=[])
```
