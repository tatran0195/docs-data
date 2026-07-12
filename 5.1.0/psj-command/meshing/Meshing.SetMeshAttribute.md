---
id: Meshing-SetMeshAttribute
title: Meshing.SetMeshAttribute()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set mesh attribute for the selected part
---

## Description

Set mesh attribute for the selected part.

:::note

This function will be used with _[Meshing.SurfaceMeshing](Meshing.SurfaceMeshing)_ function.

:::

## Syntax

```psj
Meshing.SetMeshAttribute(...)
```

Ribbon: <menuselection>Meshing &#187; SetMeshAttribute</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the Parts to be set up with mesh setting.
- This is a required input.

### `surfaceMesh`

- A _[SURFACE_MESH](./../../data-type/psj-command/parameter-types/SURFACE_MESH)_ specifying the surface mesh parameter. This parameter will change the mesher's setting.
- This is a required input.

## Return Code

A _Boolean_ of _True_ if success, or _False_ if fail.

## Sample Code

```psj {5,6,7,8,9,10,11,12,13,14,15}
Geometry.Part.Cube()

Geometry.FCircVertexAdjust(crlParts=[Part(1)])

mesh_attribute = Meshing.SetMeshAttribute(crlParts=[Part(1)], 
                                          surfaceMesh=SURFACE_MESH(dAvgElemSize=0.004,
                                                                   dMaxElemSize=0.015, 
                                                                   dMinElemSize=0.0005, 
                                                                   dGeomAngle=0.7853981634, 
                                                                   dGeomMinSize=0.0005,
                                                                   dMinStretchVal=0.0, 
                                                                   iPerformanceMode=1, 
                                                                   dAutoMergeTinyFacesAngle=0.5235987756, 
                                                                   bGeomApprox=True,
                                                                   iNextEntityOffsetId=0))

JPT.Debugger(mesh_attribute)

Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                       surfaceMesh=SURFACE_MESH(dAvgElemSize=0.004, 
                                                dMaxElemSize=0.015,
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
