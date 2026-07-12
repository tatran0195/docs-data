---
id: JPT-ConvertValueToMacroUnit
title: JPT.ConvertValueToMacroUnit()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Convert the inputted value from the SI\[m\] unit (Jupiter macro unit) to the specified unit
---

## Description

Convert the inputted value from the SI\[m\] unit (Jupiter macro unit) to the specified unit.
The return value will be the value after conversion.

## Syntax

```psj
JPT.ConvertValueToMacroUnit(inputValue, unitType, outputValueType)
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

- A _String_ specifying the desired unit of the inputted value which will be got after converting from Jupiter macro unit.
- This is a required input.

## Return Code

A _Double_ specifying the converted value.

## Sample Code

```psj {2}
# Convert 1m from Jupiter macro unit system to mm
convertToMacro = JPT.ConvertValueToMacroUnit(1, JPT.UnitType.Unit_Length, 'mm') # 1m -> mm
JPT.Debugger(convertToMacro) # 1000
```
