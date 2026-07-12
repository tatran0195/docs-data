---
id: Tools-Measure-Distance-Edge
title: Tools.Measure.Distance.Edge()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Measure the edge length
---

## Description

Measure the edge length.

## Syntax

```psj
Tools.Measure.Distance.Edge(...)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Distance &#187; Edge</menuselection>

## Inputs

### `crEdge`

- A _Cursor_ specifying the edge to measure the distance.
- This is a required input.

### `iPrecision`

- An _Integer_ specifying the number of digit after floating point. The greater `iPrecision` could be, the more accuracy of distance can be measured.
- The default value is 6.

## Return Code

A _Double_ specifying the length of the specified edge.

## Sample Code

```psj {3}
Geometry.Part.Cube()

length = Tools.Measure.Distance.Edge(crEdge=Edge(15))

JPT.Debugger(length)
```
