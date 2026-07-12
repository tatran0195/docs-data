---
id: MidPlane-AdjustThickness
title: MidPlane.AdjustThickness()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Adjust thickness of midplane
---

## Description

Adjust thickness of midplane

## Syntax

```psj
MidPlane.AdjustThickness(crlParts=[], dRatio=1.0, bAdjustFaceThick=False, bAdjustPropThick=False)
```

Ribbon: <menuselection>MidPlane &#187; AdjustThickness</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the part.
- The default value is [].

### `dRatio`

- A _Double_ specifying the ratio.
- The default value is 1.0.

### `bAdjustFaceThick`

- A _Boolean_ specifying the adjust face thickness.
- The default value is False.

### `bAdjustPropThick`

- A _Boolean_ specifying the adjust property thickness.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlane.AdjustThickness(crlParts=[], dRatio=1.0, bAdjustFaceThick=False, bAdjustPropThick=False)
```
