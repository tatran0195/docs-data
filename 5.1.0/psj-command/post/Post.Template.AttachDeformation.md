---
id: Post-Template-AttachDeformation
title: Post.Template.AttachDeformation()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Attach the current deformation settings to the specified template
---

## Description

Attach the current deformation settings to the specified template.

## Syntax

```psj
Post.Template.AttachDeformation(...)
```

Macro: [AttachTemplateDeformation](../../macro/post/AttachTemplateDeformation)

Ribbon: <menuselection>Post &#187; Template &#187; AttachDeformation</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of template, which will attach the deformation settings.
- The default value is "NewTemplate".

### `postDataVizOptDeform`

- A _[POST_DATA_VIZ_OPT_DEFORM](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_DEFORM)_ specifying all settings of the deformation display.
- The default value is [POST_DATA_VIZ_OPT_DEFORM](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_DEFORM).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {2-5}
Post.Template.Create(strName="Deformation_Template", strComment="Attach Deformation Template")
template = Post.Template.AttachDeformation(strName="Deformation_Template", 
                                        postDataVizOptDeform=POST_DATA_VIZ_OPT_DEFORM(
                                            bEachDirectionRatio=True, 
                                            dlEachDirectionRatio=[0.05, 0.05, 0.05]))
JPT.Debugger(template)
```
