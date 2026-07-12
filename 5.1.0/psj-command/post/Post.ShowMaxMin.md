---
id: Post-ShowMaxMin
title: Post.ShowMaxMin()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Show the label of the Max/Min value of the currently displayed result model
---

## Description

Show the label of the Max/Min value of the currently displayed result model.

## Syntax

```psj
Post.ShowMaxMin(...)
```

Macro: [CmdShowHideMaxMin](../../macro/post/CmdShowHideMaxMin)

Ribbon: <menuselection>Post &#187; ShowMaxMin</menuselection>

## Inputs

### `bShowHide`

- A _Boolean_ specifying whether to show/hide the max/min labels.
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {17}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Displacement", 
                strResultCompName="Translational", 
                iResultPos=1), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=1))])

# Show Max/Min
Post.ShowMaxMin()
```
