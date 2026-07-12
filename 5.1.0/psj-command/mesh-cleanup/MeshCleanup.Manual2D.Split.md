---
id: MeshCleanup-Manual2D-Split
title: MeshCleanup.Manual2D.Split()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: manual cleanup by split
---

## Description

Manual cleanup by split

## Syntax

```psj
MeshCleanup.Manual2D.Split(crplElemEdge, dRatio=0.0, crNodeRef=None, crProjectPart=None)
```

Ribbon: <menuselection>MeshCleanup &#187; Manual2D &#187; Split</menuselection>

## Inputs

### `crplElemEdge`

- A _Cursor Pair List_ specifying the element edge.
- This is a required input.

### `dRatio`

- A _Double_ specifying the ratio.
- The default value is 0.0.

### `crNodeRef`

- A _Cursor_ specifying the node reference.
- The default value is None.

### `crProjectPart`

- A _Cursor_ specifying the project part.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.Split(crplElemEdge, dRatio=0.0, crNodeRef=None, crProjectPart=None)
```
