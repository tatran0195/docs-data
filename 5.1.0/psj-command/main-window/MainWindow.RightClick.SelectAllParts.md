---
id: MainWindow-RightClick-SelectAllParts
title: MainWindow.RightClick.SelectAllParts()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Select all parts in the current document
---

## Description

Select all parts in the current document

## Syntax

```psj
MainWindow.RightClick.SelectAllParts(...)
```

Macro: [ViewSelectAllParts](../../macro/main-window/ViewSelectAllParts)

Ribbon: <menuselection>MainWindow &#187; RightClick &#187; SelectAllParts</menuselection>

## Inputs

This function does not require any input value.

## Return Code

A _List of Cursor_ specifying the selected parts.

## Sample Code

```psj {9}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=7697908)
JPT.Exec("View Fit To Model()")

# Select all parts
listParts = MainWindow.RightClick.SelectAllParts()
print(listParts)
```
