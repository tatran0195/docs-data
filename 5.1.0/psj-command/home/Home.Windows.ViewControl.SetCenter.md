---
id: Home-Windows-ViewControl-SetCenter
title: Home.Windows.ViewControl.SetCenter()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set the center of rotation of the model 
---

## Description

Set the center of rotation of the model.

## Syntax

```psj
Home.Windows.ViewControl.SetCenter(...)
```

Macro: 

Ribbon: <menuselection>Home &#187; Windows &#187; ViewControl &#187; SetCenter</menuselection>

## Inputs

### `dlCenter`

- A _List of Double_ specifying the rotation center coordinate of the model. The unit of the rotation center coordinate  is taken according to the current document unit.
- This is a required input.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Home.Windows.ViewControl.FitToModel()
Home.Windows.ViewControl.SetCenter(dlCenter=[0.0, 0.01, 0.0])
```
