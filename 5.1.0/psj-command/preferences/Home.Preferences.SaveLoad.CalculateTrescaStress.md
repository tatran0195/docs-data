---
id: Home-Preferences-SaveLoad-CalculateTrescaStress
title: Home.Preferences.SaveLoad.CalculateTrescaStress()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Calculate the Tresca stress and add it to the results tree.
---

## Description

Calculate the Tresca Stress automatically when the result file is opened.

## Syntax

```psj
Home.Preferences.SaveLoad.CalculateTrescaStress(...)
```

Macro: [SetDisplayPostAssemblyTree](../../macro/preferences/SetDisplayPostAssemblyTree)

Ribbon: <menuselection>Home &#187; Preferences &#187; SaveLoad &#187; CalculateTrescaStress</menuselection>

## Inputs

### `bUseTrescaStress`

- A _Boolean_ specifying whether to use Tresca Stress calculation.
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj 
Home.Preferences.SaveLoad.CalculateTrescaStress(bUseTrescaStress = False)
```
