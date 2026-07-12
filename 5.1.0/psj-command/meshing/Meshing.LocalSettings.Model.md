---
id: Meshing-LocalSettings-Model
title: Meshing.LocalSettings.Model()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set the mesh setting for the whole model (Define the settings before surface mesh creation)
---

## Description

Set the mesh setting for the whole model (Define the settings before surface mesh creation).

## Syntax

```psj
Meshing.LocalSettings.Model(...)
```

Ribbon: <menuselection>Meshing &#187; LocalSettings &#187; Model</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of the local mesh setting.
- This is a required input.

### `localMesh`

- A _[LOCAL_MESH](./../../data-type/psj-command/parameter-types/LOCAL_MESH)_ specifying the local mesh setting's parameter.
- This is a required input.

### `spaceMesh`

- A _[SPACE_MESH](./../../data-type/psj-command/parameter-types/SPACE_MESH)_ specifying the space mesh setting's parameter.
- This is a required input.

### `crlTargets`

- A _List of Cursor_ specifying the target Faces of the local mesh setting.
- This is a required input.

### `crEditTarget`

- A _Cursor_ specifying the edit target.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created local mesh setting.

## Sample Code

```psj {7,8,9,10,11,12,13,14,15,16,17}
Geometry.Part.Cube()

Meshing.LocalSetting.SearchTargetFaces(dlLength=[0.003, 0.003, 0.003],
                                       dlAxisPt1=[0.0, 0.0, 0.01],
                                       dlAxisPt2=[0.005, 0.0, 0.0])

created_local_mesh_setting = Meshing.LocalSettings.Model(strName="MeshParam_1",
                                                         localMesh=LOCAL_MESH(iEntityType=11,
                                                                              bEnableSizeParams=True,
                                                                              dAvgElemSize=0.001,
                                                                              dMaxElemSize=0.01,
                                                                              dMinElemSize=0.0005,
                                                                              dTrimAngle=0.7853981634),
                                                         spaceMesh=SPACE_MESH(vLength=[0.003, 0.003, 0.003],
                                                                              vAxisPt2=[0.005, 0.0, 0.0],
                                                                              dMinElemSize=0.001),
                                                         crlTargets=[Face(21, 23, 25)])

JPT.Debugger(created_local_mesh_setting)
```
