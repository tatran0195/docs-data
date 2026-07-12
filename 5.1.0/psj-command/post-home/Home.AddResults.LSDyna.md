---
id: Home-AddResults-LSDyna
title: Home.AddResults.LSDyna()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Add LS-Dyna's d3plot results to the current Jupiter Database. 
---

## Description

Add LS-Dyna's d3plot results to the current Jupiter Database. 

## Syntax

```psj
Home.AddResults.LSDyna(...)
```

Macro: [AddResultsLSDyna](../../macro/home/AddResultsLSDyna)

Ribbon: <menuselection>Home &#187; AddResults &#187; LSDyna</menuselection>

## Inputs

### `strlPaths`

- A _List of String_ specifying specifying a list of the d3plot files which will be used for importing.
- This is a required input.

### `bMergeTree`

- A _Boolean_ specifying whether or not the differences not included in the existing document will be added.
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The LS-Dyna result is added to the document successfully.
  - False: The LS-Dyna result is not added to the document.

## Sample Code

```psj {8}
# Put your sample files
Mesh = "C:/Temp/mesh.bdf"
Result = "C:/Temp/d3plot"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.LSDyna(strlPaths=[Result], bMergeTree=False)
```
