---
id: JPT-GetScreenPositionOfEntities
title: JPT.GetScreenPositionOfEntities()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Obtains the position of the specified item in the Main Window.
---

## Description

Obtains the position of the specified item in the Main Window in screen coordinate system [min_x,min_y,max_x,max_y].

## Syntax

```psj
JPT.GetScreenPositionOfEntities(...)
```

## Inputs

### `DItemVector`

- A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object representing the item whose position on the Main Window is to be retrieved.
- This is a required input.

## Return Code

A list of_[int]_ representing the upper left and lower right coordinates of the area. If no item found on the Main Window, it returns a blank list.

## Sample Code

```psj {7}
# Prepare model
Geometry.Part.Cube(iPartColor=13290083)
Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], strName="Cube_2", iPartColor=6149981)
JPT.ViewFitToModel()

# Check screen position of parts in Main Window.
ditem_list=JPT.GetAllByTypeID(JPT.DItemType.BODY)
pos=JPT.GetScreenPositionOfEntities(ditem_list)
JPT.Debugger(pos)
```
