---
id: MeshCleanup-Manual2D-Swap
title: MeshCleanup.Manual2D.Swap()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Swap Element Edge
---

## Description

Swap Element Edge

## Syntax

```psj
MeshCleanup.Manual2D.Swap(...)
```

Ribbon: <menuselection>MeshCleanup &#187; Manual2D &#187; Swap</menuselection>

## Inputs

### `crplElemEdge`

- A _Cursor Pair List_ specifying the element edge.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{3}
# Prepare model
Geometry.Part.Cube(ilAxialNodes=[3, 3, 3], iPartColor=7463537)

MeshCleanup.Manual2D.Swap(crplElemEdge=[CursorPair(Node(17), Node(18))])
```
