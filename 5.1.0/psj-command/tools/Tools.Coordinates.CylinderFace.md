---
id: Tools-Coordinates-CylinderFace
title: Tools.Coordinates.CylinderFace()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: create Coordinate by Cylinder Face
---

## Description

Create Coordinate by Cylinder Face

## Syntax

```psj
Tools.Coordinates.CylinderFace(strName="CRect1", iCoordType=0, crFace=None)
```

Ribbon: <menuselection>Tools &#187; Coordinates &#187; CylinderFace</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name.
- The default value is "CRect1".

### `iCoordType`

- An _Integer_ specifying the coordinate type.
- The default value is 0.

### `crFace`

- A _Cursor_ specifying the face.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Coordinates.CylinderFace(strName="CRect1", iCoordType=0, crFace=None)
```
