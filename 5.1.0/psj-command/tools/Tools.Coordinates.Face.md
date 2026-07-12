---
id: Tools-Coordinates-Face
title: Tools.Coordinates.Face()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: create Coordinate by Face
---

## Description

Create Coordinate by Face

## Syntax

```psj
Tools.Coordinates.Face(strName="CRect1", iCoordType=0, iOrder=0, veclPoint=[], crlNodes=[], crItem=None, crRefCoord=None, crEdit=None)
```

Ribbon: <menuselection>Tools &#187; Coordinates &#187; Face</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name.
- The default value is "CRect1".

### `iCoordType`

- An _Integer_ specifying the coordinate type.
- The default value is 0.

### `iOrder`

- An _Integer_ specifying the order.
- The default value is 0.

### `veclPoint`

- A _Vector List_ specifying the point.
- The default value is [].

### `crlNodes`

- A _List of Cursor_ specifying the node.
- The default value is [].

### `crItem`

- A _Cursor_ specifying the item.
- The default value is None.

### `crRefCoord`

- A _Cursor_ specifying the reference coordinate.
- The default value is None.

### `crEdit`

- A _Cursor_ specifying the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Coordinates.Face(strName="CRect1", iCoordType=0, iOrder=0, veclPoint=[], crlNodes=[], crItem=None, crRefCoord=None, crEdit=None)
```
