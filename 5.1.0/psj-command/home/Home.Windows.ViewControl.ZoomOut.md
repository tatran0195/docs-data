---
id: Home-Windows-ViewControl-ZoomOut
title: Home.Windows.ViewControl.ZoomOut()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Zoom out the view by the zoom ratio
---

## Description

Zoom out the view by the zoom ratio.

## Syntax

```psj
Home.Windows.ViewControl.ZoomOut(...)
```

Macro: 

Ribbon: <menuselection>Home &#187; Windows &#187; ViewControl &#187; ZoomOut</menuselection>

## Inputs

### `dZoom`

- A _Double_ specifying the zoom out ratio. The zoom ratio should be larger than 1. 
- If the inputted value is in range (0:1), then the  zoom ratio = 1/(inputted value).
- The default value is 1.2.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Home.Windows.ViewControl.FitToModel()
Home.Windows.ViewControl.ZoomOut(dZoom=1.15)
```
