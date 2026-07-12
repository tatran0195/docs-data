---
id: Post-Template-AttachDiagram
title: Post.Template.AttachDiagram()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Attach the current diagram settings to the specified template
---

## Description

Attach the current diagram settings to the specified template.

## Syntax

```psj
Post.Template.AttachDiagram(...)
```

Macro: [AttachTemplateDiagram](../../macro/post/AttachTemplateDiagram)

Ribbon: <menuselection>Post &#187; Template &#187; AttachDiagram</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of template, which will attach the diagram settings.
- The default value is "NewTemplate".

### `postDataVizOptDiagram`

- A _[POST_DATA_VIZ_OPT_DIAGRAM](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_DIAGRAM)_ specifying all settings of the diagram display.
- The default value is [POST_DATA_VIZ_OPT_DIAGRAM](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_DIAGRAM).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {2-5}
Post.Template.Create(strName="Diagram_Template", strComment="Attach Diagram Template")
template = Post.Template.AttachDiagram(strName="Diagram_Template", 
                                    postDataVizOptDiagram=POST_DATA_VIZ_OPT_DIAGRAM(
                                        dRatioModel=0.05, 
                                        dRatioScreen=0.05))
JPT.Debugger(template)
```
