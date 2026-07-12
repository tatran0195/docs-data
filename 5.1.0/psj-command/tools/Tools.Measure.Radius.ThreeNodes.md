---
id: Tools-Measure-Radius-ThreeNodes
title: Tools.Measure.Radius.ThreeNodes()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Measure arc radius by using 3 nodes
---

## Description

Measure arc radius by using 3 nodes.

## Syntax

```psj
Tools.Measure.Radius.ThreeNodes(...)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Radius &#187; ThreeNodes</menuselection>

## Inputs

### `crNode13`

- A _Cursor_ specifying the first node on the arc whose radius is measured.
- This is a required input.

### `crNode23`

- A _Cursor_ specifying the second node on the arc whose radius is measured.
- This is a required input.

### `crNode33`

- A _Cursor_ specifying the third node on the arc whose radius is measured.
- This is a required input.

### `iPrecision`

- An _Integer_ specifying the number of digit after floating point. The greater `iPrecision` could be, the more accuracy of arc radius can be measured.
- The default value is 6.

## Return Code

A _Double_ specifying the arc radius value.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cylinder()

radius = Tools.Measure.Radius.ThreeNodes(crNode13=Node(18), 
                                         crNode23=Node(14), 
                                         crNode33=Node(8))

JPT.Debugger(radius)
```
