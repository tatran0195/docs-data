---
id: Tools-Measure-Distance-TwoEdges
title: Tools.Measure.Distance.TwoEdges()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Measure the distance between two edges
---

## Description

Measure the distance of two edges.

## Syntax

```psj
Tools.Measure.Distance.TwoEdges(...)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Distance &#187; TwoEdges</menuselection>

## Inputs

### `crEdge1`

- A _Cursor_ specifying the first edge to measure distance.
- This is a required input.

### `crEdge2`

- A _Cursor_ specifying the second edge to measure distance.
- This is a required input.

### `iPrecision`

- An _Integer_ specifying the number of digit after floating point. The greater `iPrecision` could be, the more accuracy of distance can be measured.
- The default value is 6.

## Return Code

A _Double_ specifying the distance between two edges.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

distance = Tools.Measure.Distance.TwoEdges(crEdge1=Edge(20), 
                                           crEdge2=Edge(18))

JPT.Debugger(distance)
```
