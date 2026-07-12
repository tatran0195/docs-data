---
id: Post-ResultSettings-Deformation
title: Post.ResultSettings.Deformation()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set up the result settings for displaying the deformation
---

## Description

Set up the result settings for displaying the deformation.

## Syntax

```psj
Post.ResultSettings.Deformation(...)
```

Macro: [CmdPostDeformSettings](../../macro/post/CmdPostDeformSettings)

Ribbon: <menuselection>Post &#187; ResultSettings &#187; Deformation</menuselection>

## Inputs

### `postDataVizOptDeform`

- A _[POST_DATA_VIZ_OPT_DEFORM](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_DEFORM)_ specifying all settings of the deformation display.
- The default value is [POST_DATA_VIZ_OPT_DEFORM](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_DEFORM).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Deformation(postDataVizOptDeform=PostDataVizOptDeform(bEachDirectionRatio=True))
```
