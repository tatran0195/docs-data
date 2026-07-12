---
id: Home-Windows-ViewControl-FitToModel
title: Home.Windows.ViewControl.FitToModel()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Fit the entire model to the main window size
---

## Description

Fit the entire model to the main window size.

## Syntax

```psj
Home.Windows.ViewControl.FitToModel(...)
```

Macro: 

Ribbon: <menuselection>Home &#187; Windows &#187; ViewControl &#187; FitToModel</menuselection>

## Inputs

This function does not contain any input values.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {2}
Geometry.Part.Cube()
Home.Windows.ViewControl.FitToModel()
```
