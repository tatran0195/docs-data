---
id: MeshCleanup-Cleanup-TetEdge
title: MeshCleanup.Cleanup.TetEdge()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Command for cleaning tetrahedral mesh elements by edge length.
---

## Description

Command for cleaning tetrahedral mesh elements by edge length.

## Syntax

```psj
MeshCleanup.Cleanup.TetEdge(...)
```

Macro: [MC_TET_EDGE](../../macro/mesh-cleanup/MC_TET_EDGE)

## Inputs

### `crplElemEdges`
- A _List of Cursor Pair_ specifying the target element edges.
- This is a required input.

### `iCondition`
- An _Integer_ specifying the condition.
  - 0: &lt;=, Collapse the elements to cleanup.
  - 1: &gt;=, Split the elements to cleanup.
  - 2: &lt;, Collapse the elements to cleanup.
  - 3: &gt;, Split the elements to cleanup.
  
### `dLimitValue`
- A _Double_ specifying the cleanup threshold.
- Default value is 0.0.

### `iMode`
- An _Integer_ specifying the cleanup mode.
  - 0: Standard
  - 1: Aggressive
- Default value is 0.

### `iNonManifold`
- An _Integer_ specifying whether to include non-manifold elements.
  - 0: Exclude
  - 1: Include
- Default value is 0.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj {32-36}
Geometry.Part.Cube(
  ilAxialNodes=[3, 3, 3],
  iPartColor=7463537,
)

MeshCleanup.Manual2D.Split(
    crplElemEdge=[CursorPair(Node(7), Node(15))], 
    dRatio=0.99)

Meshing.SolidMeshing(
  crlParts=[Part(1)],
  dGradingFactor=1.05,
  iSpeedVsQual=1,
  iRegion=1,
  bSafeMode=False,
  iParallel=16,
  bInternalMeshOnly=True,
  iPartColor=65280,
)

result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=6,
  iCheckCondition=0,
  dLimitValue=0.0001,
)

print(result[7])
print(f"Number of error elements: {result[5]}")

# Cleanup
MeshCleanup.Cleanup.TetEdge(
  crplElemEdges=result[7],
  iCondition=0,
  dLimitValue=0.0001,
)

result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=6,
  iCheckCondition=0,
  dLimitValue=0.0001,
)
print(f"Number of error elements: {result[5]}")
```
