---
id: Home-Windows-ViewControl-PanRight
title: Home.Windows.ViewControl.PanRight()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Move the view to the right by the entered amount of movement
---

## Description

Move the view to the right by the entered amount of movement.

## Syntax

```psj
Home.Windows.ViewControl.PanRight(...)
```

Macro: 

Ribbon: <menuselection>Home &#187; Windows &#187; ViewControl &#187; PanRight</menuselection>

## Inputs

### `dDistance`

- A _Double_ specifying the relative movement amounts on the screen that the view will move to the right.
- This is a required input.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Home.Windows.ViewControl.FitToModel()
Home.Windows.ViewControl.PanRight(dDistance=50)
```
