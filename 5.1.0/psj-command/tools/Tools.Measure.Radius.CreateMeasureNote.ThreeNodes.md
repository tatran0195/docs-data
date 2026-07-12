---
id: Tools-Measure-Radius-CreateMeasureNote-ThreeNodes
title: Tools.Measure.Radius.CreateMeasureNote.ThreeNodes()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a Measure Note for Measure > Radius > 3 Nodes function
---

## Description

Create a Measure Note for Measure > Radius > 3 Nodes function.

## Syntax

```psj
Tools.Measure.Radius.CreateMeasureNote.ThreeNodes(...)
```

Macro: [CreateMeasureNoteRadiusBy3Nodes]

Ribbon: <menuselection>Tools &#187; Measure &#187; Radius &#187; CreateMeasureNote &#187; ThreeNodes</menuselection>

## Inputs

### `strNoteName`

- A _String_ specifying the name of the created note.
- This is a required input.

### `crFirstNode`

- A _Cursor_ specifying the first node.
- This is a required input.

### `crSecondNode`

- A _Cursor_ specifying the second node.
- This is a required input.

### `crThirdNode`

- A _Cursor_ specifying the third node.
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

```psj{7-11}
#Preapre model
Geometry.Part.Cylinder(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Radius.CreateMeasureNote.ThreeNodes(
  strNoteName="Radius1", 
  crFirstNode=Node(70), 
  crSecondNode=Node(46), 
  crThirdNode=Node(16))
```
