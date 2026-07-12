---
id: MeshCleanup-Manual3D-Split
title: MeshCleanup.Manual3D.Split()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Merge two Quad elements into one Quad element
---

## Description

Merge two Quad elements into one Quad element

## Syntax

```psj
MeshCleanup.Manual3D.Split(crplElemEdge, crlNodes=[], dRatioDistance=0.5)
```

Ribbon: <menuselection>MeshCleanup &#187; Manual3D &#187; Split</menuselection>

## Inputs

### `crplElemEdge`

- A _Cursor Pair List_ specifying the element edge.
- This is a required input.

### `crlNodes`

- A _List of Cursor_ specifying the node.
- The default value is [].

### `dRatioDistance`

- A _Double_ specifying the ratio distance.
- The default value is 0.5.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual3D.Split(crplElemEdge, crlNodes=[], dRatioDistance=0.5)
```
