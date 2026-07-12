---
id: Meshing-LocalSettings-Points
title: Meshing.LocalSettings.Points()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: LocalSettings.Points
---

## Description

Specify setting for fixed node position (Hard Point) when you create surface mesh, to ensure node creation at a specified location.

## Syntax

```psj
Meshing.LocalSettings.Points(...)
```

Ribbon: <menuselection>Meshing &#187; LocalSettings &#187; Points</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of the local mesh setting.
- This is a required input.

### `localMesh`

- A _[LOCAL_MESH](./../../data-type/psj-command/parameter-types/LOCAL_MESH)_
  specifying the local mesh setting's parameter.
- This is a required input.

### `veclHardPointXYZ`

- A _Vector List_ specifying the list of hard points' position in terms of x, y, z.
- This is a required input.

### `crlHardPointTarget`

- A _List of Cursor_ specifying the list of hard points' target. If point is on Face, target is that Face. If point is on Edge, target is that Edge.
- This is a required input.

### `crEditTarget`

- A _Cursor_ specifying an existed local mesh setting Point. When this parameter is used, the specified local mesh setting Point will be overwritten. When it is not used, a new local mesh setting Point will be created.
- The default value is _None_.

## Return Code

A _Cursor_ of the newly created local mesh setting.

## Sample Code

```psj {2-4}
Geometry.Part.Cube(iPartColor=7731705)
Meshing.LocalSettings.Points(strName="MeshParam_1", localMesh=LOCAL_MESH(bEnableSizeParams=True,
  dAvgElemSize=0.002, dMaxElemSize=0.01, dMinElemSize=0.001), veclHardPointXYZ=[[0.002078861077076959,
  0.008516764027639453, 0.01]], crlHardPointTarget=[Face(26)])
Meshing.SetMeshAttribute(crlParts=[Part(1)], surfaceMesh=SURFACE_MESH(dMinElemSize=0.0005,
  dGeomAngle=0.7853981634, dGeomMinSize=0.0005, iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756,
  bGeomApprox=True, iNextEntityOffsetId=0))
Meshing.SurfaceMeshing(crlParts=[Part(1)], surfaceMesh=SURFACE_MESH(dMinElemSize=0.0005, dGeomAngle=0.7853981634,
  dGeomMinSize=0.0005, iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, bGeomApprox=True,
  iNextEntityOffsetId=0), iThreadNum=4)
```
