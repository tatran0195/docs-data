---
id: SetDefaultAutoSettingMeshSize
title: SetDefaultAutoSettingMeshSize()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Turn ON/OFF Data Validation.

## Syntax

```psj
SetDefaultAutoSettingMeshSize(int Selection, float Maximum, float Minimum)
```

## Inputs

### `1. int`

Select setting type
- 0: Average 
- 1: Minimum
- 2: Maximum

### `2. float`

Coefficent for Maximum mesh size.

### `3. float`

Coefficent for Minimum mesh size.

## Return Code

No return code.

## Sample Code

```psj
SetDefaultAutoSettingMeshSize(1, 2, 0.2)
```
