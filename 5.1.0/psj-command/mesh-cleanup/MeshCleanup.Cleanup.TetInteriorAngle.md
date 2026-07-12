---
id: MeshCleanup-Cleanup-TetInteriorAngle
title: MeshCleanup.Cleanup.TetInteriorAngle()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Command for cleaning tetrahedral mesh by Metric:Interior Angle.
---

## Description

Command for cleaning tetrahedral mesh by Metric:Interior Angle.

## Syntax

```psj
MeshCleanup.Cleanup.TetInteriorAngle(...)
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

```psj{24-28}
Geometry.Part.Cube()

Meshing.SolidMeshing(
  crlParts=[Part(1)],
  bTet10=True, 
  dGradingFactor=1.05,
  iSpeedVsQual=1,
  bSafeMode=False,
  iParallel=16,
  bInternalMeshOnly=False,
  iPartColor=65280
)

# 110 elements found
result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=10,
  iCheckCondition=0,
  dLimitValue=30
)
print(f"Number of error elements is {result[5]}")

# Cleanup
MeshCleanup.Cleanup.TetInteriorAngle(
  crlParts=[Part(1)],
  crlElems=[],
  dLimitValue=30
)

# Half of them are cleanupped
result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=10,
  iCheckCondition=0,
  dLimitValue=30
)
print(f"Number of error elements is {result[5]}")
```
