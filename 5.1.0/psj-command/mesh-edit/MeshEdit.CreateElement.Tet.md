---
id: MeshEdit-CreateElement-Tet
title: MeshEdit.CreateElement.Tet()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: create element Tet
---

## Description

Create element Tet

## Syntax

```psj
MeshEdit.CreateElement.Tet(iParentEntityId=0, crlNodes=[], crlElems=[])
```

Ribbon: <menuselection>MeshEdit &#187; CreateElement &#187; Tet</menuselection>

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
MeshEdit.CreateElement.Tet(iParentEntityId=0, crlNodes=[], crlElems=[])
```
