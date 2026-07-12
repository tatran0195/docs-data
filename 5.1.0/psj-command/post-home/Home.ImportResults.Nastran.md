---
id: Home-ImportResults-Nastran
title: Home.ImportResults.Nastran()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import Nastran / Vibro result file.
---

## Description

Import Nastran / Vibro result file.

## Syntax

```psj
Home.ImportResults.Nastran(...)
```

Macro: [ImportNastran](../../macro/home/ImportNastran)

Ribbon: <menuselection>Home &#187; ImportResults &#187; Nastran</menuselection>

## Inputs

### `strPath`

- A _String_ specifying nastran result file path.
- The default value is "".

### `strlPaths`

- A _List of String_ specifying nastran hdf5 result file paths.
- The default value is [].

### `iImportType`

- An _Integer_ specifying import type:
  - 1: Standard Nastran Op2 by Property
  - 2: Simple Topology
- The default value is 1.

### `dFaceAngle`

- A _Double_ specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0 (degree).

### `dEdgeAngle`

- A _Double_ specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0 (degree).

### `bReadLoadAndConstraint`

- A _Boolean_ specifying whether or not to read loads and constraint.
- The default value is _False_.

### `bReadConnection`

- A _Boolean_ specifying whether or not to read connections.
- The default value is _False_.

### `bCreateResultsAtMidNode`

- A _Boolean_ specifying whether or not create result at Mid Nodes.
- The default value is _False_.

### `bIsVibro`

- A _Boolean_ specifying whether or not the file is Vibro Acoustic.
- The default value is _False_.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Nastran file (\*.op2 file) is imported successfully.
  - False: The Nastran file (\*.op2 file) cannot be imported.

## Sample Code

```psj {5}
import os
NastranFile = os.path.join(
    JPT.GetAppPathInfo(JPT.PathType.PROGRAM_PATH), 
    'SampleData/PSJ/PSJ-Utility/PostSample/101_solid.op2')
Home.ImportResults.Nastran(strPath=NastranFile)
```
