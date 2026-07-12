---
id: JPT-GetCenterOfEntities
title: JPT.GetCenterOfEntities()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get center coordinate of selected entities
---

## Description

Get center coordinate of selected entities.

## Syntax

```psj
JPT.GetCenterOfEntities(DItemVector)
```

## Inputs

### `DItemVector`

- A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects specifying the targets to get center coordinates.
- This is a required input.

## Return Code

A _[DoubleVector](../data-type/psj-utility/pre-utility/built-in-types/DoubleVector)_ object or _List of Double_ value containing the coordinate values \[x, y, z\] of the center of the inputted entities.

## Sample Code

```psj {9}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the center coordinate of the inputted entities
listParts = JPT.GetAllByTypeID(3)
JPT.Debugger(JPT.GetCenterOfEntities(listParts))
```
