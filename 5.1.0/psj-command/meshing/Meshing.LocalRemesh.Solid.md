---
id: Meshing-LocalRemesh-Solid
title: Meshing.LocalRemesh.Solid()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Mesh the selected solid elements locally without affecting the other positions
---

## Description

Mesh the selected solid elements locally without affecting the other positions.

## Syntax

```psj
Meshing.LocalRemesh.Solid(...)
```

Ribbon: <menuselection>Meshing &#187; LocalRemesh &#187; Solid</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the parts list to perform remesh.
- This is a required input.

### `dlCenter`

- A _List of Double_ specifying the center of the sphere. This sphere is the region to remesh.
- The default value is [0.0,0.0,0.0].

### `dRadius`

- A _Double_ specifying the radius of the remesh sphere in millimeter.
- The default value is 5.0.

### `dGradFactor`

- A _Double_ specifying the grading factor of the result mesh.
- The default value is 1.0.

### `dStretchLimit`

- A _Double_ specifying the stretch limit of the elements in the result mesh.
- The default value is 0.1.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {20,21,22,23,24}
cube = Geometry.Part.Cube(iPartColor=12603072)
MeshEdit.MoveNode.CADFollows(crlNodes=[Node(453)], 
                             dMovedPosX=5.527019999999999, 
                             dMovedPosY=5.43058, 
                             dMovedPosZ=10.0)

Meshing.SolidMeshing(crlParts=[cube], 
                     bTet10=True, 
                     dGradingFactor=1.05, 
                     dStretchLimit=0.1, 
                     iSpeedVsQual=1, 
                     iRegion=1, 
                     bSafeMode=False, 
                     iParallel=4, 
                     bSurfaceNodes=False, 
                     bEdgeNodes=False, 
                     bPreservation=False, 
                     iPartColor=65280)

remesh_status = Meshing.LocalRemesh.Solid(crlParts=[cube], 
                                          dlCenter=[0.005555555555555556, 
                                                    0.005555555555555556, 
                                                    0.01], 
                                          dRadius=2.0)

JPT.Debugger(remesh_status)
```
