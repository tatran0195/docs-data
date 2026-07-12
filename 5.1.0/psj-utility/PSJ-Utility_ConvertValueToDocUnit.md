---
id: JPT-ConvertValueToDocUnit
title: JPT.ConvertValueToDocUnit()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Convert the inputted value from SI\[m\] units (Jupiter macro units) to the current Jupiter unit system
---

## Description

Convert the inputted value from SI\[m\] units (Jupiter macro units) to the current Jupiter unit system.

## Syntax

```psj
JPT.ConvertValueToDocUnit(inputValue, unitType)
```

## Inputs

### `inputValue`

- A _Double_ which will be used for converting.
- This is a required input.

### `unitType`

- An _Enum_ specifying the _[Unit Types](../data-type/psj-utility/pre-utility/enumeration-types/unit-types.md)_ which will be used as the reference for converting.
- The type of unit can be found at: <menuselection>Home &#187; Preference &#187; Unit</menuselection> in Jupiter.
- This is a required input.

## Return Code

A _Double_ specifying the converted value.

## Sample Code

```psj {2}
# Convert 1m in Jupiter macro unit system to the current unit system of Jupiter
convertToDoc = JPT.ConvertValueToDocUnit(1, JPT.UnitType.Unit_Length)
JPT.Debugger(convertToDoc)
```
