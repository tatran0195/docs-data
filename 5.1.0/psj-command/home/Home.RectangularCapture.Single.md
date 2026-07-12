---
id: Home-RectangularCapture-Single
title: Home.RectangularCapture.Single()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a frame for Single capture and save it in the “User Frame” tree of the ViewPoint window. The created frame will be used with the "To PPT" and "To Image" command
---

## Description

Create a frame for Single capture and save it in the “User Frame” tree of the ViewPoint window. The created frame will be used with the "To PPT" and "To Image" command.

## Syntax

```psj
Home.RectangularCapture.Single(...)
```

Macro: [ViewMakeUserFrame](../../macro/home/ViewMakeUserFrame)

Ribbon: <menuselection>Home &#187; RectangularCapture &#187; Single</menuselection>

## Inputs

### `strFrameName`

- A _String_ specifying the name of frame to be captured.
- This is a required input.

### `iStartPointX`

- An _Integer_ specifying the x-coordinate of the start point of the frame.
- This is a required input.

### `iStartPointY`

- An _Integer_ specifying the x-coordinate of the start point of the frame.
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

```psj {6-7}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)

# Create a single frame
Home.RectangularCapture.Single(strFrameName="New_Frame_1 (Single)", iStartPointX=459, iStartPointY=212, 
                                iWidth=460, iHeight=214)
Home.ToPPTX()
```
