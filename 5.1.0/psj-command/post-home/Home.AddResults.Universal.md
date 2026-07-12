---
id: Home-AddResults-Universal
title: Home.AddResults.Universal()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Add result written in Universal file to the current Jupiter-Post Database.
---

## Description

Add result written in Universal file (*.unv) to the current Jupiter-Post Database.

## Syntax

```psj
Home.AddResults.Universal(...)
```

Macro: [AddResultsUniversal](../../macro/home/AddResultsUniversal)

Ribbon: <menuselection>Home &#187; AddResults &#187; Universal</menuselection>

## Inputs

### `strlPaths`

- A _List of String_ specifying .unv file path.
- This is a required input.

### `bMergeTree`

- A _Boolean_ specifying whether or not the differences not included in the existing document will be added.
- The default value is _True_.

## Return Code

- A _Boolean_ specifyingthe the function is executed successfully or not:
  - True: The Universal file (\*.unv file) is added successfully.
  - False: The Universal file (\*.unv file) cannot be added.

## Sample Code

```psj {8}
# Put your sample files
Mesh = "C:/Temp/mesh.bdf"
Result = "C:/Temp/result.unv"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.Universal(strlPaths=[Result], bMergeTree=False)
```
