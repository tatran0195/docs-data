---
id: MeshCleanup-Cleanup-Tet
title: MeshCleanup.Cleanup.Tet()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Command for cleaning tetrahedral mesh elements based on quality check results.
---

## Description

Command for cleaning tetrahedral mesh elements based on quality check results.

## Syntax

```psj
MeshCleanup.Cleanup.Tet(...)
```

Macro: [MC_Mesh_Quality_Manual_Check_Tet](../../macro/mesh-cleanup/MC_Mesh_Quality_Manual_Check_Tet)

Ribbon: <menuselection>MeshCleanup &#187; ManualCheck &#187; Tet</menuselection>

## Inputs

### `crlTargets`
- A _List of Cursor_ specifying the target entities. The targets can be a mix of Body, Face, or Element.
- This is a required input.

### `iElemType`
- An _Integer_ specifying the element type.
- Default value is 0.

### `iElemQualityType`
- An _Integer_ specifying the quality metric.
  - 0: Stretch
  - 3: Jacob. Factor
  - 7: Unstable
  - 8: Time Step (Abaqus)
- Default value is 0.

### `dMinValue`
- A _Double_ specifying the minimum quality value (statistics).
- Default value is 0.0.

### `dMaxValue`
- A _Double_ specifying the maximum quality value (statistics).
- Default value is 0.0.

### `dAverageValue`
- A _Double_ specifying the average quality value (statistics).
- Default value is 0.0.

### `iTotalEntities`
- An _Integer_ specifying the total number of target entities (statistics).
- Default value is 0.

### `iCheckCondition`
- An _Integer_ specifying the check condition.
- Default value is 0.

### `dLimitValue`
- A _Double_ specifying the cleanup threshold.
- Default value is 0.0.

### `dSafetyFactor`
- A _Double_ specifying the safety factor.
- Default value is 1.0.

### `iFailedElements`
- An _Integer_ specifying the number of failed elements (statistics).
- Default value is 0.

### `iMode`
- An _Integer_ specifying the cleanup mode.
  - 0: Standard
  - 1: Aggressive
- Default value is 0.

### `bNonmanifold`
- A _Boolean_ specifying whether to include elements with non-manifold edges.
- Default value is False.

### `bInternalMeshOnly`
- A _Boolean_ specifying whether to target internal mesh only.
- Default value is False.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj{35-41}
# Prepare model
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

# Check
ret = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=0,
  iCheckCondition=0,
  dLimitValue=0.1
)
print(f"number of error elements: {ret[5]}")

# Cleanup
MeshCleanup.Cleanup.Tet(
    crlTargets=[Part(1)], 
    dMinValue=ret[1], 
    dMaxValue=ret[2], 
    dAverageValue=ret[3], 
    iTotalEntities=ret[4], 
    iCheckCondition=0, 
    dLimitValue=0.1, 
    iFailedElements=ret[5],
    iCleanupCheck=1,
    iMode=1
)

ret = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=0,
  iCheckCondition=0,
  dLimitValue=0.1
)
print(f"number of error elements: {ret[5]}")
```
