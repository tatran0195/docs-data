---
id: Tools-Measure-Distance-Plane3NodesToNode
title: Tools.Measure.Distance.Plane3NodesToNode()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: measure the distance from node to plane(defined by 3 nodes)
---

## Description

Measure the distance from node to plane(defined by 3 nodes)

## Syntax

```psj
Tools.Measure.Distance.Plane3NodesToNode(crNode1, crNode2, crNode3, crNode, iPrecision=6)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Distance &#187; Plane3NodesToNode</menuselection>

## Inputs

### `crNode1`

- A _Cursor_ specifying the node1.
- This is a required input.

### `crNode2`

- A _Cursor_ specifying the node2.
- This is a required input.

### `crNode3`

- A _Cursor_ specifying the node3.
- This is a required input.

### `crNode`

- A _Cursor_ specifying the node.
- This is a required input.

### `iPrecision`

- An _Integer_ specifying the precision.
- The default value is 6.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Measure.Distance.Plane3NodesToNode(crNode1, crNode2, crNode3, crNode, iPrecision=6)
```
