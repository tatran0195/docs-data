---
id: JPT-DItemListToMacroListTCursor
title: JPT.DItemListToMacroListTCursor()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Convert DItemVector object or List of DItem objects to List of Cursor (Macro string type)
---

## Description

Convert _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List_ of _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects to _List of Cursor_ (Macro string type).

## Syntax

```psj
JPT.DItemListToMacroListTCursor(DItemList)
```

## Inputs

### `DItemList`

- A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or a _List_ of _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects to be converted.
- This is a required input.

## Return Code

A _String_ containing all the converted items.

## Sample Code

```psj {11}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get all the existing faces and convert them to List of Cursor (Macro string type)
## Get all Faces from model
listFaces = [JPT.CastToDItem(face) for face in JPT.GetAllFaces()] # List of DItem objects
## Return Faces to a string object, for example, return value = [6:73, 6:74, ...]
JPT.Debugger(JPT.DItemListToMacroListTCursor(listFaces))
```
