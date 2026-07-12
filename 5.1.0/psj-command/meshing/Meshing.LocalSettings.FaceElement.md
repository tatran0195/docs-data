---
id: Meshing-LocalSettings-FaceElement
title: Meshing.LocalSettings.FaceElement()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set the mesh setting for the selected elements (Define the settings before surface mesh creation)
---

## Description

Set the mesh setting for the selected elements (Define the settings before surface mesh creation).

## Syntax

```psj
Meshing.LocalSettings.FaceElement(...)
```

Ribbon: <menuselection>Meshing &#187; LocalSettings &#187; FaceElement</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of the local mesh setting.
- This is a required input.

### `localMesh`

- A _[LOCAL_MESH](./../../data-type/psj-command/parameter-types/LOCAL_MESH)_ specifying the local mesh setting's parameter.
- This is a required input.

### `crlTargets`

- A _List of Cursor_ specifying the target Elements of the local mesh setting.
- This is a required input.

### `crEditTarget`

- A _Cursor_ specifying an existed local mesh setting Face. When this parameter is used, the specified local mesh setting Face will be overwritten. When it is not used, a new local mesh setting Face will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created local mesh setting.

## Sample Code

```psj {3,4,5,6,7,8,9}
Geometry.Part.Cube()

created_local_mesh_setting = Meshing.LocalSettings.FaceElement(strName="MeshParam_1", 
                                                               localMesh=LOCAL_MESH(iEntityType=2,
                                                                                    bEnableSizeParams=True, 
                                                                                    dAvgElemSize=0.005, 
                                                                                    dMaxElemSize=0.01, 
                                                                                    dMinElemSize=0.001), 
                                                               crlTargets=[Elem(970)])

JPT.Debugger(created_local_mesh_setting)
```
