---
id: Tools-Measure-Distance-CreateMeasureNote-TwoPoints
title: Tools.Measure.Distance.CreateMeasureNote.TwoPoints()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a Measure Note for Measure > Distance > Two Points function
---

## Description

Create a Measure Note for Measure > Distance > Two Points function.

## Syntax

```psj
Tools.Measure.Distance.CreateMeasureNote.TwoPoints(...)
```

Macro: [CreateMeasureNoteDistanceBy2Points]

Ribbon: <menuselection>Tools &#187; Measure &#187; Distance &#187; CreateMeasureNote &#187; TwoPoints</menuselection>

## Inputs

### `strNoteName`

- A _String_ specifying the name of the created note.
- This is a required input.

### `dlFirstPoint`

- A _List of Double_ specifying the first point.
- This is a required input.

### `dlSecondPoint`

- A _List of Double_ specifying the second point.
- This is a required input.

### `crCoordinate`

- A _Cursor_ specifying a local coordinate.
- The default value is _None_.

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

```psj{7-10}
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Distance.CreateMeasureNote.TwoPoints(
  strNoteName="Distance1", 
  dlFirstPoint=[0.007, 0.0036, 0.01], 
  dlSecondPoint=[0.001, 0.005, 0.01])
```
