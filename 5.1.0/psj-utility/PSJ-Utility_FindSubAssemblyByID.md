---
id: JPT-FindSubAssemblyByID
title: JPT.FindSubAssemblyByID()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get the related information of the target sub assembly by its ID
---

## Description

Get the related information of the target sub assembly by its ID.

## Syntax

```psj
JPT.FindSubAssemblyByID(subAssemID)
```

## Inputs

### `subAssemID`

- An _Integer_ specifying the ID of the target sub assembly.
- This is a required input.

## Return Code

A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object specifying the information of the target sub assembly.

## Sample Code

```psj {7}
# Create 2 sub assemblies under All Parts assembly
JPT.CreateSubAssembly('CreateSubAsm0',JPT.DItem())
JPT.CreateSubAssembly('CreateSubAsm1',JPT.DItem())
JPT.ViewFitToModel()

# Get the information of the sub assembly with ID = 1
JPT.Debugger(JPT.FindSubAssemblyByID(1))
```
