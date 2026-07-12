---
id: JPT-GetMaxIDEntity
title: JPT.GetMaxIDEntity()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get the maximum ID of the inputted DItemType
---

## Description

Get the maximum ID of the inputted DItemType.

## Syntax

```psj
JPT.GetMaxIDEntity(DItemType)
```

## Inputs

### `DItemType`

- An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.
- This is a required input.

## Return Code

A _Integer_ specifying the maximum ID of the inputted DItemType.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the maximum ID of the created parts
iMaxID = JPT.GetMaxIDEntity(JPT.DItemType.BODY)
JPT.Debugger(iMaxID) # 3
```
