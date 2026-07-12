---
id: Home-Windows-TileHorizontal
title: Home.Windows.TileHorizontal()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Display opening documents in a horizontal arrangement
---

## Description

Display opening documents in a horizontal arrangement.

## Syntax

```psj
Home.Windows.TileHorizontal(...)
```

Macro: [TileHorizontal](../../macro/home/TileHorizontal), [FrameLessHorizontalMode1](../../macro/home/FrameLessHorizontalMode1), [FrameLessHorizontalMode2](../../macro/home/FrameLessHorizontalMode2), [FrameLessHorizontalMode3](../../macro/home/FrameLessHorizontalMode3), [FrameLessHorizontalMode4](../../macro/home/FrameLessHorizontalMode4), [FrameLessHorizontalMode5](../../macro/home/FrameLessHorizontalMode5), [FrameLessHorizontalMode6](../../macro/home/FrameLessHorizontalMode6), [FrameLessHorizontalMode7](../../macro/home/FrameLessHorizontalMode7)



Ribbon: <menuselection>Home &#187; Windows &#187; TileHorizontal</menuselection>

## Inputs

### `iMode`

- An _Integer_ specifying the horizontal mode of arrangement.
    - 0: Tile Horizontal.
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

# Tile horizontal arrangement
Home.Windows.TileHorizontal(iMode=0)
```
