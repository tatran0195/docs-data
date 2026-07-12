---
id: JPT-SetSelectMethod
title: JPT.SetSelectMethod()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Change the selection method in Jupiter to the specified one
---

## Description

Change the selection method in Jupiter to the specified one.

## Syntax

```psj
JPT.SetSelectMethod(selectMethodType)
```

## Inputs

### `selectMethodType`

- An _Enum_ specifying the _[SelectMethodType](../data-type/psj-utility/pre-utility/enumeration-types/select-method-types)_ describing the selection method.
- This is a required input.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {2,5,8,11}
# Select method to Body selection
JPT.SetSelectMethod(JPT.SelectMethodType.SELMTD_BODY)

# Select method to Face selection
JPT.SetSelectMethod(JPT.SelectMethodType.SELMTD_FACE)

# Select method to Edge selection
JPT.SetSelectMethod(JPT.SelectMethodType.SELMTD_EDGE)

# Select method to Node selection
JPT.SetSelectMethod(JPT.SelectMethodType.SELMTD_NODE)
```
