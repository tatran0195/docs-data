---
id: Home-ImportResults-SunShineUStar
title: Home.ImportResults.SunShineUStar()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import a SunShine UStar file to the Jupiter Database.
---

## Description

Import a SunShine UStar file (\*.op2) to the Jupiter Database.

## Syntax

```psj
Home.ImportResults.SunShineUStar(...)
```

Macro: [ImportSunShineUStar](../../macro/home/ImportSunShineUStar)

Ribbon: <menuselection>Home &#187; ImportResults &#187; SunShineUStar</menuselection>

## Inputs

### `strPath`

- A _String_ specifying 
- This is a required input.

### `iImportType`

- An _Integer_ specifying import type:
  - 1: Standard SunShine Op2 by Property
  - 2: Simple Topology
- The default value is 1.

### `dFaceAngle`

- A _Double_ specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0 (degree).

### `dEdgeAngle`

- A _Double_ specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0 (degree).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The SunShine UStar file (\*.op2 file) is imported successfully.
  - False: The SunShine Star file (\*.op2 file) cannot be imported.

## Sample Code

```psj {3}
import os
UstarFile = os.path.join(JPT.GetAppPathInfo(JPT.PathType.APPDATA_PATH), 'SampleData/PSJ/PSJ-Utility/PostSample/plate_beam_ustar.op2')
Home.ImportResults.SunShineUStar(strPath=UstarFile)
```
