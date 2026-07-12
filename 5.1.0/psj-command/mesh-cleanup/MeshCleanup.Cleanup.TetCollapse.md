---
id: MeshCleanup-Cleanup-TetCollapse
title: MeshCleanup.Cleanup.TetCollapse()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Command for cleaning tetrahedral mesh by Metric:Tet Collapse.
---

## Description

Command for cleaning tetrahedral mesh by Metric:Tet Collapse.

## Syntax

```psj
MeshCleanup.Cleanup.TetCollapse(...)
```

Macro: [CleanTetCollapse](../../macro/mesh-cleanup/CleanTetCollapse)

Ribbon: <menuselection>MeshCleanup &#187; Manual Check &#187; Tet</menuselection>

## Inputs

### `crlElems`
- A _List of Cursor_ specifying the target elements.
- This is a required input.

### `dLimitValue`
- A _Double_ specifying the cleaning threshold (e.g., minimum volume).
- Default value is 0.0.

### `iKeepSurfMesh`
- An _Integer_ specifying keeping method of surface mesh.
  - 0: Default, no keep.
  - 1: Keep Surface Mesh for all the mesh.
  - 2: Keep Surface Mesh at Freeze Mesh area.
- Default value is 0.

### `iCondition`
- An _Integer_ specifying the condition.
  - 0: &lt;=, Collapse the elements to cleanup.
  - 1: &gt;=, Split the elements to cleanup.
  - 2: &lt;, Collapse the elements to cleanup.
  - 3: &gt;, Split the elements to cleanup.

### `iMode`
- An _Integer_ specifying the cleaning mode.
  - 0: Method S
  - 1: Method A
  - 2: Method D

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj{36}
Geometry.Part.Cube(
  ilAxialNodes=[3, 3, 3],
  iPartColor=7463537
)

MeshEdit.CreateNode.Point(
  iNewNodeID=27,
  posPoint=[
    0.005026630125939846,
    0.009999999776482582,
    0.004957450088113546,
  ],
  crTarget=Face(22)
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
  iElemQualityType=4,
  iCheckCondition=0,
  dLimitValue=0.02
)
print(f"Number of error elements: {result[5]}")

# Cleanup
MeshCleanup.Cleanup.TetCollapse(crlElems=result[6], dLimitValue=0.05)

result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=4,
  iCheckCondition=0,
  dLimitValue=0.02
)
print(f"Number of error elements: {result[5]}")
```
