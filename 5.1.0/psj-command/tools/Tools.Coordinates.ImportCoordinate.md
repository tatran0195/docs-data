---
id: Tools-Coordinates-ImportCoordinate
title: Tools.Coordinates.ImportCoordinate()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import local coordinates as Nastran BDF or ADVC ADX format..
---

## Description

Import local coordinates as Nastran BDF or ADVC ADX format.

## Syntax

```psj
Tools.Coordinates.ImportCoordinate(...)
```

Macro: 

Ribbon: <menuselection>Tools &#187; Coordinates &#187; Import Coordinate</menuselection>

## Inputs

### `strlPath`

- A _List of String_ specifying path to export file.
- The default value is "".

### `crlCS`

- A _List of Cursor_ specifying local coordinates.
- The default value is _None_.

## Return Code

A _Boolean_ specifying succeeded or not.

## Sample Code

```psj {28,29}
#Prepare model
Geometry.Part.Cube(iPartColor=6409934)

#Prepare coordinates
lcs1=Tools.Coordinates.ThreeNode(
    strName="CRect_1", 
    crlNodes=[Node(7, 6, 445)])

lcs2=Tools.Coordinates.ThreeNode(
    strName="CRect_2", 
    crlNodes=[Node(310, 317, 336)])

#Export coordinates

import os 
temp_path=JPT.GetAppPathInfo(JPT.PathType.TEMP_PATH)

Tools.Coordinates.ExportCoordinate(
    strlPath=os.path.join(temp_path,'exp-lcs.bdf'), 
    crlCS=[lcs1,lcs2])

#Delete the created coordinates

JPT.Exec(f"DeleteItem(0, [{lcs1},{lcs2}], [], [], 1)")

#Recreate coordinates by import coordinates exported before

Tools.Coordinates.ImportCoordinate(
    strlPath=os.path.join(temp_path,'exp-lcs.bdf'))
```
