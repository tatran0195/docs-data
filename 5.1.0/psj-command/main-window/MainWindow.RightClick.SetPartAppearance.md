---
id: MainWindow-RightClick-SetPartAppearance
title: MainWindow.RightClick.SetPartAppearance()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set the appearance of the selected parts
---

## Description

Set the appearance of the selected parts.

## Syntax

```psj
MainWindow.RightClick.SetPartAppearance(...)
```

Macro: SetPartAppearance

Ribbon: <menuselection>MainWindow &#187; RightClick &#187; SetPartAppearance</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying 
- This is a required input.

### `strType`

- A _String_ specifying appearance target.
    - "Surface"
    - "Mesh"
    - "Edge"
    - "Node"
- This is a required input.

### `bShow`

- A _Boolean_ specifying Show or Hide.
- The default value is _True_ (Show).

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {8-13}
# Prepare model
JPT.Exec('ViewShowMesh(1)')
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=7697908)

MainWindow.RightClick.SetPartAppearance(crlParts=[Part(1)], strType="Surface", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(2)], strType="Edge", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(3)], strType="Mesh", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(4)], strType="Node", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(4)], strType="Surface", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(4)], strType="Mesh", bShow=False)

JPT.ViewFitToModel()

```
