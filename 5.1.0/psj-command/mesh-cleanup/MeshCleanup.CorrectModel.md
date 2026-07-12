---
id: MeshCleanup-CorrectModel
title: MeshCleanup.CorrectModel()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: correct model
---

## Description

Correct model

## Syntax

```psj
MeshCleanup.CorrectModel(crlParts, iEnableBreakEdge=0, dEdgeAngle=0, iEnableMergeEdge=0, dMergeEdgeAngle=0, iEnableMergePlanarFace=0, iEnableRemoveExtraVertex=0)
```

Ribbon: <menuselection>MeshCleanup &#187; CorrectModel</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the part.
- This is a required input.

### `iEnableBreakEdge`

- An _Integer_ specifying the enable break edge.
- The default value is 0.

### `dEdgeAngle`

- A _Double_ specifying the edge angle.
- The default value is 0.

### `iEnableMergeEdge`

- An _Integer_ specifying the enable merge edge.
- The default value is 0.

### `dMergeEdgeAngle`

- A _Double_ specifying the merge edge angle.
- The default value is 0.

### `iEnableMergePlanarFace`

- An _Integer_ specifying the enable merge planar face.
- The default value is 0.

### `iEnableRemoveExtraVertex`

- An _Integer_ specifying the enable remove extra vertex.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.CorrectModel(crlParts, iEnableBreakEdge=0, dEdgeAngle=0, iEnableMergeEdge=0, dMergeEdgeAngle=0, iEnableMergePlanarFace=0, iEnableRemoveExtraVertex=0)
```
