---
id: Tools-Measure-Angle-TwoNodesAxis
title: Tools.Measure.Angle.TwoNodesAxis()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Measure the angle created by 2 nodes and Axis.
---

## Description

Measure the angle created by 2 nodes and Axis.

## Syntax

```psj
Tools.Measure.Angle.TwoNodesAxis(...)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Angle &#187; TwoNodesAxis</menuselection>

## Inputs

### `crNode1`

- A _Cursor_ specifying the node1.
- This is a required input.

### `crNode2`

- A _Cursor_ specifying the node2.
- This is a required input.

### `dlAxis`

- A _Double List_ specifying the axis.
- The default value is [1,0,0].

### `strTarget`

- A _String_ specifying the target.
- The default value is "Angle".

### `iPrecision`

- An _Integer_ specifying the precision.
- The default value is 6.

## Return Code

Value measured with the precision set in iPrecision in _String_ format.

## Sample Code

```psj {3-6}
Geometry.Part.Cube()

angle=Tools.Measure.Angle.TwoNodesAxis(
    crNode1=Node(462), 
    crNode2=Node(466), 
    dlAxis=[0.0, 1.0, 0.0])

JPT.Debugger(angle)
```
