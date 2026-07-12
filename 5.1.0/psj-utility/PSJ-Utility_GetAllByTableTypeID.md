---
id: JPT-GetAllByTableTypeID
title: JPT.GetAllByTableTypeID()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get all the information of all entities by inputting DTableType
---

## Description

Get all the information of all entities by inputting _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_.

## Syntax

```psj
JPT.GetAllByTableTypeID(DTableType)
```

## Inputs

### `DTableType`

- An _Enum_ specifying _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_ of the target entities.
- This is a required input.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of all the found entities by inputted ID.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Select all parts and store their information to a list of DItem
listDTableParts = JPT.GetAllByTableTypeID(JPT.DTableType.DTABLE_BODY) # ID = 5
JPT.Debugger(listDTableParts)

```
