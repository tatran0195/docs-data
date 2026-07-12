---
id: Post-Template-Load
title: Post.Template.Load()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Load the specified template in the template list to the current screen
---

## Description

Load the specified template in the template list to the current screen.

## Syntax

```psj
Post.Template.Load(...)
```

Macro: [LoadTemplate](../../macro/post/LoadTemplate)

Ribbon: <menuselection>Post &#187; Template &#187; Load</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of template will be loaded.
- This is a required input.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {14}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create new Template
Post.Template.Create(strName="Template_1", strComment="")
Post.Template.AttachViewPoint(
    strName="Template_1", 
    postDataVizOptViewPoint=POST_DATA_VIZ_OPT_VIEWPOINT(
        dlCenter=[0.016, 0.005, 0.0025], 
        dScaleFactor=0.0349344))

# Load template
loadTemplate = Post.Template.Load(strName="Template_1")
JPT.Debugger(loadTemplate)
```
