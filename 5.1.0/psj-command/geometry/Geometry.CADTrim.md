---
id: Geometry-CADTrim
title: Geometry.CADTrim()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: CAD Trim
---

## Description

This method reduces the number of facets (triangle patch shape) for CAD shape. This can be obtained by recursively finding and collapsing adjacent element edges that are at an angle less than a specified angle or at an element edge length less than a specified size.

## Syntax

```psj
Geometry.CADTrim(crlFaces = [], crlParts = [], dTrimSize=1.0, dTrimAngle=15.0)
```

Macro: [GeometryCADTrim](../../macro/geometry/GeometryCADTrim)

Ribbon: <menuselection>Geometry &#187; CAD Trim</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying faces to be trimmed. Either _crlFaces_, or _crlParts_ must be specified.
- The default value is [].

### `crlParts`

- A _List of Cursor_ specifying parts to be trimmed. Either _crlFaces_, or _crlParts_ must be specified.
- The default value is [].

### `dTrimSize`

- A _Double_ specifying the maximum length of element edge.
- The default value is 1.0.

### `dTrimAngle`

- A _Double_ specifying the maximum angle in degrees between element edges.
- The default value is 15.0.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Home.ImportCAD.Parasolid([JPT.GetProgramPath() + "SampleData\\bracket.x_t"],
    dAngleToleranceDegree=7.0, dScale=0.001)

Geometry.CADTrim(crlFaces=[Face(149)], crlParts=[Part(1)], dTrimSize=20.0, dTrimAngle=16.0)
```
