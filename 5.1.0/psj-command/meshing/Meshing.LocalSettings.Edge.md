---
id: Meshing-LocalSettings-Edge
title: Meshing.LocalSettings.Edge()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set the mesh setting for the selected edges (Define the settings before surface mesh creation)
---

## Description

Set the mesh setting for the selected edges (Define the settings before surface mesh creation).

## Syntax

```psj
Meshing.LocalSettings.Edge(...)
```

Ribbon: <menuselection>Meshing &#187; LocalSettings &#187; Edge</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of the local mesh setting.
- This is a required input.

### `localMesh`

- A _[LOCAL_MESH](./../../data-type/psj-command/parameter-types/LOCAL_MESH)_ specifying the local mesh setting's parameter.
- This is a required input.

### `crlTargets`

- A _List of Cursor_ specifying the target Edges of the local mesh setting.
- This is a required input.

### `crEditTarget`

- A _Cursor_ specifying an existed local mesh setting Edge. When this parameter is used, the specified local mesh setting Edge will be overwritten. When it is not used, a new local mesh setting Edge will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created local mesh setting if success, or None if fail.

## Sample Code

```psj {3,4,5,6,7,8,9,10,11}
Geometry.Part.Cube()

local_mesh = Meshing.LocalSettings.Edge(strName="MeshParam_1", 
                                        localMesh=LOCAL_MESH(iEntityType=3, 
                                                             dAvgElemSize=0.005, 
                                                             dMaxElemSize=0.01, 
                                                             dMinElemSize=0.001, 
                                                             dTrimAngle=0.7853981634, 
                                                             bEnableMeshCount=True, 
                                                             iNodeCount=8), 
                                        crlTargets=[Edge(18)])

JPT.Debugger(local_mesh)

Geometry.FCircVertexAdjust(crlParts=[Part(1)])

Meshing.SetMeshAttribute(crlParts=[Part(1)], 
                         surfaceMesh=SURFACE_MESH(dMaxElemSize=0.015, 
                                                  dMinElemSize=0.0005,
                                                  dGeomAngle=0.7853981634, 
                                                  dGeomMinSize=0.0005, 
                                                  dMinStretchVal=0.0, 
                                                  iPerformanceMode=1, 
                                                  dAutoMergeTinyFacesAngle=0.5235987756,
                                                  bGeomApprox=True, 
                                                  iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                       surfaceMesh=SURFACE_MESH(dMaxElemSize=0.015, 
                                                dMinElemSize=0.0005,
                                                dGeomAngle=0.7853981634, 
                                                dGeomMinSize=0.0005, 
                                                dMinStretchVal=0.0, 
                                                iPerformanceMode=1, 
                                                dAutoMergeTinyFacesAngle=0.5235987756,
                                                bGeomApprox=True, 
                                                iNextEntityOffsetId=0), 
                       iThreadNum=4)
```
