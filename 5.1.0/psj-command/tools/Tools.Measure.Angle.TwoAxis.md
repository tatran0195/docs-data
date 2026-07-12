---
id: Tools-Measure-Angle-TwoAxis
title: Tools.Measure.Angle.TwoAxis()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Measure the angle created by 2 Axis.
---

## Description

Measure the angle created by 2 Axis.

## Syntax

```psj
Tools.Measure.Angle.TwoAxis(...)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Angle &#187; TwoAxis</menuselection>

## Inputs

### `dlXyz1`

- A _Double List_ specifying the xyz1.
- The default value is [0, 0, 0].

### `dlXyz2`

- A _Double List_ specifying the xyz2.
- The default value is [0, 0, 0].

### `strTarget`

- A _String_ specifying the target.
- The default value is "Angle".

### `iPrecision`

- An _Integer_ specifying the precision.
- The default value is 6.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {5}
Geometry.Part.Cube()
Tools.Coordinates.ThreeNode(crlNodes=[Node(7, 8, 5)])
Tools.Coordinates.ThreeNode(strName="CRect2", crlNodes=[Node(3, 7, 2)])

angle = Tools.Measure.Angle.TwoAxis(dlXyz1=[0.0, -1.0, 0.0], dlXyz2=[1.0, 0.0, 0.0])

JPT.Debugger(angle)
```
