---
id: MainWindow-RightClick-InverseHide
title: MainWindow.RightClick.InverseHide()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Invert hide targets by context menu
---

## Description

Invert hide targets by context menu

## Syntax

```psj
MainWindow.RightClick.InverseHide(...)
```

Macro: [ViewInverseHide](../../macro/main-window/ViewInverseHide)

Ribbon: <menuselection>MainWindow &#187; RightClick &#187; InverseHide</menuselection>

## Inputs

### `crlTargets`

- A _List of Cursor_ specifying the targets to be inverted hide. The target can be Part or Face.
- The default value is [].

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {7}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
JPT.ViewFitToModel()

# Invert hide Part(1)
target = MainWindow.RightClick.InverseHide(crlTargets=[Part(1)])
JPT.Debugger(target)
```
