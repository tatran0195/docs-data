---
id: MufflerT-SpecialModeling-Rod-Rod
title: MufflerT.SpecialModeling.Rod.Rod()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: create rod
---

## Description

Create rod

## Syntax

```psj
MufflerT.SpecialModeling.Rod.Rod(...)
```

Ribbon: <menuselection>MufflerT &#187; SpecialModeling &#187; Rod &#187; Rod</menuselection>

## Inputs

### `crlNodes`

- A _List of Cursor_ specifying the node.
- This is a required input.

### `dRadius`

- A _Double_ specifying the radius.
- This is a required input.

### `iType`

- An _Integer_ specifying the type.
- This is a required input.

### `dMeshSize`

- A _Double_ specifying the mesh size.
- This is a required input.

### `dStartDist`

- A _Double_ specifying the start dist.
- This is a required input.

### `dWeldDist`

- A _Double_ specifying the weld dist.
- This is a required input.

### `iDivNumber`

- An _Integer_ specifying the divide number.
- This is a required input.

### `dDeformWidth`

- A _Double_ specifying the deformation width.
- This is a required input.

### `iTransitionElem`

- An _Integer_ specifying the transition element.
- This is a required input.

### `dlPosDir`

- A _Double List_ specifying the position direction.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MufflerT.SpecialModeling.Rod.Rod(crlNodes, dRadius, iType, dMeshSize, dStartDist, dWeldDist, iDivNumber, dDeformWidth, iTransitionElem, dlPosDir)
```
