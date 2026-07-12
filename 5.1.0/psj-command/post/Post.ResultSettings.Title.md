---
id: Post-ResultSettings-Title
title: Post.ResultSettings.Title()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set up the result settings for displaying the title
---

## Description

Set up the result settings for displaying the title.

## Syntax

```psj
Post.ResultSettings.Title(...)
```

Macro: [CmdPostTitleSettings](../../macro/post/CmdPostTitleSettings)

Ribbon: <menuselection>Post &#187; ResultSettings &#187; Title</menuselection>

## Inputs

### `postDataVizOptTitle`

- A _[POST_DATA_VIZ_OPT_TITLE](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_TITLE)_ specifying all settings of the result title display.
- The default value is [POST_DATA_VIZ_OPT_TITLE](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_TITLE).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Title(postDataVizOptTitle=PostDataVizOptTitle(iBackgroundFillColor=17919, dTransparency=0.6))
```
