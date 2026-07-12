---
id: JPT-SelectionByID
title: JPT.SelectionByID()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Select an entity by using its ID
---

## Description

Select an entity by using its ID.

## Syntax

```psj
JPT.SelectionByID(DItemType, entityID, BoolType)
```

## Inputs

### `DItemType`

- An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.
- This is a required input.

### `entityID`

- An _Integer_ specifying ID of the selecting entity.
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

# Select face with ID = 51
JPT.SelectionByID(JPT.DItemType.FACE, 51, JPT.BoolType.TRUE_VAL)
```
