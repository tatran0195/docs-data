---
id: Post-Template-AttachCircle
title: Post.Template.AttachCircle()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Attach the current result circle settings to the specified template
---

## Description

Attach the current result circle settings to the specified template.

## Syntax

```psj
Post.Template.AttachCircle(...)
```

Macro: [AttachTemplateCircle](../../macro/post/AttachTemplateCircle)

Ribbon: <menuselection>Post &#187; Template &#187; AttachCircle</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of template, which will attach the circle settings.
- The default value is "NewTemplate".

### `postDataVizOptCircle`

- A _[POST_DATA_VIZ_OPT_CIRCLE](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_CIRCLE)_ specifying all settings of the circle display.
- The default value is [POST_DATA_VIZ_OPT_CIRCLE](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_CIRCLE).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {2-5}
Post.Template.Create(strName="Circle_Template", strComment="Attach Circle Template")
template = Post.Template.AttachCircle(strName="Circle_Template", 
                                    postDataVizOptCircle=POST_DATA_VIZ_OPT_CIRCLE(
                                        dRatioModel=0.04, 
                                        dRatioScreen=0.04))
JPT.Debugger(template)
```
