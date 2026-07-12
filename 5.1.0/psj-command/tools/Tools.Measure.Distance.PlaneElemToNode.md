---
id: Tools-Measure-Distance-PlaneElemToNode
title: Tools.Measure.Distance.PlaneElemToNode()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Measure Distance between Node and plane (created by element).
---

## Description

Measure Distance between Node and plane (created by element).

## Syntax

```psj
Tools.Measure.Distance.PlaneElemToNode(crNode=None, crElem=None, iPrecision=6)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Distance &#187; PlaneElemToNode</menuselection>

## Inputs

### `crNode`

- A _Cursor_ specifying the node.
- The default value is None.

### `crElem`

- A _Cursor_ specifying the element.
- The default value is None.

### `iPrecision`

- An _Integer_ specifying the precision.
- The default value is 6.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Measure.Distance.PlaneElemToNode(crNode=None, crElem=None, iPrecision=6)
```
