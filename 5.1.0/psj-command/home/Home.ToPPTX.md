---
id: Home-ToPPTX
title: Home.ToPPTX()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Save the display window of Jupiter to an image file in pptx.
---

## Description

Save the display window of Jupiter to an image file in pptx.

## Syntax

```psj
Home.ToPPTX(...)
```

Ribbon: <menuselection>Home &#187; ToImage &#187; 2D Image</menuselection>

## Inputs

### `bAutoCapture`

- A _Boolean_ to specify whether crop image to the displayed entity range.
- The default value is _False_.

### `listAdjust`

- A list of _Integer_ specifying the left, top, right and bottom margins from the minimized area.
- The default value is [0,0,0,0]
 
## Return Code

A _Boolean_ specifying the status of the process:

- _True_: The display window of Jupiter is saved to an image file in pptx.
- _False_: The display window of Jupiter cannot be saved to an image file in pptx.

## Sample Code

```psj {9,10}
Geometry.Part.Cube()
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

copy_paste = Home.ToPPTX()

JPT.Debugger(copy_paste)

export_status = Home.ToPPTX(bAutoCapture=True, 
                            listAdjust=[10,20,10,20])

JPT.Debugger(copy_paste)
```
