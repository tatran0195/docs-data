---
id: Post-SetNote-ResultUnit
title: Post.SetNote.ResultUnit()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set to display the unit of data in the note window
---

## Description

Set to display the unit of data in the note window

## Syntax

```psj
Post.SetNote.ResultUnit(...)
```

Macro: [SetNoteResultUnit](../../macro/post/SetNoteResultUnit)

Ribbon: <menuselection>Post &#187; SetNote &#187; ResultUnit</menuselection>

## Inputs

### `bNoteResultUnit`

- A _Boolean_ specifying whether to display the unit of data in the note window.
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {25}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Plot the result
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Displacement", 
                strResultCompName="Translational", 
                iResultPos=1), 
                postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=4))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))
Post.Note.Node(crlTargets=[RONode(133)])

# Hide Unit of data
Post.SetNote.ResultUnit(bNoteResultUnit=False)
```
