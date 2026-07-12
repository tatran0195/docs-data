---
id: JPT-PreviewScaling
title: JPT.PreviewScaling()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Show preview result of body scaling
---

## Description

Show preview result of body scaling.

## Syntax

```psj
JPT.PreviewScaling(...)
```

## Inputs

### `DBodyVector`

- A _[DBodyVector](../data-type/psj-utility/pre-utility/built-in-types/BodyVector)_ object or _List of [DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ objects storing the information of parts to be scaled.
- This is a required input.

### `dlScaleVector`

- A _List of Double_ specifying the scale vector. It defines how much scaling is used in each direction.
- This is a required input.

### `dlScaleCenter`

- A _List of Double_ specifying the scale center position. It defines a point where the scaling should be started.
- This is a required input.

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

```psj {11}
# Clear Preview
JPT.ClearPreview()

# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube_2", iPartColor=13259210)

# Preview
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
parts = JPT.GetAllParts()
JPT.PreviewScaling(parts,[2.1,1.1,1.1],[0,0,0],color,0.2)
JPT.ViewFitToModel()
```
