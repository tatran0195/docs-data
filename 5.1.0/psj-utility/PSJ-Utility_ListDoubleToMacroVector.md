---
id: JPT-ListDoubleToMacroVector
title: JPT.ListDoubleToMacroVector()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Convert a list of 3 double values to a vector3d (Macro string type)
---

## Description

Convert a _List_ of 3 _Double_ values to a Vector3D (Macro string type).

## Syntax

```psj
JPT.ListDoubleToMacroVector(doubleValue1, doubleValue2, doubleValue3)
```

## Inputs

### `doubleValue1`

- A _Double_ specifying the first value which will be used for converting.
- This is a required input.

### `doubleValue2`

- A _Double_ specifying the second value which will be used for converting.
- This is a required input.

### `doubleValue3`

- A _Double_ specifying the third value which will be used for converting.
- This is a required input.

## Return Code

A _String_ specifying the converted Vector3D (Macro string type).

## Sample Code

```psj {6}
# Convert a list of 3 double values to a vector3d (Macro string type)
inputValue1 = 0.001
inputValue2 = 2.1
inputValue3 = 5.5
# Return a string object with value = [0.001,2.1,5.5]
JPT.Debugger(JPT.ListDoubleToMacroVector(inputValue1, inputValue2, inputValue3))
```
