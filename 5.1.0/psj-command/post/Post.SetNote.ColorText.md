---
id: Post-SetNote-ColorText
title: Post.SetNote.ColorText()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set the text color and thickness of the character in the Note window
---

## Description

Set the text color and thickness of the character in the Note window.

## Syntax

```psj
Post.SetNote.ColorText(...)
```

Macro: [SetNoteColorText](../../macro/post/SetNoteColorText)

Ribbon: <menuselection>Post &#187; SetNote &#187; ColorText</menuselection>

## Inputs

### `iTextColor`

- An _Integer_ specifying the text color.
- The default value is 0.

### `iTextSize`

- An _Integer_ specifying the text size.
- The default value is 14.

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

# Modify the text color and text size
Post.Note.Node(crlTargets=[RONode(133)])
Post.SetNote.ColorText(iTextColor=42495, iTextSize=18)
```
