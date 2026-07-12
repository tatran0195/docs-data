---
id: JPT-ShowHideEntitiesByID
title: JPT.ShowHideEntitiesByID()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Show or Hide an entity by inputted its ID
---

## Description

Show or Hide an entity by inputted its ID.

## Syntax

```psj
JPT.ShowHideEntitiesByID(DTableType, itemID, BoolType)
```

## Inputs

### `DTableType`

- An _Enum_ specifying the _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_ of the entities which will be shown/hidden.
- This is a required input.

### `itemID`

- An _Integer_ specifying the ID of the target entity.
- This is a required input.

### `BoolType`

- An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the display mode:
  - _False_: Hide the inputted part.
  - _True_: Show the inputted part.
- This is a required input.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {11}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Hide all parts
JPT.ShowHideAllParts(JPT.BoolType.FALSE_VAL)

# Show Cube_1
JPT.ShowHideEntitiesByID(JPT.DTableType.DTABLE_BODY, 1, JPT.BoolType.TRUE_VAL)
```
