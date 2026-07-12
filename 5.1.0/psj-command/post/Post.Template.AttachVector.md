---
id: Post-Template-AttachVector
title: Post.Template.AttachVector()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Attach the current vector settings to the specified template
---

## Description

Attach the current vector settings to the specified template.

## Syntax

```psj
Post.Template.AttachVector(...)
```

Macro: [AttachTemplateVector](../../macro/post/AttachTemplateVector)

Ribbon: <menuselection>Post &#187; Template &#187; AttachVector</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of template, which will attach the vector settings.
- The default value is "NewTemplate".

### `postDataVizOptVector`

- A _[POST_DATA_VIZ_OPT_VECTOR](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_VECTOR)_ specifying all settings of the result vector display.
- The default value is [POST_DATA_VIZ_OPT_VECTOR](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_VECTOR).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {2-5}
Post.Template.Create(strName="Vector_Template", strComment="Attach Vector Template")
template = Post.Template.AttachVector(strName="Vector_Template", 
                                    postDataVizOptVector=POST_DATA_VIZ_OPT_VECTOR(
                                        dRatioModel=0.05, 
                                        dRatioScreen=0.05))
JPT.Debugger(template)
```
