---
id: MeshCleanup-Cleanup-TetTriangleHeight
title: MeshCleanup.Cleanup.TetTriangleHeight()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Command for cleaning tetrahedral mesh by Metric:Triangle Height.
---

## Description

Command for cleaning tetrahedral mesh by Metric:Triangle Height.

## Syntax

```psj
MeshCleanup.Cleanup.TetTriangleHeight(...)
```

Ribbon: <menuselection>MeshCleanup &#187; Manual Check &#187; Tet</menuselection>

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

### `iCondition`
- An _Integer_ specifying the condition.
  - 0: &lt;=, Collapse the elements to cleanup.
  - 1: &gt;=, Split the elements to cleanup.
  - 2: &lt;, Collapse the elements to cleanup.
  - 3: &gt;, Split the elements to cleanup.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj{34-39}
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

result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=9,
  iCheckCondition=0,
  dLimitValue=0.0003
)

print(f"Number of the error elements: {result[5]}")

# Cleanup
MeshCleanup.Cleanup.TetTriangleHeight(
  crlParts=[Part(1)],
  crlElems=[],
  dLimitValue=0.0003,
  iCondition=0
)

result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=9,
  iCheckCondition=0,
  dLimitValue=0.0003
)

print(f"Number of the error elements: {result[5]}")
```
