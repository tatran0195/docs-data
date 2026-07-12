---
id: MainWindow-RightClick-SelectSurfaceColor
title: MainWindow.RightClick.SelectSurfaceColor()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Select faces that have the same color as the selected face.
---

## Description

Select faces that have the same color as the selected face.

## Syntax

```psj
MainWindow.RightClick.SelectSurfaceColor(...)
```

Macro: [SelectSurfaceColor](../../macro/main-window/SelectSurfaceColor)

Ribbon: <menuselection>MainWindow &#187; RightClick &#187; SelectSurfaceColor</menuselection>

## Inputs

### `crFace`

- A _Cursor_ that specify the target face.
- This is a required input.

### `bSelectFacesInSamePart`

- A _Boolean_ value that defines the search scope.
  - _True_: Searches for faces with the same color within the part that contains the face specified in `crInput`.
  - _False_: Searches for faces with the same color across the entire model.

## Return Code

- A list of _Cursor_ (string format) for the detected faces.


## Sample Code

```psj  {18-22, 25-28}
#Prepare Model
Geometry.Part.Cube(
    iPartColor=6409934
    )

Geometry.Part.Cube( 
    dlOrigin=[0.02, 0.0, 0.0], 
    strName="Cube_2", 
    iPartColor=7434735
    )

# Change the color of the specified face (Face 21)
Assembly.RightClick.ChangeEntityColor(
    crlEntities=[Face(48, 50, 47, 21, 23, 22)], 
    iColor=16776960
    )

#Get faces with the same color as Face 21 in the entire model.
blue_faces = MainWindow.RightClick.SelectSurfaceColor(
    crFace=Face(21), 
    bSelectFacesInSamePart=False
    )
JPT.Debugger(blue_faces)

#Get faces with the same color as Face 21 within its part.
blue_faces_in_cube_1 = MainWindow.RightClick.SelectSurfaceColor(
    crFace=Face(21), 
    bSelectFacesInSamePart=True
    )
JPT.Debugger(blue_faces_in_cube_1)
```
