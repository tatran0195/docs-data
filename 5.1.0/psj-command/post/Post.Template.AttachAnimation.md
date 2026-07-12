---
id: Post-Template-AttachAnimation
title: Post.Template.AttachAnimation()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Attach the current animation settings to the specified template
---

## Description

Attach the current animation settings to the specified template.

## Syntax

```psj
Post.Template.AttachAnimation(...)
```

Macro: [AttachTemplateAnimation](../../macro/post/AttachTemplateAnimation)

Ribbon: <menuselection>Post &#187; Template &#187; AttachAnimation</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of template, which will attach the animation settings.
- The default value is "NewTemplate".

### `postDataVizOptAnimation`

- A _[POST_DATA_VIZ_OPT_ANIMATION](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_ANIMATION)_ specifying all settings of the animation display.
- The default value is [POST_DATA_VIZ_OPT_ANIMATION](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_ANIMATION).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {2-7}
Post.Template.Create(strName="Animation_Template", strComment="Attach Animation Template")
template = Post.Template.AttachAnimation(strName="Animation_Template", 
                                        postDataVizOptAnimation=POST_DATA_VIZ_OPT_ANIMATION(
                                            iFPS=10, 
                                            iFrameNumber=10, 
                                            iLoopType=0, 
                                            bPhaseAngle=True))
JPT.Debugger(template)
```
