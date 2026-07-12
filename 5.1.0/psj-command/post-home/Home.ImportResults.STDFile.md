---
id: Home-ImportResults-STDFile
title: Home.ImportResults.STDFile()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import std result file.
---

## Description

Import std result file.

## Syntax

```psj
Home.ImportResults.STDFile(...)
```

Macro: [ImportSTDFile](../../macro/home/ImportSTDFile)

Ribbon: <menuselection>Home &#187; ImportResults &#187; STDFile</menuselection>

## Inputs

### `strPath`

- A _String_ specifying std result file path.
- This is a required input.

### `iImportType`

- An _Integer_ specifying import type. For STDFile, it is always set to 1. 
- The default value is 1.

### `dFaceAngle`

- A _Double_ specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0 (degree).

### `dEdgeAngle`

- A _Double_ specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0 (degree).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The STD file (\*.std file) is imported successfully.
  - False: The STD file (\*.std file) cannot be imported.

## Sample Code

```psj {4}
#Please set path to your sample std file.
filepath="C:/Temp/Sample.std"

Home.ImportResults.STDFile(filepath)
```
