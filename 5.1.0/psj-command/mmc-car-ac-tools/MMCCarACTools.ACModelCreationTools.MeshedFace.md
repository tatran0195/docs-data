---
id: MMCCarACTools-ACModelCreationTools-MeshedFace
title: MMCCarACTools.ACModelCreationTools.MeshedFace()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

## Syntax

```psj
MMCCarACTools.ACModelCreationTools.MeshedFace(crlItem1, crlItem2, crlItem3, crlParts, iType, dMeshSise, bMergeTol, dTol, bCreatePart)
```

Ribbon: <menuselection>MMCCarACTools &#187; ACModelCreationTools &#187; MeshedFace</menuselection>

## Inputs

### `crlItem1`

- A _List of Cursor_ specifying the item1.
- This is a required input.

### `crlItem2`

- A _List of Cursor_ specifying the item2.
- This is a required input.

### `crlItem3`

- A _List of Cursor_ specifying the item3.
- This is a required input.

### `crlParts`

- A _List of Cursor_ specifying the part.
- This is a required input.

### `iType`

- An _Integer_ specifying the type.
- This is a required input.

### `dMeshSise`

- A _Double_ specifying the mesh sise.
- This is a required input.

### `bMergeTol`

- A _Boolean_ specifying the merge tolerance.
- This is a required input.

### `dTol`

- A _Double_ specifying the tolerance.
- This is a required input.

### `bCreatePart`

- A _Boolean_ specifying the create part.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MMCCarACTools.ACModelCreationTools.MeshedFace(crlItem1, crlItem2, crlItem3, crlParts, iType, dMeshSise, bMergeTol, dTol, bCreatePart)
```
