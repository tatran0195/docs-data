---
id: Post-ResultSettings-Animation
title: Post.ResultSettings.Animation()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set up the result settings for displaying the animation
---

## Description

Set up the result settings for displaying the animation.

## Syntax

```psj
Post.ResultSettings.Animation(...)
```

Macro: [CmdPostAnimationSettings](../../macro/post/CmdPostAnimationSettings)

Ribbon: <menuselection>Post &#187; ResultSettings &#187; Animation</menuselection>

## Inputs

### `postDataVizOptAnimation`

- A _[POST_DATA_VIZ_OPT_ANIMATION](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_ANIMATION)_ specifying all settings of the animation display.
- The default value is [POST_DATA_VIZ_OPT_ANIMATION](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_ANIMATION).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Animation(postDataVizOptAnimation=PostDataVizOptAnimation(iLoopType=2, bFixContour=True))
```
