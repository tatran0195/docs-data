---
id: Tools-Measure-Distance-EdgeNode
title: Tools.Measure.Distance.EdgeNode()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Measure Distance From Node to Edge
---

## Description

Measure Distance From Node to Edge

## Syntax

```psj
Tools.Measure.Distance.EdgeNode(crEdge, crNode, iPrecision=6)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Distance &#187; EdgeNode</menuselection>

## Inputs

### `crEdge`

- A _Cursor_ specifying the edge.
- This is a required input.

### `crNode`

- A _Cursor_ specifying the node.
- This is a required input.

### `iPrecision`

- An _Integer_ specifying the precision.
- The default value is 6.

## Return Code

A _Double_ specifying the distance between edge - node.

## Sample Code

```psj {2}
Geometry.Part.Trapezoid()
dist=Tools.Measure.Distance.EdgeNode(crEdge=Edge(20), crNode=Node(85), iPrecision=15)
print(dist)
```
