---
id: MeshCleanup-Cleanup-Auto
title: MeshCleanup.Cleanup.Auto()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Command for automatically cleaning triangle or quadrilateral mesh elements based on quality check results.
---

## Description

Command for automatically cleaning triangle or quadrilateral mesh elements based on quality check results.

## Syntax

```psj
MeshCleanup.Cleanup.Auto(...)
```

Macro: [CleanupAuto](../../macro/mesh-cleanup/CleanupAuto)

## Inputs

### `crlParts`
- A _List of Cursor_ specifying the target parts.
- This is a required input.

### `iElemType`
- An _Integer_ specifying the type of target elements.
  - 0: Triangle
  - 1: Quadrilateral
- This is a required input.

### `blCheckCondition`
- A _List of Boolean_ specifying the condition check enable flags for each cleanup condition.
- This is a required input.

### `blElemQuality`
- A _List of Boolean_ specifying the enable flags for each element quality metric.
- This is a required input.

### `dlLimitValue`
- A _List of Double_ specifying the threshold value for each quality metric.
- This is a required input.

### `crlElems`
- A _List of Cursor_ specifying the target elements.
- This is a required input.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj {38-45}
#Prepare Model
Geometry.Part.Cube(
    ilAxialNodes=[3, 3, 3], 
    iPartColor=7463537
)

MeshCleanup.Manual2D.Split(
    crplElemEdge=[CursorPair(Node(7), Node(15))], 
    dRatio=0.99
)

MeshCleanup.Manual2D.Split(
    crplElemEdge=[CursorPair(Node(16), Node(22))], 
    dRatio=0.99
)

# Check
result = MeshCleanup.AutoCheck.Tri(
    crlTargets=[Part(1)], 
    bStretchCheck=True, 
    bAspectRatioCheck=True, 
    bEdgeLengthCheck=True, 
    bAreaCheck=True, 
    bNodeValenceCheck=True, 
    bInteriorAngleCheck=True, 
    bDuplicateElemsCheck=True, 
    dStretchLimit=0.1, 
    dAspectRatioLimit=10, 
    dEdgeLengthLimit=0.0001, 
    dAreaLimit=1e-08, 
    dNodeValenceLimit=10, 
    dInteriorAngleLimit=0.174533
)

print(f"Number of error elements: {result[1]}")

# Auto cleanup
MeshCleanup.Cleanup.Auto(
    crlParts=[Part(1)], 
    iElemType=0, 
    blCheckCondition=[False, True, False, False, True, False, False], 
    blElemQuality=[False, True, True, True, True, True, True],
     dlLimitValue=[0.1, 10.0, 0.0001, 1e-08, 10.0, 10.0, 0.0], 
    crlElems=result[2]
)

result = MeshCleanup.AutoCheck.Tri(
    crlTargets=[Part(1)], 
    bStretchCheck=True, 
    bAspectRatioCheck=True, 
    bEdgeLengthCheck=True, 
    bAreaCheck=True, 
    bNodeValenceCheck=True, 
    bInteriorAngleCheck=True, 
    bDuplicateElemsCheck=True, 
    dStretchLimit=0.1, 
    dAspectRatioLimit=10, 
    dEdgeLengthLimit=0.0001, 
    dAreaLimit=1e-08, 
    dNodeValenceLimit=10, 
    dInteriorAngleLimit=0.174533
)

print(f"Number of error elements: {result[1]}")
```
