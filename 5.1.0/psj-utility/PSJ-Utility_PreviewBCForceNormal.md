---
id: JPT-PreviewBCForceNormal
title: JPT.PreviewBCForceNormal()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Show preview result of applying normal force on target
---

## Description

Show preview result of applying normal force on target.

## Syntax

```psj
JPT.PreviewBCForceNormal(...)
```

## Inputs

### `DElemForNormal`

- A _[DElem](../data-type/psj-utility/pre-utility/built-in-types/DElem)_ object specifying 2D element information.
- This element will be used to calculate normal vector for force direction.
- This is a required input.

### `DItemVector`

- A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects storing the information of targets for applying force.
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

```psj {12}
# Clear Preview
JPT.ClearPreview()

# Prepare model
Geometry.Part.Cube()

# Preview
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
selFace = JPT.GetEntitiesByID(JPT.DItemType.FACE, 26)
normalElem = JPT.GetEntitiesByID(JPT.DItemType.ELEM, 1065)
normalElem = JPT.CastDItemToDElem(normalElem[0])
JPT.PreviewBCForceNormal(normalElem,selFace,0,color,0.8)
JPT.ViewFitToModel()
```
