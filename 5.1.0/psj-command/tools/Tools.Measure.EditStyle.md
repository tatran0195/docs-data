---
id: Tools-Measure-EditStyle
title: Tools.Measure.EditStyle()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Edit style of the specified measure note
---

## Description

Edit style of the specified measure note

## Syntax

```psj
Tools.Measure.EditStyle(...)
```

Macro: [EditMeasureNoteStyle]

Ribbon: <menuselection>Tools &#187; Measure &#187; EditStyle</menuselection>

## Inputs

### `crlMeasureNote`

- A _List of Cursor_ specifying measure notes.
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

A _Boolean_ specifying the function succeeded or not.

## Sample Code

```psj{13-21}
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Distance.CreateMeasureNote.TwoNodes(
  strNoteName="Distance1", 
  crFirstNode=Node(473), 
  crSecondNode=Node(439))

#Edit the style of the Measure Note
Tools.Measure.EditStyle(
  crlMeasureNote=[MeasureNote(1)], 
  iFontColor=255, 
  iBackgroundColor=15794175,
  iOutlineWidth=3, 
  iArrowWidth=2, 
  iArrowColor=255, 
  iArrowType=1, 
  iTitleType=1)
```
