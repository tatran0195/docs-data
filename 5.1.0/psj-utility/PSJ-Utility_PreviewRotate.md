---
id: JPT-PreviewRotate
title: JPT.PreviewRotate()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Show preview result of body rotation
---

## Description

Show preview result of body rotation.

## Syntax

```psj
JPT.PreviewRotate(...)
```

## Inputs

### `DBodyVector`

- A _[DBodyVector](../data-type/psj-utility/pre-utility/built-in-types/BodyVector)_ object or _List of [DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ objects storing the information of parts to be rotated.
- This is a required input.

### `posCenter`

- A _List_ specifying the center position of rotation.
- This is a required input.

### `vecAxis`

- A _List_ specifying the axis of rotation.
- This is a required input.

### `dAngle`

- A _Double_ specifying the rotation angle in degree.
- This is a required input.

### `iColor`

- An _Integer_ specifying the color of the previewed entity.
- The default value is 255.

### `dTransparency`

- A _Double_ specifying the transparency of the previewed entity.
- The range of `dTransparency` = [0.0, 1.0]
- The default value is 0.5.

### `DCoord`

- A _[DCoord](../data-type/psj-utility/pre-utility/built-in-types/DCoord)_ object specifying Local Coordinate System.
- The default value is None (Global Coordinate System).

## Return Code

This utility function does not have output value.

## Sample Code

```psj {13}
# Clear Preview
JPT.ClearPreview()

# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube_2", iPartColor=13259210)
Tools.Coordinates.ThreeNode(iOrder=-1, crlNodes=[Node(496, 578, 590)])

# Preview
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
parts = JPT.GetAllParts()
coord = JPT.GetAllCoordinates()
JPT.PreviewRotate(parts,[0,0,0],[0,1,0],45,color,0.8,coord[0])
JPT.ViewFitToModel()
```
