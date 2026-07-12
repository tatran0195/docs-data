---
id: JPT-SelectionByIDs
title: JPT.SelectionByIDs()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Select entities by using their list of IDs
---

## Description

Select entities by using their list of IDs.

## Syntax

```psj
JPT.SelectionByIDs(DItemType, entityIDs, BoolType)
```

## Inputs

### `DItemType`

- An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.
- This is a required input.

### `entityIDs`

- An _List of Integer_ specifying the list of ID of the selecting entites.
- This is a required input.

### `BoolType`

- An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the selection mode:
  - _True_: Select the inputted entity with its ID.
  - _False_: Deselect the inputted entity with its ID.
- This is a required input.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {7}
# Prepare model
Geometry.Part.Cube(iPartColor=6974164)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7599987)
JPT.ViewFitToModel()

# Select face with IDs = [50, 51, 52]
JPT.SelectionByIDs(JPT.DItemType.FACE, [50, 51, 52], JPT.BoolType.TRUE_VAL)
```
