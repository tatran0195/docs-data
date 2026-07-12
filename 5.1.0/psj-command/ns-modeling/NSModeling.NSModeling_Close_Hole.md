---
id: NSModeling-NSModeling_Close_Hole
title: NSModeling.NSModeling_Close_Hole()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: NSModeling NSModeling_Close_Hole
---

## Description

NSModeling NSModeling_Close_Hole

## Syntax

```psj
NSModeling.NSModeling_Close_Hole(iType, dMaxLength, bMergeFaces, bSetCenterPoint, crlNodes, crlParts)
```

Ribbon: <menuselection>NSModeling &#187; NSModeling_Close_Hole</menuselection>

## Inputs

### `iType`

- An _Integer_ specifying the type.
- This is a required input.

### `dMaxLength`

- A _Double_ specifying the maximum length.
- This is a required input.

### `bMergeFaces`

- A _Boolean_ specifying the merge faces.
- This is a required input.

### `bSetCenterPoint`

- A _Boolean_ specifying the set center point.
- This is a required input.

### `crlNodes`

- A _List of Cursor_ specifying the node.
- This is a required input.

### `crlParts`

- A _List of Cursor_ specifying the part.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
NSModeling.NSModeling_Close_Hole(iType, dMaxLength, bMergeFaces, bSetCenterPoint, crlNodes, crlParts)
```
