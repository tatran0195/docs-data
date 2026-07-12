---
id: Post-Template-AttachViewPoint
title: Post.Template.AttachViewPoint()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Attach the current view point settings to the specified template
---

## Description

Attach the current view point settings to the specified template

## Syntax

```psj
Post.Template.AttachViewPoint(...)
```

Macro: [AttachTemplateViewPoint](../../macro/post/AttachTemplateViewPoint)

Ribbon: <menuselection>Post &#187; Template &#187; AttachViewPoint</menuselection>

## Inputs

### `strName`

- A _String_ specifying specifying the name of template, which will attach the viewpoint settings.
- The default value is "NewTemplate".

### `postDataVizOptViewPoint`

- A _[POST_DATA_VIZ_OPT_VIEWPOINT](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_VIEWPOINT)_ specifying all settings of a view point.
- The default value is [POST_DATA_VIZ_OPT_VIEWPOINT](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_VIEWPOINT).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {2-6}
Post.Template.Create(strName="ViewPoint_Template", strComment="Attach View Point Template")
template = Post.Template.AttachViewPoint(strName="ViewPoint_Template", 
                                        postDataVizOptViewPoint=POST_DATA_VIZ_OPT_VIEWPOINT(
                                            dlTranslationMatrix=[-0.707107, -0.5, 0.5, 0.0, 0.707107, -0.5, 0.5, 0.0, -4.49147e-08, 0.707107, 0.707107, 0.0, 0.0, 0.0, 0.0, 1.0], 
                                            dlCenter=[0.016, 0.005, 0.0025], 
                                            dScaleFactor=0.0115058))
JPT.Debugger(template)
```
