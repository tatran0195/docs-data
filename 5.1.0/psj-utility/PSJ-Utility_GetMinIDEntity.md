---
id: JPT-GetMinIDEntity
title: JPT.GetMinIDEntity()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get the minimum ID of the inputted DItemType
---

## Description

Get the minimum ID of the inputted DItemType.

## Syntax

```psj
JPT.GetMinIDEntity(DItemType)
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

# Get the minimum ID of the created parts
iMinID = JPT.GetMinIDEntity(JPT.DItemType.BODY)
JPT.Debugger(iMinID) # 1
```
