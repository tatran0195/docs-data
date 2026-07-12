---
id: JPT-GetCountByType
title: JPT.GetCountByType()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get total number of entities by inputting DItemType
---

## Description

Get total number of entities by inputting _[DItemType](../data-type/psj-command/DItem-types)_.

## Syntax

```psj
JPT.GetCountByType(DItemType)
```

## Inputs

### `DItemType`

- An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ that wants to count the total number.
- This is a required input.

## Return Code

An _Integer_ specifying the total number of the inputted type.

## Sample Code

```psj {9}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Count the total number of bodies existing on the current Jupiter
iPartCount = JPT.GetCountByType(JPT.DItemType.BODY)
print(iPartCount) # 3
```
