---
id: Home-AddResults-MappedMeshResult
title: Home.AddResults.MappedMeshResult()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Add mapped mesh result to the current Jupiter Database. 
---

## Description

Add mapped mesh result to the current Jupiter Database. 

## Syntax

```psj
Home.AddResults.MappedMeshResult(...)
```

Macro: [AddResultsMappedMeshFile](../../macro/home/AddResultsMappedMeshFile)

Ribbon: <menuselection>Home &#187; AddResults &#187; MappedMeshResult</menuselection>

## Inputs

### `strlPaths`

- A _List of String_ specifying mapped mesh files.
- This is a required input.

### `bMergeTree`

- A _Boolean_ specifying whether or not the differences not included in the existing document will be added.
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The mapped mesh result is added to the document successfully.
  - False: The mapped mesh result is not added to the document.

## Sample Code

```psj {8}
# Put your sample files
Mesh = "C:/Temp/mesh.bdf"
Result = "C:/Temp/result.dat"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.MappedMeshResult(strlPaths=[Result], bMergeTree=False)
```
