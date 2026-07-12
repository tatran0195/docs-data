---
id: Geometry-Transform-MatingFace
title: Geometry.Transform.MatingFace()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Transform Mating Face
---

## Description

Translate parts by defining mating faces, mating edges, and mating points.

## Syntax

```psj
Geometry.Transform.MatingFace(...)
```

Ribbon: <menuselection>Geometry &#187; Transform &#187; Mating Face</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying parts to transform.
- This is a required input.

### `crSrcFace`

- A _Cursor_ specifying the face to be used as the source for the transform operation.
- This is a required input.

### `crDstFace`

- A _Cursor_ specifying the face to be used as the reference for the transform operation.
- This is a required input.

### `crSrcEdge`

- A _Cursor_ specifying the edge to be used as the source for the transform operation.
- The default value is _None_.

### `crDstEdge`

- A _Cursor_ specifying the edge to be used as the reference for the transform operation. This argument must be specified when _iAlignMethodType=0_.
- The default value is _None_.

### `crSrcNode`

- A _Cursor_ specifying the node to be used as the source for the transform operation.
- The default value is _None_.

### `crDstNode`

- A _Cursor_ specifying the node to be used as the reference for the transform operation. This argument must be specified when _iAdjustPointType=0_.
- The default value is _None_.

### `iFaceOpposite`

- An _Integer_ specifying whether or not the source surface should be on the opposite side of the destination surface.
  - If _iFaceOpposite=0_: The source surface lay on the current side of the destination surface.
  - If _iFaceOpposite=1_: The source surface lay on the opposite side of the destination surface.
- The default value is 0.

### `dEdgeAngle`

- A _Double_ specifying the angle in degrees between two specified edges, _crSrcEdge_ and _crDstEdge_, after the transform operation.
- The default value is 0.0.

### `iEdgeOpposite`

- An _Integer_ specifying whether to match the opposite direction of source edge to destination edge.
  - If _iEdgeOpposite=0_: Match the current direction of source edge to destination edge.
  - If _iEdgeOpposite=1_: Match the opposite direction of source edge to destination edge.
- The default value is 0.

### `iAlignMethodType`

- An _Integer_ specifying how to align the edges between the source and the destination. This argument will be ignored if _crSrcEdge_ has a default value.
  - If _iAlignMethodType=0_: Move the given source part so that _crSrcEdge_ is coincident with _crDstEdge_.
  - If _iAlignMethodType=1_: Move _crSrcEdge_ edges along the direction of the specified vector _dlAlignVector_.
- The default value is 0.

### `iAdjustPointType`

- An _Integer_ specifying how to move the node along the direction. This argument will be ignored if _crSrcNode_ has a default value.
  - If _iAdjustPointType=0_: Move on a direction defined by two nodes, from source and destination.
  - If _iAdjustPointType=1_: Move on a direction defined by a node and a coordinate, from source and destination.
- The default value is 0.

### `iAdjustProjectionType`

- An _Integer_ specifying the projection direction. This argument will be ignored if _crSrcNode_ has a default value.
  - If _iAdjustProjectionType=0_: Projection direction is the normal direction of the surface.
  - If _iAdjustProjectionType=1_: Projection direction is the specified vector _dlAdjustVector_.
- The default value is 0.

### `dlAlignVector`

- A _List of Double_ specifying the alignment vector. This argument is used when _iAlignMethodType=1_.
- The default value is [0.0, 0.0, 0.0].

### `dlAdjustPoint`

- A _List of Double_ specifying the destination point which _crSrcNode_ will move to. This argument is used when _iAdjustPointType=1_.
- The default value is [0.0, 0.0, 0.0].

### `dlAdjustVector`

- A _List of Double_ specifying adjustment vector. This argument is used when _iAdjustPointType=1_.
- The default value is [0.0, 0.0, 0.0].

### `bCreateNewPart`

- A _Boolean_ specifying whether to keep the original part and make a copy one then transform.
- The default value is _False_.

### `bCopyLBC`

- A _Boolean_ specifying whether to copy load boundary condition of original part to transformed part. This argument is used when _bCreateNewPart=True_.
- The default value is _False_.

### `bCopyProperty`

- A _Boolean_ specifying whether to copy property of original part to transformed part. This argument is used when _bCreateNewPart=True_.
- The default value is _False_.

### `bIsPreview`

- A _Boolean_ specifying whether to enable preview or not.
- The default value is _False_.

### `crlCoordSyss`

- A _List of Cursor_ specifying the coordinate systems.
- The default value is [].

### `bCopyReference`

- A _Boolean_ specifying whether to copy references from the existing part to the created parts or not.
- The default value is _False_.

## Return Code

No return value.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Geometry.Part.Cylinder(dlOrigin=[0.02, 0.005, 0.005], dTopOuterRadius=0.005, dBottomOuterRadius=0.005)
Geometry.Transform.MatingFace(crlParts=[Part(2)], crSrcFace=Face(30), crDstFace=Face(22))
```
