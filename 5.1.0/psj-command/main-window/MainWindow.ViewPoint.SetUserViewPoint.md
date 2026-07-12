---
id: MainWindow-ViewPoint-SetUserViewPoint
title: MainWindow.ViewPoint.SetUserViewPoint()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set the user ViewPoint
---

## Description

Set the user ViewPoint

## Syntax

```psj
MainWindow.ViewPoint.SetUserViewPoint(...)
```

Macro: 

Ribbon: <menuselection>MainWindow &#187; ViewPoint &#187; SetUserViewPoint</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of ViewPoint.
- This is a required input.

### `bRotate`

- A _Boolean_ specifying whether to rotate the view. 
- The default value is _True_.

### `bPan`

- A _Boolean_ specifying whether to pan the view.
- The default value is _True_.

### `bScale`

- A _Boolean_ specifying whether to scale the view. 
- The default value is _True_.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {6}}
JPT.Exec('ViewReset()')
JPT.Exec('ViewControl_Rotate([0, -60, 0])')
JPT.Exec('ViewControl_SetCenter([0.005, 0.005, 0.005])')
JPT.Exec('AddUserViewPoint("New View Point")')
JPT.Exec('ViewReset()')
MainWindow.ViewPoint.SetUserViewPoint(strName="New View Point")
```
