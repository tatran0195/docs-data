---
id: Post-ShowContour
title: Post.ShowContour()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Load result on model and show contour.
---

## Description

Load result on model and show contour.

## Syntax

```psj
Post.ShowContour(...)
```

Macro: CmdShowPostContour

Ribbon: <menuselection>Post &#187; ShowContour</menuselection>

## Inputs

### `crPostJob`

- A _Cursor_ specifying the Post job result (post data).
- This is a required input.

### `lContourSettings`

- A _list of [POST_CONTOUR_SETTINGS](./../../data-type/psj-command/parameter-types/POST_CONTOUR_SETTING)_ specifying the setting for contour of 1st result (required) and 2 additional results (optional). 
- This is a required input.

### `bEnableMidNode`

- A _Boolean_ specifying whether or not enable result option.
- The default value is _False_.

### `bApplyAll`

- A _Boolean_ specifying whether or not apply above settings to all active Post documents.
- The default value is _False_.

## Return Code

- A _Boolean_ specifying if the contour can be showed or not.

## Sample Code

```psj {6-17}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath)

# Show contour
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
