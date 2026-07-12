---
id: Tools-Measure-CreateMeasureNoteForce
title: Tools.Measure.CreateMeasureNoteForce()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a Measure Note for Measure > Force function
---

## Description

Create a Measure Note for Measure > Force function.

## Syntax

```psj
Tools.Measure.CreateMeasureNoteForce(...)
```

Macro: [CreateMeasureNoteForce]

Ribbon: <menuselection>Tools &#187; Measure &#187; CreateMeasureNoteForce</menuselection>

## Inputs

### `strNoteName`

- A _String_ specifying the name of the created note.
- This is a required input.

### `crlTargets`

- A _List of Cursor_ specifying target entities.
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

```psj{4-6}
#Please load result contains force result here.
#Input IDs of nodes to measure.
n1=1
n2=2
n3=3

Tools.Measure.CreateMeasureNoteForce(
        strNoteName="Force1", 
        crlTargets=[Node(n1, n2, n3)])
```
