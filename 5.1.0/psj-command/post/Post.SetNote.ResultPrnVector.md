---
id: Post-SetNote-ResultPrnVector
title: Post.SetNote.ResultPrnVector()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set the display of principal stress/principal strain unit vector in the note window
---

## Description

Set the display of principal stress/principal strain unit vector in the note window.

## Syntax

```psj
Post.SetNote.ResultPrnVector(...)
```

Macro: [SetNoteResultPrnVector](../../macro/post/SetNoteResultPrnVector)

Ribbon: <menuselection>Post &#187; SetNote &#187; ResultPrnVector</menuselection>

## Inputs

### `bNoteResultPrnVector`

- A _Boolean_ specifying whether to display the principal stress/principal strain unit vector in the note window.
- The default value is _True_.

### `iNoteResultPrnVector`

- An _Integer_ specifying the method to display the principal stress/principal strain unit vector title as default or user-defined name.
    - 0: Default
    - 1: User-Defined
- The default value is 0.

### `strNoteResultPrnVector`

- A _String_ specifying an arbitrary user-defined name for the principal stress/principal strain vector. This option was used when _iNoteResultPrnVector_= 1.
- The default value is "".

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {28,30}
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
                strResultCompName="Max Principal Stress", 
                iResultPos=4), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=1, 
                iOptionConversion=1, 
                iOptionContinuous=8))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Stress", 
                    strResultCompName="Max Principal Stress"))
Post.Note.Node(crlTargets=[RONode(133)])

# Hide Principal stress direction
Post.SetNote.ResultPrnVector(bNoteResultPrnVector=False)
# User defines Principal stress direction title
Post.SetNote.ResultPrnVector(iNoteResultPrnVector=1, strNoteResultPrnVector="Direction")
```
