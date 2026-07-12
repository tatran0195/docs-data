---
id: JPT-GetEntitiesByName
title: JPT.GetEntitiesByName()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get information of the inputted entity name
---

## Description

Get information of the inputted entity name.

## Syntax

```psj
JPT.GetEntitiesByName(DTableType, itemName, BoolType)
```

## Inputs

### `DTableType`

- An _Enum_ specifying the _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_ of entity in Jupiter.
- This is a required input.

### `itemName`

- A _String_ specifying the name of the target entity.
- This is a required input.

### `BoolType`

- An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the matching type:
  - _False_: Approximate match.
  - _True_: Exact match.
- This is a required input.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing the information of the entities have the inputted name.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the information of the part with name = "_" and store it to a list
listParts = JPT.GetEntitiesByName(JPT.DTableType.DTABLE_BODY, "_", JPT.BoolType.FALSE_VAL)
print(listParts[0].name) # Cube_1
print(listParts[2].name) # Cube_3
print(listParts[2].id) # 3
```
