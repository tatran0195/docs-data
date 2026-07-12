---
id: MainWindow-RightClick-ShowHideFlip
title: MainWindow.RightClick.ShowHideFlip()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Toggle the display of hidden parts or faces on the current document
---

## Description

Toggle the display of hidden parts or faces on the current document.

## Syntax

```psj
MainWindow.RightClick.ShowHideFlip(...)
```

Macro: [ShowHideFlip](../../macro/main-window/ShowHideFlip)

Ribbon: <menuselection>MainWindow &#187; RightClick &#187; ShowHideFlip</menuselection>

## Inputs

### `iType`

- An _Integer_ specifying the target type to toggle the displaying. The target is  Part or Face.
- The default value is 0.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {9}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=7697908)
JPT.ViewFitToModel()

# Show hide flip parts
flipPart = MainWindow.RightClick.ShowHideFlip(iType=0)
print(flipPart)
```
