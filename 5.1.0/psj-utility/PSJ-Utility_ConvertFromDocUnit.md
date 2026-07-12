---
id: JPT-ConvertFromDocUnit
title: JPT.ConvertFromDocUnit()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Convert the inputted value from the current using Jupiter unit system to SI\[m\] units (Jupiter macro units)
---

## Description

Convert the inputted value from the current using Jupiter unit system to SI\[m\] unit (Jupiter macro unit).
The return value will be the value after the conversion.

## Syntax

```psj
JPT.ConvertFromDocUnit(inputValue, unitType)
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
# Convert the value = 1 from the current Jupiter Unit system to Jupiter macro unit system
convertFromDoc = JPT.ConvertFromDocUnit(1, JPT.UnitType.Unit_Length)
JPT.Debugger(convertFromDoc)
```
