---
id: Home-ExportSTL
title: Home.ExportSTL()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: export stl
---

## Description

Export stl

## Syntax

```psj
Home.ExportSTL(strFile="", crlParts=[], dScale=1, bBinaryFormat=False)
```

Ribbon: <menuselection>Home &#187; ExportSTL</menuselection>

## Inputs

### `strFile`

- A _String_ specifying the file.
- The default value is "".

### `crlParts`

- A _List of Cursor_ specifying the part.
- The default value is [].

### `dScale`

- A _Double_ specifying the scale.
- The default value is 1.

### `bBinaryFormat`

- A _Boolean_ specifying the filter index.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Home.ExportSTL(strFile="", crlParts=[], dScale=1, bBinaryFormat=False)
```
