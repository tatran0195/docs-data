---
id: Post-Template-Delete
title: Post.Template.Delete()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Delete a specified template
---

## Description

Delete a specified template.

## Syntax

```psj
Post.Template.Delete(...)
```

Macro: [DeleteTemplate](../../macro/post/DeleteTemplate)

Ribbon: <menuselection>Post &#187; Template &#187; Delete</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of template will be deleted.
- This is a required input.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {13}
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
Post.Template.Copy(strCurrentTemplate="Template_1", strNewTemplate="Template_2")
Post.Template.Delete(strName="Template_2")
```
