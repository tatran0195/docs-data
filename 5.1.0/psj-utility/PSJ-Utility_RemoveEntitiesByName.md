---
id: JPT-RemoveEntitiesByName
title: JPT.RemoveEntitiesByName()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Remove entities by using the inputted name
---

## Description

Remove entities by using the inputted name.

## Syntax

```psj
JPT.RemoveEntitiesByName(DTableType, itemName, BoolType)
```

## Inputs

### `DTableType`

- An _Enum_ specifying the _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_ of entity in Jupiter.
- This is a required input.

### `itemName`

- A _String_ specifying the name of the target entity to be removed.
- This is a required input.

### `BoolType`

- An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the matching type:
  - _False_: Approximate match.
  - _True_: Exact match.
- This is a required input.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Remove all the parts with their name have the "_" character inside
JPT.RemoveEntitiesByName(JPT.DTableType.DTABLE_BODY, "_", JPT.BoolType.FALSE_VAL)
```
