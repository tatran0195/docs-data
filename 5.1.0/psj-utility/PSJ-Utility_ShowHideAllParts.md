---
id: JPT-ShowHideAllParts
title: JPT.ShowHideAllParts()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Show or Hide all part existing on the screen
---

## Description

Show or Hide all part existing on the screen.

## Syntax

```psj
JPT.ShowHideAllParts(BoolType)
```

## Inputs

### `BoolType`

- An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the display mode:
  - _False_: Hide all parts.
  - _True_: Show all parts.
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

# Show all parts
JPT.ShowHideAllParts(JPT.BoolType.TRUE_VAL)
```
