---
id: Home-ImportResults-Abaqus
title: Home.ImportResults.Abaqus()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import Abaqus result file.
---

## Description

Import Abaqus result file.

## Syntax

```psj
Home.ImportResults.Abaqus(...)
```

Macro: [ImportAbaqus](../../macro/home/ImportAbaqus)

Ribbon: <menuselection>Home &#187; ImportResults &#187; Abaqus</menuselection>

## Inputs

### `strPath`

- A _String_ specifying abaqus result file path.
- This is a required input.

### `iVersion`

- An _Integer_ specifying version of abaqus file to import.
- This is a required input.

### `iImportType`

- An _Integer_ specifying import type:
- The default value is 1.

### `dFaceAngle`

- A _Double_ specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0 (degree).

### `dEdgeAngle`

- A _Double_ specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0 (degree).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Abaqus file (\*.odb file) is imported successfully.
  - False: The Abaqus file (\*.odb file) cannot be imported.


## Sample Code

```psj {4}
#Please set path to your sample Abaqus file.
filepath="C:/Temp/Sample.odb"

Home.ImportResults.Abaqus(filepath, iVersion=2023)

```
