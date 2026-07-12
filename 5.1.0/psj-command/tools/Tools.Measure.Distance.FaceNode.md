---
id: Tools-Measure-Distance-FaceNode
title: Tools.Measure.Distance.FaceNode()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Measure Distance By FaceNode
---

## Description

Measure Distance By FaceNode

## Syntax

```psj
Tools.Measure.Distance.FaceNode(crlFaces, crlNodes, iPrecision=6)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Distance &#187; FaceNode</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the face.
- This is a required input.

### `crlNodes`

- A _List of Cursor_ specifying the node.
- This is a required input.

### `iPrecision`

- An _Integer_ specifying the precision.
- The default value is 6.

## Return Code

A _Double_ specifying the distance between face - node.

## Sample Code

```psj {2}
Geometry.Part.Trapezoid()
dist=Tools.Measure.Distance.FaceNode(crlFaces=[Face(23)], crlNodes=[Node(306)],iPrecision=15)
print(dist)
```
