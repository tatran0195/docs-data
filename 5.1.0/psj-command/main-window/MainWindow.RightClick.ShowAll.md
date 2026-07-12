---
id: MainWindow-RightClick-ShowAll
title: MainWindow.RightClick.ShowAll()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Show all hidden entities 
---

## Description

Show all hidden entities.

## Syntax

```psj
MainWindow.RightClick.ShowAll(...)
```

Macro: [ViewShowAll](../../macro/main-window/ViewShowAll)

Ribbon: <menuselection>MainWindow &#187; RightClick &#187; ShowAll</menuselection>

## Inputs

This function does not require any input value.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {11}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=7697908)
JPT.ViewFitToModel()

# Hide some parts
JPT.Exec("Show_Entity([3:2, 3:3], 0)")
# Show all parts again
MainWindow.RightClick.ShowAll()
```
