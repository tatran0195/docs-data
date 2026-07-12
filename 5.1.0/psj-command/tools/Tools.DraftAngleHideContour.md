---
id: Tools-DraftAngleHideContour
title: Tools.DraftAngleHideContour()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Hide result contour of Draft Angle function.
---

## Description

Hide result contour of Draft Angle function.

## Syntax

```psj
Tools.DraftAngleHideContour(...)
```

Macro: HideContourDraftAngle()

Ribbon: <menuselection>Tools &#187; DraftAngleHideContour</menuselection>

## Inputs

This function does not have input argument.

## Return Code

- A _Boolean_ specifying whether the function succeeded or not.
  - 0: Failed
  - 1: Succeeded
  
## Sample Code

```psj {34}
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

# Show result by contour
Tools.DraftAngleShowContour(listPairCursorData=draft_angle_result)

# Hide result contour
Tools.DraftAngleHideContour() 
```
