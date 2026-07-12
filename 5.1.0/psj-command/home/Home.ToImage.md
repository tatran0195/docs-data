---
id: Home-ToImage
title: Home.ToImage()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Save the display window of Jupiter to an image file
---

## Description

Save the display window of Jupiter to an image file.

## Syntax

```psj
Home.ToImage(...)
```

Ribbon: <menuselection>Home &#187; ToImage</menuselection>

## Inputs

### `strImgPath`

- A _String_ specifying the path for exporting image.
- This is a required input.

### `bWhiteBG`

- A _Boolean_ specifying whether to set background color to white.
- The default value is _False_.

### `bTransparentBG`

- A _Boolean_ specifying whether to set background color to transparent. This option can only takes effect when export image is .png extension. Also, it cannot be used when `bWhiteBG` is set to True.
- The default value is _False_.

### `bFixedSize`

- A _Boolean_ specifying whether to make the size of export image fixed.
  - If this parameter is True, the image will be exported with size specified in `iExportWidth` and `iExportHeight`.
  - If this parameter is False, the size of the export image is the same as the size of the view window.
- The default value is _False_.

### `iExportWidth`

- An _Integer_ specifying the width of the export image.
- The default value is 1200.

### `iExportHeight`

- An _Integer_ specifying the height of the export image.
- The default value is 900.

### `bAutoCapture`

- A _Boolean_ to specify whether crop image to the displayed entity range.
- The default value is _False_.

### `listAdjust`

- A list of _Integer_ specifying the left, top, right and bottom margins from the minimized area.
- The default value is [0,0,0,0]
 
## Return Code

A _Boolean_ specifying the status of the process:

- _True_: The display window of Jupiter is saved to an image file.
- _False_: The display window of Jupiter cannot be saved to an image file.

## Sample Code

```psj {8,9,13-16}
import re
from os import environ

Geometry.Part.Cube()
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

export_status = Home.ToImage(strImgPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                          "/TechnoStar/Cube.png")

JPT.Debugger(export_status)

export_status = Home.ToImage(strImgPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                          "/TechnoStar/Cube_minimize.png",
                            bAutoCapture=True, 
                            listAdjust=[10,20,10,20])

JPT.Debugger(export_status)
```
