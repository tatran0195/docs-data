---
id: Post-Note-SearchPositions
title: Post.Note.SearchPositions()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Search point and markup its position note
---

## Description

Search point and markup its position note.

## Syntax

```psj
Post.Note.SearchPositions(...)
```

Macro: [CmdMarkupSearchPoint](../../macro/post/CmdMarkupSearchPoint),
       [CmdMarkupSearchMultiPoints](../../macro/post/CmdMarkupSearchMultiPoints) 

Ribbon: <menuselection>Post &#187; Note &#187; SearchPositions</menuselection>

## Inputs

### `dlPositions`

- A _List of Double_ specifying the coordinates of points for searching.
- This is a required input.

### `dTolerance`

- A _Double_ specifying the tolerance value for searching.
- The default value is 0.0.

### `bSearch`

- A _Boolean_ specifying whether to search only on the displayed parts or all parts of the model. 
- The default value is _False_.

## Return Code

- A list of _Boolean_ specifying whether the search target is successfully found or not.
    - _True_: The target is found.
    - _False_: The target is not found.

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
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=4))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))

# Search and display note at points
ret=Post.Note.SearchPositions(
        dlPositions=[
            [0.0, 0.0, 0.0], 
            [22.0, 5.0, 5.0], 
            [22.0, 10.0, 5.0], 
            [10.0, 10.0, 10.0]], 
        dTolerance=0.01)
        
# >> [1,1,1,0] First 3 points are found, last 1 point is not found.
print(ret)

```
