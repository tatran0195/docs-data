---
id: Tools-Measure-Area-CreateMeasureNote-Element
title: Tools.Measure.Area.CreateMeasureNote.Element()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a Measure Note for Measure > Area > Element
---

## Description

Create a Measure Note for Measure > Area > Element

## Syntax

```psj
Tools.Measure.Area.CreateMeasureNote.Element(...)
```

Macro: [CreateMeasureNoteAreaElem]

Ribbon: <menuselection>Tools &#187; Measure &#187; Area &#187; CreateMeasureNote &#187; Element</menuselection>

## Inputs

### `strNoteName`

- A _String_ specifying the name of the created note.
- This is a required input.

### `crlElements`

- A _List of Cursor_ specifying elements.
- This is a required input.

### `crCoordinate`

- A _Cursor_ specifying local coordinate.
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

```psj{7-9}
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Area.CreateMeasureNote.Element(
    strNoteName="Area1", 
    crlElements=[Elem(233, 216, 215, 197, 198, 180)])
```
