---
id: Home-ExportGeometryBDF
title: Home.ExportGeometryBDF()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Export Geometry BDF file.
---

## Description

Export Geometry BDF file.

## Syntax

```psj
Home.ExportGeometryBDF(strFileName, crlParts=[], bBigID=False, bUseUnit=True, bVert=True, bEdge=True, bFace=True, bSolid=True)
```

Ribbon: <menuselection>Home &#187; ExportGeometryBDF</menuselection>

## Inputs

### `strFileName`

- A _String_ specifying the file name.
- This is a required input.

### `crlParts`

- A _List of Cursor_ specifying the part.
- The default value is [].

### `bBigID`

- A _Boolean_ specifying the big ID.
- The default value is False.

### `bUseUnit`

- A _Boolean_ specifying the use unit.
- The default value is _True_.

### `bVert`

- A _Boolean_ specifying the vert.
- The default value is _True_.

### `bEdge`

- A _Boolean_ specifying the edge.
- The default value is _True_.

### `bFace`

- A _Boolean_ specifying the face.
- The default value is _True_.

### `bSolid`

- A _Boolean_ specifying the solid.
- The default value is _True_.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Home.ExportGeometryBDF(strFileName, crlParts=[], bBigID=False, bUseUnit=True, bVert=True, bEdge=True, bFace=True, bSolid=True)
```
