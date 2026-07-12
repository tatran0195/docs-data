---
id: BoundaryConditions-LBCCopy-ConnectionCopyMirror
title: BoundaryConditions.LBCCopy.ConnectionCopyMirror()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Copy boundary conditions by using mirror method
---

## Description

Copy boundary conditions by using mirror method.

## Syntax

```psj
BoundaryConditions.LBCCopy.ConnectionCopyMirror(...)
```

Ribbon: <menuselection>BoundaryConditions &#187; LBCCopy &#187; ConnectionCopyMirror</menuselection>

## Inputs

### `iMethod`

- An _Integer_ specifying the connection copy method:
  - 0: Translation method. The copy destination is searched by translation in the X, Y, and Z directions.
  - 1: Rotation method. The copy destination is searched by the rotational movement of the specified axis.
  - 2: Mirror method. Search the copy destination by plane and offset amount. To define a plane, select 3 nodes or 2D elements.
- The default value is 2.

### `iMatchMethod`

- An _Integer_ specifying the match method:
  - 0: Node method. This matching method matches the exact nodes of the target to get matching results. It is useful when the target features are different.
  - 1: Feature method. This matching method is very fast, especially for large models, and requires face-to-face, vertex to vertex like feature matching.
- The default value is 0.

### `poslPoints`

- A _Nested List_ specifying the list of points that create the center line of mirror.
- The default value is [].

### `dOffset`

- A _Double_ specifying the offset value for mirror in unit of length.
- The default value is 0.0.

### `dTol`

- A _Double_ specifying the tolerance value to be used for determination of conformity.
- The default value is 1.0.

### `crlTargets`

- A _List of Cursor_ specifying the list of targets.
- The default value is [].

## Return Code

A _Cursor_ specifying the created LBCs.

## Sample Code

```psj {28,29,30,31,32}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_3", 
                   iPartColor=13259210)

BoundaryConditions.FixedConstraint(crlTargets=[Face(76)])

MeshEdit.CreateNode.Between2Nodes(iNodeID=1465, 
                                  dX=1.5e-05, 
                                  dY=1e-05, 
                                  dZ=1e-05, 
                                  iNumberofNodes=1, 
                                  crlNodes=[Node(581, 580)])
MeshEdit.CreateNode.Between2Nodes(iNodeID=1466, 
                                  dX=1.5e-05, 
                                  dY=1e-05, 
                                  iNumberofNodes=1, 
                                  crlNodes=[Node(517, 516)])
MeshEdit.CreateNode.Between2Nodes(iNodeID=1467, 
                                  dX=1.5e-05, 
                                  dZ=1e-05, 
                                  iNumberofNodes=1, 
                                  crlNodes=[Node(565, 564)])

created_lbc = BoundaryConditions.LBCCopy.LBCCopyMirror(poslPoints=[[0.015, 0, 0.01], 
                                                                   [0.015, 0.01, 0.01], 
                                                                   [0.015, 0.01, 0]], 
                                                       dTol=0.1, 
                                                       crlTargets=[LbcConstraint(1)])

JPT.Debugger(created_lbc)
```
