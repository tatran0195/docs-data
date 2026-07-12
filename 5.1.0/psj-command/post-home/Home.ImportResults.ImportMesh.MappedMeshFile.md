---
id: Home-ImportResults-ImportMesh-MappedMeshFile
title: Home.ImportResults.ImportMesh.MappedMeshFile()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import a mapped mesh file to the Jupiter Database as Post document to add result to the mesh.
---

## Description

Import a mapped mesh file (\*.dat) to the Jupiter Database as Post document to add result to the mesh.

## Syntax

```psj
Home.ImportResults.ImportMesh.MappedMeshFile(...)
```

Macro: [ImportMappedMeshFileDat](../../macro/home/ImportMappedMeshFileDat)

Ribbon: <menuselection>Home &#187; ImportResults &#187; ImportMesh &#187; MappedMeshFile</menuselection>

## Inputs

### `strPath`

- A _String_ specifying Mapped Mesh file path.
- This is a required input.

### `iImportType`

- An _Integer_ specifying import type. For Mapped Mesh file, it is always set to 1.
- The default value is 1.

### `dFaceAngle`

- A _Double_ specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0 (degree).

### `dEdgeAngle`

- A _Double_ specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0 (degree).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Mapped Mesh file is imported successfully.
  - False: The Mapped Mesh file cannot be imported.

## Sample Code

```psj {4}
#Please set path to your sample mapped mesh file.
filepath="C:/Temp/SampleFrontISTR"

Home.ImportResults.ImportMesh.MappedMeshFile(filepath)
```
