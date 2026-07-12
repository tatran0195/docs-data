---
id: Home-Windows-TileVertical
title: Home.Windows.TileVertical()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Display opening documents in a vertical side-by-side arrangement
---

## Description

Display opening documents in a vertical side-by-side arrangement.

## Syntax

```psj
Home.Windows.TileVertical(...)
```

Macro: [TileVertical](../../macro/home/TileVertical), [FrameLessVerticalMode1](../../macro/home/FrameLessVerticalMode1), [FrameLessVerticalMode2](../../macro/home/FrameLessVerticalMode2), [FrameLessVerticalMode3](../../macro/home/FrameLessVerticalMode3), [FrameLessVerticalMode4](../../macro/home/FrameLessVerticalMode4), [FrameLessVerticalMode5](../../macro/home/FrameLessVerticalMode5), [FrameLessVerticalMode6](../../macro/home/FrameLessVerticalMode6), [FrameLessVerticalMode7](../../macro/home/FrameLessVerticalMode7)

Ribbon: <menuselection>Home &#187; Windows &#187; TileVertical</menuselection>

## Inputs

### `iMode`

- An _Integer_ specifying the vertical mode of arrangement.
    - 0: Tile Vertical.
    - 1: Mode 1.
    - 2: Mode 2.
    - 3: Mode 3.
    - 4: Mode 4.
    - 5: Mode 5.
    - 6: Mode 6.
    - 7: Mode 7.
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

# Tile vertical arrangement
Home.Windows.TileVertical(iMode=0)
```
