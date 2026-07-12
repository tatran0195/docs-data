---
id: Home-ImportCAD-TechnoStarGeometry
title: Home.ImportCAD.TechnoStarGeometry()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import Geometry bdf file
---

## Description

Import Geometry by bdf file

## Syntax

```psj
Home.ImportCAD.TechnoStarGeometry(...)
```

Macro: [ImportGeomBDF](../../macro/home/ImportGeomBDF)

Ribbon: <menuselection>Home &#187; ImportCAD &#187; TechnoStarGeometry</menuselection>

## Inputs

### `strlPath`

- A _List of String_ specifying the path.
- The default value is [].

### `bUseUnit`

- A _Boolean_ specifying the use unit.
- The default value is _True_.

## Return Code

A _String_ of 1 if successed, or 0 if failed.

## Sample Code

```psj {1}
Home.ImportCAD.TechnoStarGeometry(strlPath=[], bUseUnit=True)
```
