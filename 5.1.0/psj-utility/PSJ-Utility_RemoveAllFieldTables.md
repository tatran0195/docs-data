---
id: JPT-RemoveAllFieldTables
title: JPT.RemoveAllFieldTables()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Remove all the existing field tables
---

## Description

Remove all the existing field tables.

## Syntax

```psj
JPT.RemoveAllFieldTables()
```

## Inputs

This utility function does not require any input value.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {10}
# Create sample fields data
BoundaryConditions.FieldData(strName="test_1", iType=1,
                             ilSheet=[3, 4, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3])
BoundaryConditions.FieldData(strName="test_2", iType=4,
                             ilSheet=[3, 2, 1, 1, 2, 2, 3, 3])
BoundaryConditions.FieldData(strName="test_3", iType=3,
                             ilSheet=[3, 2, 1, 1, 2, 2, 3, 3])

# Remove all the created fields data
JPT.RemoveAllFieldTables()
```
