---
id: JPT-UpdateCheckboxAssembly
title: JPT.UpdateCheckboxAssembly()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Set state of checkbox of item in Assembly Tree
---

## Description

Set the state of checkbox of item in Assembly Tree.

## Syntax

```psj
JPT.UpdateCheckboxAssembly(DItemType, entityID, BoolType)
```

## Inputs

### `DItemType`

- An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of the entity.
- This is a required input.

### `entityID`

- An _Integer_ specifying the ID of the target entity.
- This is a required input.

### `BoolType`

- An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the state of checkbox:
  - _True_: Check the checkbox of item in Assembly Tree.
  - _False_: Uncheck the checkbox of item in Assembly Tree.
- This is a required input.

:::tip
You also can input **1** instead of inputting JPT.BoolType.TRUE_VAL,
or input **0** instead of inputting JPT.BoolType.FALSE_VAL.
:::

## Return Code

This utility function does not have output value.

## Sample Code

```psj {10-11}
# prepare model...
JPT.Exec('CreateCube([0, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_1", 7105764, 0:0)')
JPT.Exec('CreateCube([0.02, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_2", 6409934, 0:0)')
JPT.Exec('CreateCube([0, 0.02, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_3", 13259210, 0:0)')

parts = JPT.GetAllParts()

# update checkbox from assembly tree
for part in parts:
    JPT.UpdateCheckboxAssembly(JPT.DItemType.BODY, part.id, 1) # turn on checkbox
    JPT.UpdateCheckboxAssembly(JPT.DItemType.BODY, part.id, 0) # turn off checkbox
```
