---
id: JPT-SelectionByType
title: JPT.SelectionByType()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Select all the existing entities by type
---

## Description

Select all the existing entities by type.

## Syntax

```psj
JPT.SelectionByType(DItemType, BoolType)
```

## Inputs

### `DItemType`

- An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.
- This is a required input.

### `BoolType`

- An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the selection mode:
  - _True_: Select the inputted entity with its ID.
  - _False_: Deselect the inputted entity with its ID.
- This is a required input.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {6}
# Prepare model
Geometry.Part.Cube(iPartColor=6974164)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7599987)

# Select all the created parts
JPT.SelectionByType(JPT.DItemType.BODY, JPT.BoolType.TRUE_VAL)
```
