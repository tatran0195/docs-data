---
id: JPT-PreviewBCPressureGeneral
title: JPT.PreviewBCPressureGeneral()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Show preview result of applying general pressure on target
---

## Description

Show preview result of applying general pressure on target.

## Syntax

```psj
JPT.PreviewBCPressureGeneral(...)
```

## Inputs

### `DItemVector`

- A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects storing the information of targets for applying pressure.
- This targets can be Face, Edge or Node.
- This is a required input.

### `iArrowDir`

- An _Integer_ specifying the display arrow direction.
  - 0: Start at node.
  - 1: End at node.
- The default value is 0.

### `iColor`

- An _Integer_ specifying the color of the previewed entity.
- The default value is 255.

### `dTransparency`

- A _Double_ specifying the transparency of the previewed entity.
- The range of `dTransparency` = [0.0, 1.0]
- The default value is 0.5.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {10}
# Clear Preview
JPT.ClearPreview()

# Prepare model
Geometry.Part.Cube()

# Preview
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
selFace = JPT.GetEntitiesByID(JPT.DItemType.FACE, 26)
JPT.PreviewBCPressureGeneral(selFace,1,color,0.8)
JPT.ViewFitToModel()
```
