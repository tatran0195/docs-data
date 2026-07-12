---
id: JPT-DeleteSubAssembly
title: JPT.DeleteSubAssembly()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Delete the inputted sub assembly
---

## Description

Delete the inputted sub assembly.

## Syntax

```psj
JPT.DeleteSubAssembly(subAssembly)
```

## Inputs

### `subAssembly`

- A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object specifying the sub assembly which will be deleted.
- This is a required input.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {7}
# Create 2 sub assemblies under All Parts assemly
JPT.CreateSubAssembly('CreateSubAsm0',JPT.DItem())
JPT.CreateSubAssembly('CreateSubAsm1',JPT.DItem())

# Delete the created CreateSubAsm1
subAssem = JPT.FindSubAssemblyByID(2)
JPT.DeleteSubAssembly(subAssem)
```
