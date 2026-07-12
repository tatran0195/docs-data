---
id: MainWindow-RightClick-SelectReverse
title: MainWindow.RightClick.SelectReverse()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Reverse the selection on the displaying bodies.
---

## Description

Reverse the selection on the displaying bodies.

## Syntax

```psj
MainWindow.RightClick.SelectReverse(...)
```

Macro: [ViewSelectReverse](../../macro/main-window/ViewSelectReverse)

Ribbon: <menuselection>MainWindow &#187; RightClick &#187; SelectReverse</menuselection>

## Inputs

### `iTargetType`

- An _Integer_ specifying the target type to select entities in reverse. The targets can only be faces or 2D elements.
- This is a required input.

### `crlTargets`

- A _List of Cursor_ specifying the targets will reverse the selection.
- The default value is [].

## Return Code

A _List of Cursor_ specifying the selected entities in revert.

## Sample Code

```psj {8}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
JPT.ViewFitToModel()

# Revert selection from Face(26)
revertFaces = MainWindow.RightClick.SelectReverse(iTargetType=3, crlTargets=[Face(26)])
print(revertFaces)
```
