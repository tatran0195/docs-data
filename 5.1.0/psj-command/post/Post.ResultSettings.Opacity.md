---
id: Post-ResultSettings-Opacity
title: Post.ResultSettings.Opacity()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set up the result settings for displaying the opacity
---

## Description

Set up the result settings for displaying the opacity.

## Syntax

```psj
Post.ResultSettings.Opacity(...)
```

Macro: [CmdPostTransparencySettings](../../macro/post/CmdPostTransparencySettings)

Ribbon: <menuselection>Post &#187; ResultSettings &#187; Opacity</menuselection>

## Inputs

### `postDataVizOptTransparency`

- A _[POST_DATA_VIZ_OPT_TRANSPARENCY](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_TRANSPARENCY)_ specifying all settings of the opacity display.
- The default value is [POST_DATA_VIZ_OPT_TRANSPARENCY](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_TRANSPARENCY).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Opacity(postDataVizOptTransparency=PostDataVizOptTransparency(dTransparency=0.5))
```
