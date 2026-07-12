---
id: Tools-CustomNote-Create
title: Tools.CustomNote.Create()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a custom note
---

## Description

Create a custom note.

## Syntax

```psj
Tools.CustomNote.Create(...)
```

Macro: 

Ribbon: <menuselection>Tools &#187; CustomNote &#187; Create</menuselection>

## Inputs

### `strNoteName`

- A _String_ specifying note name.
- The default value is "CustomNote_1".

### `dlNotePosition`

- A _List of Double_ specifying position where the created note indicates.
- The default value is [0.0,0.0,0.0].

### `iTargetEntityType`

- An _Integer_ specifying target entity type.
  - 0: None
  - 1: Node
  - 2 :1D Element
  - 3: 2D Element
  - 4 :3D Element
  - 5: Face Point
  - 6: Edge Point
- The default value is 0.

### `crTarget`

- A _Cursor_ specifying target entity.
- The default value is _None_.

### `crParentCollection`

- A _Cursor_ specifying custom note collection to store the custom note.
- The default value is _None_.

### `strParentName`

- A _String_ specifying name of newly created custom note collection.
- The default value is "".

### `listContent`

- A _List of String_ specifying content of custom note.
- This is a required input.

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

### `strImagePath`
- A _String_ specifying image path.
- The default value is "".

### `crEdit`
- A _Cursor_ specifying a custom note to modify.
- The default value is 0:0.
  
## Return Code

A _Cursor_ specifying created custom note.

## Sample Code

```psj{5-16}
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

Tools.CustomNote.Create(
    strNoteName="CustomNote_1", 
    dlNotePosition=[0.0029, 0.0063, 0.01], 
    iTargetEntityType=5, 
    crTarget=Elem(1022), 
    strParentName="Collection_1", 
    listContent=["Top Face"], 
    iFontSize=18, 
    bBold=True, 
    iBackgroundColor=13826810, 
    iOutlineColor=2763429, 
    iArrowColor=2763429)
```
