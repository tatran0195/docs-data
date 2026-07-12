---
id: Home-Windows-ViewControl-ZoomIn
title: Home.Windows.ViewControl.ZoomIn()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Zoom in the view by the zoom ratio
---

## Description

Zoom in the view by the zoom ratio.

## Syntax

```psj
Home.Windows.ViewControl.ZoomIn(...)
```

Macro: 

Ribbon: <menuselection>Home &#187; Windows &#187; ViewControl &#187; ZoomIn</menuselection>

## Inputs

### `dZoom`

- A _Double_ specifying the zoom in ratio. The zoom ratio should be in range (0:1). 
- If the inputted larger than 1, then the  zoom ratio = 1/(inputted value).
- The default value is 0.83333333.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Home.Windows.ViewControl.FitToModel()
Home.Windows.ViewControl.ZoomIn(dZoom=0.3)
```
