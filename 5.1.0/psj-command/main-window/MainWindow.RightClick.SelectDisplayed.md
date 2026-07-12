---
id: MainWindow-RightClick-SelectDisplayed
title: MainWindow.RightClick.SelectDisplayed()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Select all targets of the same type as the specified target that are displayed in the current document
---

## Description

Select all targets of the same type as the specified target that are displayed in the current document.

## Syntax

```psj
MainWindow.RightClick.SelectDisplayed(...)
```

Macro: [ViewSelectDisplayed](../../macro/main-window/ViewSelectDisplayed)

Ribbon: <menuselection>MainWindow &#187; RightClick &#187; SelectDisplayed</menuselection>

## Inputs

### `iTargetType`

- An _Integer_ specifying the target type to be selected. The targets can only be faces or 2D elements.
- This is a required input.

## Return Code

A _List of Cursor_ specifying the selected faces or 2D elements.

## Sample Code

```psj {11}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
JPT.ViewFitToModel()

# Hide some faces
JPT.Exec("Show_Entity([6:52, 6:78], 0)")

# Select on displaying faces
displayFaces = MainWindow.RightClick.SelectDisplayed(iTargetType=3)
if displayFaces is None:
    print("There is no displaying faces")
elif len(displayFaces) == 1:
    print("1 displaying face was selected")
    print(displayFaces)
else:
    print(str(len(displayFaces)) + " displaying faces were selected")
    print(displayFaces)
```
