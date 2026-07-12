---
id: Geometry-MakeFacePlanar
title: Geometry.MakeFacePlanar()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Flatten curved faces into the planar face
---

## Description

This method flattens the curved faces or bumpy faces into planar faces defined by a set of three-nodes.

## Syntax

```psj
Geometry.MakeFacePlanar(dlPlanePt1=[0.0,0.0,0.0], dlPlanePt2=[0.0,0.0,0.0],
    dlPlanePt3=[0.0,0.0,0.0], ilFaceIds=[], iMergeFace=0)
```

Macro: [MakeFacePlanar](../../macro/geometry/MakeFacePlanar)

Ribbon: <menuselection>Geometry &#187; Make Face Planar</menuselection>

## Inputs

### `dlPlanePt1`

- A _List of Double_ specifying the plane point 1.
- The default value is [0.0,0.0,0.0].

### `dlPlanePt2`

- A _List of Double_ specifying the plane point 2.
- The default value is [0.0,0.0,0.0].

### `dlPlanePt3`

- A _List of Double_ specifying the plane point 3.
- The default value is [0.0,0.0,0.0].

### `ilFaceIds`

- A _List of Integer_ specifying the target face ids.
- The default value is [].

### `iMergeFace`

- An _Integer_ specifying whether to merge adjacent faces to each other after the operation. Possible values are 0 and 1.
- If _iMergeFace=0_, do not merge faces after the operation.
- If _iMergeFace=1_, merge faces after the operation.
- The default value is 0.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()

Geometry.Part.Trapezoid(dlOrigin=[0.0005, 0.0005, 0.01], dlLength=[0.005, 0.005, 0.005],
    dTopXLength=3.0, strName="Trapezoid_5", iPartColor=7697908)

Geometry.MakeFacePlanar(dlPlanePt1=[0.01, 0.0, 0.01], dlPlanePt2=[0.01, 0.01, 0.01],
    dlPlanePt3=[0.0, 0.01, 0.01], ilFaceIds=[52, 50, 48, 49, 47])
```
