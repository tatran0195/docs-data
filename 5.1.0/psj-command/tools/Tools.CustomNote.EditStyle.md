---
id: Tools-CustomNote-EditStyle
title: Tools.CustomNote.EditStyle()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Edit style of indicated custom notes.
---

## Description

Edit style of indicated custom notes.

## Syntax

```psj
Tools.CustomNote.EditStyle(...)
```

Macro: EditCustomNoteStyle

Ribbon: <menuselection>Tools &#187; CustomNote &#187; EditStyle</menuselection>

## Inputs

### `crlTargets`

- A _List of Cursor_ specifying custom notes or collections to edit style.
- The default value is [].

### `iFontSize`

- An _Integer_ specifying font size.
- The default value is 16.

### `iFontColor`

- An _Integer_ specifying font color.
- The default value is 0.

### `bBold`

- A _Boolean_ specifying font bold.
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

- An _Integer_ specifying type of arrow.
  - 0 : None
  - 1 : Arrow
- The default value is 1.

### `iAlignment`

- An _Integer_ specifying alignment.
  - 0: Left
  - 1: Center
  - 2: Right
- The default value is 0.

## Return Code

A _Boolean_ specifying edit custom note style works successfully or not.

## Sample Code

```psj{22-26}
Geometry.Part.Cube(strName="Cube_1", iPartColor=6409934)

Tools.CustomNote(
    strNoteName="CustomNote_1", 
    dlNotePosition=[0.0, 0.01, 0.01],
    iTargetEntityType=1, crTarget=Node(8), 
    strParentName="Collection_1", 
    listContent=["My Custom Note 1"], 
    iFontSize=11, 
    bBold=True)

Tools.CustomNote(
    strNoteName="CustomNote_2", 
    dlNotePosition=[0.01, 0.01, 0.01], 
    iTargetEntityType=1, 
    crTarget=Node(7), c
    rParentCollection=CustomNoteCollection(1), 
    listContent=["My Custom Note 2"], 
    iFontSize=11, 
    bBold=True)

Tools.CustomNote.EditStyle(
    crlTargets=[CustomNoteCollection(1)], 
    bBold=True, 
    iBackgroundColor=13826810, 
    iOutlineColor=25600, 
    iArrowColor=8421376)
```
