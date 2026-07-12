---
id: Post-SetNote-ResultNumber
title: Post.SetNote.ResultNumber()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set the display of result number in the note window.
---

## Description

Set the display of result number in the note window.

## Syntax

```psj
Post.SetNote.ResultNumber(...)
```

Ribbon: <menuselection>Post &#187; SetNote &#187; ResultNumber</menuselection>

## Inputs

### `bNoteResultNumber`

- A _Boolean_ specifying whether to display the result number in the note window.
- The default value is _True_.

### `iNoteResultNumber`

- An _Integer_ specifying the method to display the result number title as default or user-defined name.
    - 0: Default
    - 1: User-Defined
- The default value is 0.

### `strNoteResultNumber`

- A _String_ specifying an arbitrary user-defined name for the result number title. This option is used when _iNoteResultNumber_= 1.
- The default value is "".

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {25,27}
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
Post.Note.Position(crElement=ROElem(448), dlPosition=[28.588114, 6.313289, 5.0])

# Hide Result Number information
Post.SetNote.ResultNumber(bNoteResultNumber=False)
# User defines Result Number title
Post.SetNote.ResultNumber(iNoteResultNumber=1, strNoteResultNumber="Result Number")
```
