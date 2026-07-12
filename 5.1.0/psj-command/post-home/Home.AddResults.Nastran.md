---
id: Home-AddResults-Nastran
title: Home.AddResults.Nastran()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Add Nastran Op2 results to the current Jupiter Database. 
---

## Description

Add Nastran Op2 results to the current Jupiter Database. The Jupiter document should be Post document.

## Syntax

```psj
Home.AddResults.Nastran(...)
```

Macro: [AddResultsNastran](../../macro/home/AddResultsNastran)

Ribbon: <menuselection>Home &#187; AddResults &#187; Nastran</menuselection>

## Inputs

### `strlPaths`

- A _List of String_ specifying a list of the Nastran files (\*.op2 files) which will be used for importing.
- This is a required input.

### `bMergeTree`

- A _Boolean_ specifying whether or not the differences not included in the existing document will be added.
- The default value is _True_.

### `bCreateResultAtMidNode`

- A _Boolean_ specifying whether or not create result at Mid Nodes.
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Nastran result is added to the document successfully.
  - False: The Nastran result is not added to the document.

## Sample Code

```psj {8}
# Put your sample files
Mesh = "C:/Temp/mesh.bdf"
Result = "C:/Temp/result.op2"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.Nastran(strlPaths=[Result], bMergeTree=False)
```
