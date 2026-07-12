---
id: Home-RectangularCapture-Multiple
title: Home.RectangularCapture.Multiple()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a frame for Multiple capture and save it in the “User Frame” tree of the ViewPoint window. The created frame will be used with the "To PPT" and "To Image" command
---

## Description

Create a frame for Multiple capture and save it in the “User Frame” tree of the ViewPoint window. The created frame will be used with the "To PPT" and "To Image" command.

## Syntax

```psj
Home.RectangularCapture.Multiple(...)
```

Macro: [ViewMakeUserFrame](../../macro/home/ViewMakeUserFrame)

Ribbon: <menuselection>Home &#187; RectangularCapture &#187; Multiple</menuselection>

## Inputs

### `strFrameName`

- A _String_ specifying the name of frame to be captured.
- This is a required input.

### `iStartPointX`

- An _Integer_ specifying the x-coordinate of the start point of the frame.
- This is a required input.

### `iStartPointY`

- An _Integer_ specifying the y-coordinate of the start point of the frame.
- This is a required input.

### `iWidth`

- An _Integer_ specifying the width of the frame size.
- This is a required input.

### `iHeight`

- An _Integer_ specifying the height of the frame size.
- This is a required input.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {26-27}
# Prepare model
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

# Create a multiple frames
Home.RectangularCapture.Multiple(strFrameName="New_Frame_1 ((Multiple))", iStartPointX=459, iStartPointY=212, 
                                iWidth=460, iHeight=214)
Home.ToPPTX()
```
