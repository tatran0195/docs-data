---
id: JPT-GetSharedElements
title: JPT.GetSharedElements()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get all information of the shared elements
---

## Description

Get all information of the shared elements.

## Syntax

```psj
JPT.GetSharedElements(DItemVector)
```

## Inputs

### `DItemVector`

- A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects to get the shared elements.
- This is a required input.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of all the shared elements.

## Sample Code

```psj {14}
# Prepare model
Geometry.Part.Cube(iPartColor=6217822)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6908379)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=7138924)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=15753968)
JPT.ViewFitToModel()

# Create shared faces
JPT.Exec('AssembleFaceMatingStep([], [], [3:1, 3:2, 3:3, 3:4], 1e-05)')
JPT.Exec('AssembleFaceEx([49, 24, 50, 75, 101, 76], 1e-05, 0, 0)')

# Get the information of all shared elements
listParts = JPT.GetAllByTypeID(JPT.DItemType.BODY)
listSharedElems = JPT.GetSharedElements(listParts)
JPT.Debugger(listSharedElems)
```
