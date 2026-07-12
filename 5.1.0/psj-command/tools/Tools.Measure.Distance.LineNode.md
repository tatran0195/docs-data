---
id: Tools-Measure-Distance-LineNode
title: Tools.Measure.Distance.LineNode()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Measures the distance of a perpendicular line from a node toward the line defined by the two nodes.
---

## Description

Measures the distance of a perpendicular line from a node toward the line defined by the two nodes.

## Syntax

```psj
Tools.Measure.Distance.LineNode(crlNodes, iPrecision=6)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Distance &#187; LineNode</menuselection>

## Inputs

### `crlNodes`

- A _List of Cursor_ specifying the target node.
- This is a required input.

### `iPrecision`

- An _Integer_ specifying the precision.
- The default value is 6.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Measure.Distance.LineNode(crlNodes, iPrecision=6)
```
