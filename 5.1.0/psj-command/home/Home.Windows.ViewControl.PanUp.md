---
id: Home-Windows-ViewControl-PanUp
title: Home.Windows.ViewControl.PanUp()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Move the view up by the entered amount of movement
---

## Description

Move the view up by the entered amount of movement.

## Syntax

```psj
Home.Windows.ViewControl.PanUp(...)
```

Macro: 

Ribbon: <menuselection>Home &#187; Windows &#187; ViewControl &#187; PanUp</menuselection>

## Inputs

### `dDistance`

- A _Double_ specifying the relative movement amounts on the screen that the view will move up.
- This is a required input.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Home.Windows.ViewControl.FitToModel()
Home.Windows.ViewControl.PanUp(dDistance=50)
```
