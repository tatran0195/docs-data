---
id: MainWindow-RightClick-FlipElement
title: MainWindow.RightClick.FlipElement()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Flip normal of surface.
---

## Description

Flip normal of surface (face or element). 

## Syntax

```psj
MainWindow.RightClick.FlipElement(...)
```

Ribbon: <menuselection>MainWindow &#187; RightClick &#187; FlipElement</menuselection>

## Inputs

### `crlTargets`

- A _List of Cursor_ specifying the target.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {2-3}
Geometry.Part.Cube()
MainWindow.RightClick.FlipElement(crlTargets=[Face(21, 23, 26)])
MainWindow.RightClick.FlipElement(crlTargets=[Elem(1009, 1025, 968)])
```
