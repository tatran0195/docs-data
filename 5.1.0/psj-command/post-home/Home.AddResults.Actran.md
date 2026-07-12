---
id: Home-AddResults-Actran
title: Home.AddResults.Actran()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Add Actran Op2 results to the current Jupiter Database.
---

## Description

Add Actran Op2 results to the current Jupiter Database. The Jupiter document should be Post document.

## Syntax

```psj
Home.AddResults.Actran(...)
```

Macro: [AddResultsActran](../../macro/home/AddResultsActran)

Ribbon: <menuselection>Home &#187; AddResults &#187; Actran</menuselection>

## Inputs

### `strlPaths`

- A _List of String_ specifying a list of the Actran files (\*.op2 files) which will be used for importing.
- This is a required input.

### `bMergeTree`

- A _Boolean_ specifying whether or not the differences not included in the existing document will be added.
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Actran result is added to the document successfully.
  - False: The Actran result is not added to the document.

## Sample Code

```psj {6}
# Please put mesh and actran file below path
meshfile='C:/Sample/mesh.bdf'
actrandatafile= 'C:/Sample/actran.op2'

Home.ImportResults.ImportMesh.Nastran(meshfile, bReadLoadAndConstraint=True, bReadConnection=True)
Home.AddResults.Actran(strlPaths=[actrandatafile], bMergeTree=False)
```
