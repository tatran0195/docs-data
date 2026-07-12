---
id: JPT-ConvertFromMacroUnit
title: JPT.ConvertFromMacroUnit()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Convert the inputted value with the specified unit to the SI\[m\] unit (Jupiter macro unit)
---

## Description

Convert the inputted value with the specified unit to the SI\[m\] unit (Jupiter macro unit).
The return value will be the value after the conversion.

## Syntax

```psj
JPT.ConvertFromMacroUnit(inputValue, unitType, outputValueType)
```

## Inputs

### `inputValue`

- A _Double_ which will be used for converting.
- This is a required input.

### `unitType`

- An _Enum_ specifying the _[Unit Types](../data-type/psj-utility/pre-utility/enumeration-types/unit-types.md)_ which will be used as the reference for converting.
- The type of unit can be found at: <menuselection>Home &#187; Preference &#187; Unit</menuselection> in Jupiter.
- This is a required input.

### `outputValueType`

- A _String_ specifying the indicated unit of the inputted value which will be used for converting to Jupiter macro unit.
- This is a required input.

## Return Code

A _Double_ specifying the converted value.

## Sample Code

```psj {2}
# Convert 1mm to the Jupiter macro unit system
convertFromMacro = JPT.ConvertFromMacroUnit(1, JPT.UnitType.Unit_Length, 'mm') # mm -> m
JPT.Debugger(convertFromMacro) # 0.001 m
```
