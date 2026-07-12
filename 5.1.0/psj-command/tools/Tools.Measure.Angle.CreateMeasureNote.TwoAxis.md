---
id: Tools-Measure-Angle-CreateMeasureNote-TwoAxis
title: Tools.Measure.Angle.CreateMeasureNote.TwoAxis()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a Measure Note for Measure > Angle > 2 Axes function
---

## Description

Create a Measure Note for Measure > Angle > 2 Axes function

## Syntax

```psj
Tools.Measure.Angle.CreateMeasureNote.TwoAxis(...)
```

Macro: [CreateMeasureNoteAngleBy2Axis]

Ribbon: <menuselection>Tools &#187; Measure &#187; Angle &#187; CreateMeasureNote &#187; TwoAxis</menuselection>

## Inputs

### `strNoteName`

- A _String_ specifying the name of the created note.
- This is a required input.

### `iAxis`

- An _Integer_ specifying an axis.
- This is a required input.

### `crCoordinate`

- A _Cursor_ specifying coordinate of the axis.
- The default value is _None_.

### `crCoordinateRef`

- A _Cursor_ specifying reference coordinate of the reference axis.
- This is a required input.

### `iAxisRef`

- An _Integer_ specifying a reference axis.
- This is a required input.



### `iFontSize`

- An _Integer_ specifying font size.
- The default value is 16.

### `iFontColor`

- An _Integer_ specifying font color.
- The default value is 0.

### `bBold`

- A _Boolean_ specifying bold type or not.
- The default value is _False_.

### `iBackgroundColor`

- An _Integer_ specifying background color.
- The default value is 16777215.

### `iOutlineWidth`

- An _Integer_ specifying outline width.
- The default value is 1.

### `iOutlineColor`

- An _Integer_ specifying outline color.
- The default value is 0.

### `iArrowWidth`

- An _Integer_ specifying arrow width.
- The default value is 1.

### `iArrowColor`

- An _Integer_ specifying arrow color.
- The default value is 0.

### `iArrowType`

- An _Integer_ specifying arrow type.
  - 0: None.
  - 1: Arrow.
- The default value is 1.

### `iTitleType`

- An _Integer_ specifying title type.
  - 0: None.
  - 1: Measure type.
  - 2: Name of note.
- The default value is 1.

## Return Code

A _CursorStr_ specifying created note.

## Sample Code

```psj{9-14}
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
Tools.Coordinates.ThreeNode(strName="CRect_1", crlNodes=[Node(6, 437, 472)])
Tools.Coordinates.ThreeNode(strName="CRect_2", crlNodes=[Node(370, 186, 170)])
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Angle.CreateMeasureNote.TwoAxis(
  strNoteName="Angle1", 
  iAxis=0, 
  crCoordinateRef=Coord(2),
  iAxisRef=0, 
  crCoordinate=Coord(1))
```
