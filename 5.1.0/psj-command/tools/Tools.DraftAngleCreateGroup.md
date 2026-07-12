---
id: Tools-DraftAngleCreateGroup
title: Tools.DraftAngleCreateGroup()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create the nodal groups for each draft angle 
---

## Description

Create the nodal groups for each draft angle.

## Syntax

```psj 
Tools.DraftAngleCreateGroup(...)
```

Macro: CreateGroupDraftAngle

Ribbon: <menuselection>Tools &#187; DraftAngleCreateGroup</menuselection>

## Inputs

### `listPairCursorData`

- A _List of Cursor-Value_ specifying a list of pair data (list type), which data includes cursor and value.
- This is a required input.

### `iNumDigits`

- An _Integer_ specifying the number of digits of contour.
- The default value is 1.

### `dGroupMax`

- A _Double_ specifying the number of the maximum value of the group.
- The default value is 90.

### `dGroupMin`

- A _Double_ specifying the number of the minimum value of the group.
- The default value is -90.

## Return Code

A _List of Cursor_ specifying the newly created groups.

## Sample Code

```psj {31,34-36}
# Create Sample Model
Geometry.Part.Trapezoid(
    dlLength=[0.01, 0.001, 0.01], 
    ilAxialNodes=[10, 2, 10], 
    iPartColor=7961077)

JPT.ViewFitToModel()

MeshEdit.OneNode(
    crlNodes=[Node(45)],
    crlFaceFixed=[Face(21)], 
    bOffsetvector=True, dlOffset=[0.8, 0.0, 0.0], dOffset=0.0, 
    dDistStrong=2.0, dDistWeak=5.0)

MeshEdit.OneNode(
    crlNodes=[Node(56)],
    crlFaceFixed=[Face(21)], 
    bOffsetvector=True, dlOffset=[-0.8, 0.0, 0.0], dOffset=0.0,
    dDistStrong=2.0, dDistWeak=5.0)

MeshEdit.OneNode(
    crlNodes=[Node(4)], 
    crlFaceFixed=[Face(21)], 
    bOffsetvector=True, dlOffset=[0.8, 0.0, 0.0], dOffset=0.0, 
    dDistStrong=2.0, dDistWeak=5.0)

# Calculate Draft Angle
draft_angle_result=Tools.DraftAngle(dlDraftDirection=[0, 1, 0], crlTargets=[Part(1)])

# Save result in group 
Tools.DraftAngleCreateGroup(listPairCursorData=draft_angle_result)

# Overwrite result in group with different parameter 
Tools.DraftAngleCreateGroup(
    listPairCursorData=draft_angle_result, 
    iNumDigits=5, dGroupMax=60, dGroupMin=-60)
```
