---
id: Geometry-BodyCut-XXYYOnOnePoint
title: Geometry.BodyCut.XXYYOnOnePoint()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Separate a part along the specified coordinate plane with one node as a starting point
---

## Description

Separate a part along the specified coordinate plane with one node as a starting point.

## Syntax

```psj
Geometry.BodyCut.XXYYOnOnePoint(...)
```

Macro: [CutBodyByPlane](../../macro/geometry/CutBodyByPlane)

Ribbon: <menuselection>Geometry &#187; Body Cut &#187; XX-YY On 1 Point</menuselection>

## Inputs

### `crPart`

- A _Cursor_ specifying the part to partition.
- This is a required input.

### `posCutPoint`

- A _Position_ specifying a point on the cutting plane. This position can get from node, point on edge or point on face.
- The default value is [0.0,0.0,0.0].

### `iCuttingPlane`

- An _Integer_ specifying the cutting plane.
  - If _iType = 0_, cutting by plane Oxy.
  - If _iType = 1_, cutting by plane Oxz.
  - If _iType = 2_, cutting by plane Oyz.
- The default value is 0.

### `dOffsetDistance`

- A _Double_ specifying the offset distance from the selected position.
- The default value is 0.0.

### `bSplitOnly`

- A _Boolean_ specifying whether or not retain the original part.
  - If _False_, the specified part will be divided into two parts separately.
  - If _True_, the specified part just split by cutting plane without dividing into two parts.
- The default value is _False_.

### `bMakeSectionFace`

- A _Boolean_ specifying whether to generate a cross-section face at the division section.
- The default value is _True_.

### `bSharedFace`

- A _Boolean_ specifying whether to generate a shared face at the division section. This argument will only affect the functionality when _bMakeSectionFace=True_ and _bSplitOnly=False_.
- The default value is _False_.

### `crLocalCoordinate`

- A _Cursor_ specifying the local coordinate. When the default value is used, the global coordinate is selected.
- The default value is _None_.

### `bSeparateFace`

- A _Boolean_ specifying whether to prevent the section faces to be coupled (merge) in the enclave. This option will only affect the functionality if _bMakeSectionFace=True_.
  - If _True_, the section faces will be created separately.
  - If _False_, only a section face will be created.
- The default value is _False_

## Return Code

A _List of Cursor_ specifying the new bodies.

## Sample Code

```psj {3,4,5,6,7,8,9}
Torus = Geometry.Part.Torus(strName="Torus_2", iPartColor=14114775)

separate_status = Geometry.BodyCut.XXYYOnOnePoint(crPart=Torus, 
                                                  posCutPoint=[-0.015,
                                                               -0.005, 
                                                               0.006],
                                                  iCuttingPlane=1, 
                                                  bSharedFace=True, 
                                                  bSeparateFace=True)

JPT.Debugger(separate_status)
```
