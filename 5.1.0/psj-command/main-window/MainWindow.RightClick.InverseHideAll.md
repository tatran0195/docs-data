---
id: MainWindow-RightClick-InverseHideAll
title: MainWindow.RightClick.InverseHideAll()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Hide all targets other than the specified face. (Display only the specified faces)
---

## Description

Hide all targets other than the specified face.(Display only the specified faces)

## Syntax

```psj
MainWindow.RightClick.InverseHideAll(...)
```

Macro: [ViewInverseHideAll](../../macro/main-window/ViewInverseHideAll)

Ribbon: <menuselection>MainWindow &#187; RightClick &#187; InverseHideAll</menuselection>

## Inputs

### `crlTargets`

- A _List of Cursor_ specifying the target faces to display only.
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
target = MainWindow.RightClick.InverseHideAll(crlTargets=[Face(26)])
JPT.Debugger(target)
```
