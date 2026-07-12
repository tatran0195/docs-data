---
id: Post-ShowDeformation
title: Post.ShowDeformation()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Load deformation on the model.
---

## Description

Load deformation on the model.

## Syntax

```psj
Post.ShowDeformation(...)
```

Macro: CmdShowPostDeformation

Ribbon: <menuselection>Post &#187; ShowDeformation</menuselection>

## Inputs

### `crPostJob`

- A _Cursor_ specifying the Post job result (post data).
- This is a required input.

### `postResultKey`

- A _[POST_RESULT_KEY](./../../data-type/psj-command/parameter-types/POST_RESULT_KEY)_ specifying result to show deformation.
- This is a required input.

### `postDataOption`

- A _[PostDataOp](./../../data-type/psj-command/parameter-types/POST_DATA_OPTION)_ specifying result options.

## Return Code

True if success, or False if failed.

## Sample Code

```psj {19-26}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath)

# Load contour
Post.ShowContour(
    crPostJob=TSVPostJob(1), 
    lContourSettings=[
        PostContourSetting(
            postResultKey=PostResultKey(
                iAnalysisType=1, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Displacement", 
                strResultCompName="Translational", 
                iResultPos=1), 
            postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])

Post.ShowDeformation(
    crPostJob=TSVPostJob(1), 
    postResultKey=PostResultKey(
        iAnalysisType=1, 
        iResultSet=1, 
        iTimeStep=1, 
        strResultName="Displacement", 
        strResultCompName="Translational"))

Post.EnableMiddleNodes()
```
