---
id: Post-SetNote-ResultTitle
title: Post.SetNote.ResultTitle()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set to display the entire component title in the note window
---

## Description

Set the display of the entire component title in the note window.

## Syntax

```psj
Post.SetNote.ResultTitle(...)
```

Macro: [SetNoteResultTitle](../../macro/post/SetNoteResultTitle)

Ribbon: <menuselection>Post &#187; SetNote &#187; ResultTitle</menuselection>

## Inputs

### `bNoteResultTitle`

- A _Boolean_ specifying whether to display the entire component title in the note window.
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
                strResultName="Stress", 
                strResultCompName="Mises", 
                iResultPos=2), 
                postDataOp=PostDataOp(iResultLocation=2))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Stress", 
                    strResultCompName="Mises"))
Post.Note.Element(crlTargets=[ROElem(448)])

# Hide all component titles
Post.SetNote.ResultTitle(bNoteResultTitle=False)
```
