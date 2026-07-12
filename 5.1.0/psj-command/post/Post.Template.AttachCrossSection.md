---
id: Post-Template-AttachCrossSection
title: Post.Template.AttachCrossSection()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Attach the current cross section settings to the specified template
---

## Description

Attach the current cross section settings to the specified template.

## Syntax

```psj
Post.Template.AttachCrossSection(...)
```

Macro: [AttachTemplateCrossSection](../../macro/post/AttachTemplateCrossSection)

Ribbon: <menuselection>Post &#187; Template &#187; AttachCrossSection</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of template, which will attach the cross section settings.
- The default value is "NewTemplate".

### `postDataVizOptCrossSection`

- A _[POST_DATA_VIZ_OPT_SECTION](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_CROSS_SECTION)_ specifying all settings of the cross section display.
- The default value is [POST_DATA_VIZ_OPT_SECTION](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_CROSS_SECTION).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {2-9}
Post.Template.Create(strName="Cross Section", strComment="Attach Cross Section Template")
template = Post.Template.AttachCrossSection(strName="Cross Section", 
                                        postDataVizOptCrossSection=POST_DATA_VIZ_OPT_CROSS_SECTION(
                                            bCapping=False, 
                                            bCuttingEdge=True, 
                                            bSectionElem=True, 
                                            bMeshLine=True, 
                                            dlTranslationMatrix=[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.016, 0.005, 0.0025, 1.0], 
                                            dlPosition=[0.016, 0.005, 0.0025]))
JPT.Debugger(template)
```
