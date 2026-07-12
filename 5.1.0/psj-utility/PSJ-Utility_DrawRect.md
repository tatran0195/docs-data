---
id: JPT-DrawRect
title: JPT.DrawRect()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Draw a rectangle on Main Window
---

## Description

Draw a rectangle on Main Window by window coordinate.

## Syntax

```psj
JPT.DrawRect()
```

## Inputs

### `left `
- An _Int_ specifying the x-coordinate of the left edge of the rectangle, in pixels.

### `top`
- An _Int_ specifying the Y-coordinate of the top edge of the rectangle, in pixels.

### `right`
- An _Int_ specifying the x-coordinate of the right edge of the rectangle, in pixels.

### `bottom`
- An _Int_ specifying the y-coordinate of the bottom edge of the rectangle, in pixels.

### `color`
- An _Int_ in hexadecimal format representing the arrow's color. 
- The default color is cyan (RGB(0, 255, 255)).

### `width`
- An _Int_ specifying the width of the arrow's shaft in pixels. 
- The default is 1.

## Return Code

- A _Boolean_ specifying Succeeded or Failed.
  - True: Succeeded.
  - False: Failed.

## Sample Code

```psj {6,12,18}
JPT.ClearDraw()
# Draw a rectangle with 
# top-left corner at (10, 20) 
# bottom-right corner at (50, 100)
# in pixels
JPT.DrawRect(10, 20, 50, 100)

# Draw a rectangle in red with  
# top-left corner at (100, 200) 
# and bottom-right corner at (400, 400)
# in pixels
JPT.DrawRect(100, 200, 400, 400, 255)

# Draw a rectangle in yellow, width=5 with 
# top-left corner at (100, 10) 
# bottom-right corner at (200, 100)
# in pixels
JPT.DrawRect(100, 10, 200, 100, JPT.ConvertRGBToJPTColor(255,255,0), 5)

```
