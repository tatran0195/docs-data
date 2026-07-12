---
id: JPT-FindSubAssemblyByName
title: JPT.FindSubAssemblyByName()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get the related information of the target sub assembly by its name
---

## Description

Get the related information of the target sub assembly by its name.

## Syntax

```psj
JPT.FindSubAssemblyByName(subAssemName)
```

## Inputs

### `subAssemName`

- A _String_ specifying the name of the target sub assembly.
- This is a required input.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or a _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ specifying found sub assemblies.

## Sample Code

```psj {7}
# Create 2 sub assemblies under All Parts assembly
JPT.CreateSubAssembly('CreateSubAsm0',JPT.DItem())
JPT.CreateSubAssembly('CreateSubAsm1',JPT.DItem())
JPT.ViewFitToModel()

# Get the information of the sub assembly with name = CreateSubAsm0
JPT.Debugger(JPT.FindSubAssemblyByName('CreateSubAsm0'))

```
