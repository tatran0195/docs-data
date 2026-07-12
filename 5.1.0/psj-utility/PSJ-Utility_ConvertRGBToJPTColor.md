---
id: JPT-ConvertRGBToJPTColor
title: JPT.ConvertRGBToJPTColor()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Convert RGB (Red, Green, Blue) color code to color value in Jupiter
---

## Description

Convert RGB (Red, Green, Blue) color code to color value in Jupiter.

## Syntax

```psj
JPT.ConvertRGBToJPTColor(redValue, greenValue, blueValue)
```

## Inputs

### `redValue`

- An _Integer_ specifying the red color code.
- This is a required input.

### `greenValue`

- An _Integer_ specifying the green color code.
- This is a required input.

### `blueValue`

- An _Integer_ specifying the blue color code.
- This is a required input.

## Return Code

An _Integer_ specifying color code in Jupiter.

## Sample Code

```psj {2}
# Convert the RGB color code to the color code in Jupiter
newColor = JPT.ConvertRGBToJPTColor(255,100,213) # Pink color
JPT.Debugger(newColor)
```
