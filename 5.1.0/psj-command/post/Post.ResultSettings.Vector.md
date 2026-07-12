---
id: Post-ResultSettings-Vector
title: Post.ResultSettings.Vector()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set up the result settings for displaying the vector
---

## Description

Set up the result settings for displaying the vector.

## Syntax

```psj
Post.ResultSettings.Vector(...)
```

Macro: [CmdPostVectorSettings](../../macro/post/CmdPostVectorSettings)

Ribbon: <menuselection>Post &#187; ResultSettings &#187; Vector</menuselection>

## Inputs

### `postDataVizOptVector`

- A _[POST_DATA_VIZ_OPT_VECTOR](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_VECTOR)_ specifying all settings of the result vector display.
- The default value is [POST_DATA_VIZ_OPT_VECTOR](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_VECTOR).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Vector(postDataVizOptVector=PostDataVizOptVector(dRatioModel=0.05, dRatioScreen=0.05))
```
