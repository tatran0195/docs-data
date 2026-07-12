---
id: Post-ResultSettings-Contour
title: Post.ResultSettings.Contour()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set up the result settings for displaying the contour 
---

## Description

Set up the result settings for displaying the contour.

## Syntax

```psj
Post.ResultSettings.Contour(...)
```

Macro: [CmdPostContourSettings](../../macro/post/CmdPostContourSettings)

Ribbon: <menuselection>Post &#187; ResultSettings &#187; Contour</menuselection>

## Inputs

### `postDataVizOptContour`

- A _[POST_DATA_VIZ_OPT_CONTOUR](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_CONTOUR)_ specifying all settings of the contour display.
- The default value is [POST_DATA_VIZ_OPT_CONTOUR](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_CONTOUR).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {1-6}
Post.ResultSettings.Contour(postDataVizOptContour=PostDataVizOptContour(
                            dMaxUser=1696.404297, 
                            dMinUser=0.0, 
                            dMaxTotal=1696.404297, 
                            dMinTotal=0.0, 
                            iInterpolateMethod=-1))
```
