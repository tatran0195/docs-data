---
id: Home-AddResults-Abaqus
title: Home.AddResults.Abaqus()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Add Abaqus .odb results to the current Jupiter Database. 
---

## Description

Add Abaqus .odb results to the current Jupiter Database. 

## Syntax

```psj
Home.AddResults.Abaqus(...)
```

Macro: [AddResultsAbaqus](../../macro/home/AddResultsAbaqus)

Ribbon: <menuselection>Home &#187; AddResults &#187; Abaqus</menuselection>

## Inputs

### `strlPaths`

- A _List of String_ specifying a list of the Abaqus files (\*.odb files) which will be used for importing.
- This is a required input.

### `bMergeTree`

- A _Boolean_ specifying whether or not the differences not included in the existing document will be added.
- The default value is _True_.

### `iVersion`

- An _Integer_ specifying version of Abaqus file.
- The default value is 2019.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Abaqus result is added to the document successfully.
  - False: The Abaqus result is not added to the document.

## Sample Code

```psj {8}
# Put your sample files
Mesh = "C:/Temp/mesh.inp"
Result = "C:/Temp/result.odb"

# Import mesh file
Home.ImportResults.ImportMesh.Abaqus(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.Abaqus(strlPaths=[Result], bMergeTree=False)
```
