---
id: Tools-Measure-Radius-Edge
title: Tools.Measure.Radius.Edge()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Measure arc radius of the specified edge
---

## Description

Measure arc radius of the specified edge.

## Syntax

```psj
Tools.Measure.Radius.Edge(...)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Radius &#187; Edge</menuselection>

## Inputs

### `crEdge`

- A _Cursor_ specifying the edge to measure the arc radius. The selected edge should be a curved edge, not to be a straight edge.
- This is a required input.

### `iPrecision`

- An _Integer_ specifying the number of digit after floating point. The greater `iPrecision` could be, the more accuracy of arc radius can be measured.
- The default value is 6.

## Return Code

A _Double_ specifying the arc radius value.

## Sample Code

```psj {3}
Geometry.Part.Cylinder()

radius = Tools.Measure.Radius.Edge(crEdge=Edge(1))

JPT.Debugger(radius)
```
