---
id: Home-CopyToClipboard
title: Home.CopyToClipboard()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Save the current display window of Jupiter to the clipboard
---

## Description

Save the current display window of Jupiter to the clipboard.

## Syntax

```psj
Home.CopyToClipboard(...)
```

Ribbon: <menuselection>Home &#187; CopyToClipboard</menuselection>

## Inputs

### `bWhiteBG`

- A _Boolean_ specifying whether to set background color to white.
- The default value is _False_.

### `bTransparentBG`

- A _Boolean_ specifying whether to set background color to transparent.
  This option can only takes effect when export image is .png extension. Also, it cannot be used when `bWhiteBG` is set to True.
- The default value is _False_.

### `bFixedSize`

- A _Boolean_ specifying whether to make the size of export image fixed.
  If this parameter is True, the image will be exported with size specified in `iExportWidth` and `iExportHeight`.
  If this parameter is False, the size of the export image is the same as the size of the view window.
- The default value is _False_.

### `iWidth`

- An _Integer_ specifying the width of the export image.
- The default value is 1200.

### `iHeight`

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
- _True_: The current display window of Jupiter is saved to clipboard.
- _False_: The current display window cannot be saved to clipboard.

## Sample Code

```psj {5-9,13-19}
Geometry.Part.Cube()
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

copy = Home.CopyToClipboard(bWhiteBG=False,
                            bTransparentBG=False,
                            bFixedSize=False,
                            iWidth=1200,
                            iHeight=900)

JPT.Debugger(copy)

copy = Home.CopyToClipboard(bWhiteBG=False,
                            bTransparentBG=False,
                            bFixedSize=False,
                            iWidth=1200,
                            iHeight=900,
                            bAutoCapture=True, 
                            listAdjust=[10,20,10,20])

JPT.Debugger(copy)
```
