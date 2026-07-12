---
id: MainWindow-RightClick-AssociatedPick
title: MainWindow.RightClick.AssociatedPick()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: pick associated entity
---

## Description

Pick associated entity

## Syntax

```psj
MainWindow.RightClick.AssociatedPick(...)
```

Ribbon: <menuselection>MainWindow &#187; RightClick &#187; AssociatedPick</menuselection>

## Inputs

### `crlInput`

- A _List of Cursor_ specifying the input.
- This is a required input.

### `strTarget`

- A _String_ specifying the target.
- This is a required input.

### `strConnect`

- A _String_ specifying the connect.
- The default value is "UNKNOWN".

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{2}
Geometry.Part.Cube()
connectFace=MainWindow.RightClick.AssociatedPick(crlInput=[Node(1)], strTarget="Face")
JPT.Debugger(connectFace)
```
