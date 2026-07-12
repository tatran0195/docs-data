---
id: Post-ResultSettings-FFT3DDisplay
title: Post.ResultSettings.FFT3DDisplay()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set up the result settings for displaying the FFT3D
---

## Description

Set up the result settings for displaying the FFT3D.

## Syntax

```psj
Post.ResultSettings.FFT3DDisplay(...)
```

Macro: [CmdPostFFT3DDisplaySettings](../../macro/post/CmdPostFFT3DDisplaySettings)

Ribbon: <menuselection>Post &#187; ResultSettings &#187; FFT3DDisplay</menuselection>

## Inputs

### `postDataVizOptBDPP`

- A _[POST_DATA_VIZ_OPT_BDPP](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_BDPP)_ specifying all settings of the FFT3D display.
- The default value is [POST_DATA_VIZ_OPT_BDPP](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_BDPP).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {1-5}
Post.ResultSettings.FFT3DDisplay(postDataVizOptBDPP=PostDataVizOptBDPP(
                                dLayerPointSize=2.0, 
                                dLineWidth=2.0, 
                                dPointSize=2.0, 
                                dDotDistance=0.05))
```
