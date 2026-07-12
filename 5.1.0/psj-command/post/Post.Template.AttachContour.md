---
id: Post-Template-AttachContour
title: Post.Template.AttachContour()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Attach the current contour settings to the specified template
---

## Description

Attach the current contour settings to the specified template.

## Syntax

```psj
Post.Template.AttachContour(...)
```

Macro: [AttachTemplateContour](../../macro/post/AttachTemplateContour)

Ribbon: <menuselection>Post &#187; Template &#187; AttachContour</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of Template will attach the contour settings.
- The default value is "NewTemplate".

### `postDataVizOptContour`

- A _[POST_DATA_VIZ_OPT_CONTOUR](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_CONTOUR)_ specifying all settings of the contour display.
- The default value is [POST_DATA_VIZ_OPT_CONTOUR](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_CONTOUR).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {2-6}
Post.Template.Create(strName="Contour_Template", strComment="Attach Contour Template")
template = Post.Template.AttachContour(strName="Contour_Template", 
                                    postDataVizOptContour=POST_DATA_VIZ_OPT_CONTOUR(
                                        iColorDivision=20, 
                                        dMaxUser=0, 
                                        dMinUser=0))
JPT.Debugger(template)
```
