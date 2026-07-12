---
id: Tools-Measure-Angle-TwoElemEdges
title: Tools.Measure.Angle.TwoElemEdges()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

## Syntax

```psj
Tools.Measure.Angle.TwoElemEdges(...)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Angle &#187; TwoElemEdges</menuselection>

## Inputs

### `crpElemEdge1`

- A _Cursor Pair_ specifying the element edge1 - two nodes.
- This is a required input.

### `crpElemEdge2`

- A _Cursor Pair_ specifying the element edge2 - two nodes.
- This is a required input.

### `strTarget`

- A _String_ specifying the target.
- The default value is "Angle".

### `iPrecision`

- An _Integer_ specifying the precision.
- The default value is 6.

## Return Code

Value measured with the precision set in iPrecision in _String_ format.

## Sample Code

```psj {3-5}
Geometry.Part.Cube()

angle = Tools.Measure.Angle.TwoElemEdges(
            crpElemEdge1=CursorPair(Node(95), Node(487)), 
            crpElemEdge2=CursorPair(Node(453), Node(462)))

JPT.Debugger(angle)
```
