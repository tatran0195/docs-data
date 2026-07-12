---
id: MeshCleanup-Manual2D-RemeshElement
title: MeshCleanup.Manual2D.RemeshElement()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: local surface remesh
---

## Description

Local surface remesh

## Syntax

```psj
MeshCleanup.Manual2D.RemeshElement(crlTargets=[], surfaceMesh=SURFACE_MESH(), bUseSetting=False, bGrading=False, bFMesher=False, iOverrideType=0, bKeepConnection=False, bProjCAD=False, bTinyFaceMerge=False, dMinFaceWidth=0, dMaxFaceWidth=0.001, bIDchcek=False, bKeepRemeshEdge=False)
```

Ribbon: <menuselection>MeshCleanup &#187; Manual2D &#187; RemeshElement</menuselection>

## Inputs

### `crlTargets`

- A _List of Cursor_ specifying the target.
- The default value is [].

### `surfaceMesh`

- A _[SURFACE_MESH](./../../data-type/psj-command/parameter-types/SURFACE_MESH)_ specifying the mesh.
- The default value is _[SURFACE_MESH](./../../data-type/psj-command/parameter-types/SURFACE_MESH)_.

### `bUseSetting`

- A _Boolean_ specifying the use setting.
- The default value is False.

### `bGrading`

- A _Boolean_ specifying the grading.
- The default value is False.

### `bFMesher`

- A _Boolean_ specifying the mesher.
- The default value is False.

### `iOverrideType`

- An _Integer_ specifying the override type.
- The default value is 0.

### `bKeepConnection`

- A _Boolean_ specifying the keep connection.
- The default value is False.

### `bProjCAD`

- A _Boolean_ specifying the projection CAD.
- The default value is False.

### `bTinyFaceMerge`

- A _Boolean_ specifying the tiny face merge.
- The default value is False.

### `dMinFaceWidth`

- A _Double_ specifying the minimum face width.
- The default value is 0.

### `dMaxFaceWidth`

- A _Double_ specifying the maximum face width.
- The default value is 0.001.

### `bIDchcek`

- A _Boolean_ specifying the i dchcek.
- The default value is False.

### `bKeepRemeshEdge`

- A _Boolean_ specifying the keep remesh edge.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.RemeshElement(crlTargets=[], surfaceMesh=SURFACE_MESH(), bUseSetting=False, bGrading=False, bFMesher=False, iOverrideType=0, bKeepConnection=False, bProjCAD=False, bTinyFaceMerge=False, dMinFaceWidth=0, dMaxFaceWidth=0.001, bIDchcek=False, bKeepRemeshEdge=False)
```
