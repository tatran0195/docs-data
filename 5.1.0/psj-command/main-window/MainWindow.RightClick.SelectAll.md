---
id: MainWindow-RightClick-SelectAll
title: MainWindow.RightClick.SelectAll()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Select all faces or shell elements according to the specified target type
---

## Description

Select all faces or shell elements according to the specified target type.

## Syntax

```psj
MainWindow.RightClick.SelectAll(...)
```

Macro: [ViewSelectAll](../../macro/main-window/ViewSelectAll)

Ribbon: <menuselection>MainWindow &#187; RightClick &#187; SelectAll</menuselection>

## Inputs

### `iTargetType`

- An _Integer_ specifying the target type to be selected. The target can be face or 2D element only.
- This is a required input.

## Return Code

A _List of Cursor_ specifying the selected targets.

## Sample Code

```psj {7,11}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
JPT.ViewFitToModel()

# Select all faces
listFaces = MainWindow.RightClick.SelectAll(iTargetType=3)
print(listFaces)

# Select all 2D elements
listElems= MainWindow.RightClick.SelectAll(iTargetType=7)
print(listElems)
```
