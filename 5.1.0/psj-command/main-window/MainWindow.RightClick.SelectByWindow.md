---
id: MainWindow-RightClick-SelectByWindow
title: MainWindow.RightClick.SelectByWindow()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Select all targets of the same type as the specified one that is displaying the working window region
---

## Description

Select all targets of the same type as the specified one that is displaying the working window region.

## Syntax

```psj
MainWindow.RightClick.SelectByWindow(...)
```

Macro: [ViewSelectByWindow](../../macro/main-window/ViewSelectByWindow)

Ribbon: <menuselection>MainWindow &#187; RightClick &#187; SelectByWindow</menuselection>

## Inputs

### `iTargetType`

- An _Integer_ specifying the target type to be selected.
- This is a required input.

## Return Code

A _List of Cursor_ specifying the selected faces or 2D elements

## Sample Code

```psj {8}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
JPT.ViewFitToModel()

# Select on displaying faces  
displayFaces = MainWindow.RightClick.SelectByWindow(iTargetType=3)
if displayFaces is None:
    print("There is no face on current window")
elif len(displayFaces) == 1:
    print("1 displaying face was selected")
    print(displayFaces)
else:
    print(str(len(displayFaces)) + " displaying faces were selected")
    print(displayFaces)
```
