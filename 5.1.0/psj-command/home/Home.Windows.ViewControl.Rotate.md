---
id: Home-Windows-ViewControl-Rotate
title: Home.Windows.ViewControl.Rotate()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Rotate the entire models around each axis by the entered angle
---

## Description

Rotate the entire models around each axis by the entered angle.

## Syntax

```psj
Home.Windows.ViewControl.Rotate(...)
```

Macro: 

Ribbon: <menuselection>Home &#187; Windows &#187; ViewControl &#187; Rotate</menuselection>

## Inputs

### `dlAngle`

- A _List of Double_ specifying the angle (degree) in each axis (X, Y, Z) to rotate the entire model.
- This is a required input.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Home.Windows.ViewControl.FitToModel()
Home.Windows.ViewControl.Rotate(dlAngle=[0, 20, 20])
```
