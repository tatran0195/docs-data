---
id: Tools-Measure-Distance-TwoPoints
title: Tools.Measure.Distance.TwoPoints()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: measure distance 2 points
---

## Description

Measure distance 2 points

## Syntax

```psj
Tools.Measure.Distance.TwoPoints(posPoint1=[0,0,0], posPoint2=[0,0,0], strTarget="ALL", iPrecision=6, crCoordinateSystem=None)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Distance &#187; TwoPoints</menuselection>

## Inputs

### `posPoint1`

- A _Position_ specifying the point1.
- The default value is [0,0,0].

### `posPoint2`

- A _Position_ specifying the point2.
- The default value is [0,0,0].

### `strTarget`

- A _String_ specifying the target.
- The default value is "ALL".

### `iPrecision`

- An _Integer_ specifying the precision.
- The default value is 6.

### `crCoordinateSystem`

- A _Cursor_ specifying the coordinate system.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Measure.Distance.TwoPoints(posPoint1=[0,0,0], posPoint2=[0,0,0], strTarget="ALL", iPrecision=6, crCoordinateSystem=None)
```
