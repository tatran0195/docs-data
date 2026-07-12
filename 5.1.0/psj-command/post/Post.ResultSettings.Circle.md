---
id: Post-ResultSettings-Circle
title: Post.ResultSettings.Circle()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set up the result settings for displaying the circle
---

## Description

Set up the result settings for displaying the circle.

## Syntax

```psj
Post.ResultSettings.Circle(...)
```

Macro: [CmdPostCircleSettings](../../macro/post/CmdPostCircleSettings)

Ribbon: <menuselection>Post &#187; ResultSettings &#187; Circle</menuselection>

## Inputs

### `postDataVizOptCircle`

- A _[POST_DATA_VIZ_OPT_CIRCLE](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_CIRCLE)_ specifying all settings of the circle display.
- The default value is [POST_DATA_VIZ_OPT_CIRCLE](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_CIRCLE).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Circle(postDataVizOptCircle=PostDataVizOptCircle(dRatioModel=0.05, dRatioScreen=0.05))
```
