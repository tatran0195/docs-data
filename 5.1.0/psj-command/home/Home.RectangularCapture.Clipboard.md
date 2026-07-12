---
id: Home-RectangularCapture-Clipboard
title: Home.RectangularCapture.Clipboard()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Capture specified area in Main Window to clipboard.
---

## Description

Capture specified area in Main Window to clipboard.

## Syntax

```psj
Home.RectangularCapture.Clipboard(...)
```

Macro: Capture_Rectangular()

Ribbon: <menuselection>Home &#187; RectangularCapture &#187; Clipboard</menuselection>

## Inputs

### `iLeft`

- An _Integer_ specifying pixel position of image left.
- The default value is 0.

### `iTop`

- An _Integer_ specifying pixel position of image top.
- The default value is 0.

### `iRight`

- An _Integer_ specifying pixel position of image right.
- The default value is 0.

### `iBottom`

- An _Integer_ specifying pixel position of image bottom.
- The default value is 0.

## Return Code

A _Boolean_ specifying whether the function is successfully executed or not.

## Sample Code

```psj {3-7}
Geometry.Part.Cube()
JPT.ViewFitToModel
Home.RectangularCapture.Clipboard(
    iLeft=157, 
    iTop=175, 
    iRight=408, 
    iBottom=297)
```
