---
id: JPT-RemoveAllByTableType
title: JPT.RemoveAllByTableType()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Remove all the entities relating to the inputted DTableType
---

## Description

Remove all the entities relating to the inputted _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_.

## Syntax

```psj
JPT.RemoveAllByTableType(DTableType)
```

## Inputs

### `DTableType`

- An _Enum_ specifying the _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_ of the entities which will be removed.
- This is a required input.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {9}
# Prepare model
Geometry.Part.Cube(iPartColor=5955674)
Geometry.Part.Cube(strName="Cube_2", iPartColor=5682356)
Geometry.Part.Cube(strName="Cube_3", iPartColor=12237393)
Geometry.Part.Cube(strName="Cube_4", iPartColor=6740326)
Geometry.Part.Cube(strName="Cube_5", iPartColor=7335919)

# Remove all the created parts
JPT.RemoveAllByTableType(JPT.DTableType.DTABLE_BODY)
```
