---
id: Home-AddResults-Sysnoise
title: Home.AddResults.Sysnoise()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Add sysnoise result to the current Jupiter Database
---

## Description

Add sysnoise result to the current Jupiter Database. 

## Syntax

```psj
Home.AddResults.Sysnoise(...)
```

Macro: [AddResultsSysnoise](../../macro/home/AddResultsSysnoise)

Ribbon: <menuselection>Home &#187; AddResults &#187; Sysnoise</menuselection>

## Inputs

### `strlPaths`

- A _List of String_ specifying sysnoise result files.
- This is a required input.

### `bMergeTree`

- A _Boolean_ specifying whether or not the differences not included in the existing document will be added.
- The default value is _True_.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The sysnoise result is added to the document successfully.
  - False: The sysnoise result is not added to the document.

## Sample Code

```psj {8}
# Put your sample files
Mesh = "C:/Temp/mesh.bdf"
Result = "C:/Temp/result"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.Sysnoise(strlPaths=[Result], bMergeTree=False)
```
