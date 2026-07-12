---
id: Post-ResultSettings-MaxMin
title: Post.ResultSettings.MaxMin()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set up the result settings for displaying Max/Min value
---

## Description

Set up the result settings for displaying Max/Min value.

## Syntax

```psj
Post.ResultSettings.MaxMin(...)
```

Macro: [CmdPostMaxMinSettings](../../macro/post/CmdPostMaxMinSettings)

Ribbon: <menuselection>Post &#187; ResultSettings &#187; MaxMin</menuselection>

## Inputs

### `postDataVizOptMaxMin`

- A _[POST_DATA_VIZ_OPT_MAXMIN](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_MAXMIN)_ specifying all settings to display Max/Min value.
- The default value is [POST_DATA_VIZ_OPT_MAXMIN](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_MAXMIN).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.MaxMin(postDataVizOptMaxMin=PostDataVizOptMaxMin(iGroupMethod=1))
```
