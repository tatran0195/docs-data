---
id: Home-Windows-TileBox
title: Home.Windows.TileBox()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Display opening documents in vertical and horizontal arrangement like a box
---

## Description

Display opening documents in vertical and horizontal arrangement like a box.

## Syntax

```psj
Home.Windows.TileBox(...)
```

Macro: [FrameLessBoxMode1](../../macro/home/FrameLessBoxMode1), [FrameLessBoxMode2](../../macro/home/FrameLessBoxMode2)

Ribbon: <menuselection>Home &#187; Windows &#187; TileBox</menuselection>

## Inputs

### `iMode`

- An _Integer_ specifying the mode of arrangement.
    - 1: Mode 1.
    - 2: Mode 2.
- This is a required input.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {10}
# Prepare 2 JPT documents
Geometry.Part.Cube()
JPT.ViewFitToModel()
JPT.CreateNewDocument()
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
JPT.ViewFitToModel()

# Tile box arrangement
Home.Windows.TileBox(iMode=1)
```
