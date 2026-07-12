---
id: MeshCleanup-Cleanup-TetVolMesh
title: MeshCleanup.Cleanup.TetVolMesh()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Command for cleaning tetrahedral mesh by Metric:Volume.
---

## Description

Command for cleaning tetrahedral mesh by Metric:Volume.

## Syntax

```psj
MeshCleanup.Cleanup.TetVolMesh(...)
```

Ribbon: <menuselection>MeshCleanup &#187; Manual Check &#187; Tet</menuselection>

Macro: [CleaningVolumeMesh](../../macro/mesh-cleanup/CleaningVolumeMesh)

## Inputs

### `crlParts`
- A _List of Cursor_ specifying the target parts.
- This is a required input.

### `crlElems`
- A _List of Cursor_ specifying the target elements.
- This is a required input.

### `dLimitValue`
- A _Double_ specifying the cleaning threshold (e.g., minimum volume).
- Default value is 0.0.

### `iMode`
- An _Integer_ specifying the cleaning mode.
  - 0: Standard
  - 1: Aggressive
  - 2: Remove
- Default value is 0.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj{31-36}
Geometry.Part.Cube(
  ilAxialNodes=[3, 3, 3],
  iPartColor=7463537
)

MeshEdit.MoveNode.CADFollows(
  crlNodes=[Node(15)],
  dMovedPosX=10.0,
  dMovedPosY=10.0,
  dMovedPosZ=9.60758
)

Meshing.SolidMeshing(
  crlParts=[Part(1)],
  dGradingFactor=1.05,
  iSpeedVsQual=1,
  iRegion=1,
  bSafeMode=False,
  iParallel=16,
  bInternalMeshOnly=False,
  iPartColor=65280
)

MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=2,
  iCheckCondition=0,
  dLimitValue=2e-09
)

MeshCleanup.Cleanup.TetVolMesh(
  crlParts=[Part(1)],
  crlElems=[],
  dLimitValue=2e-09,
  iMode=1
)

MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=2,
  iCheckCondition=0,
  dLimitValue=2e-09
)
```
