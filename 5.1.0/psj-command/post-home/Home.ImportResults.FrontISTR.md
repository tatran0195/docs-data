---
id: Home-ImportResults-FrontISTR
title: Home.ImportResults.FrontISTR()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import FrontISTR result file.
---

## Description

Import FrontISTR result file.

## Syntax

```psj
Home.ImportResults.FrontISTR(...)
```

Macro: [ImportFrontISTR](../../macro/home/ImportFrontISTR)

Ribbon: <menuselection>Home &#187; ImportResults &#187; FrontISTR</menuselection>

## Inputs

### `strPath`

- A _String_ specifying FrontISTR result folder path.
- This is a required input.

### `iImportType`

- An _Integer_ specifying import type.
- The default value is 1.

### `dFaceAngle`

- A _Double_ specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0 (degree).

### `dEdgeAngle`

- A _Double_ specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0 (degree).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Front ISTR file is imported successfully.
  - False: The Front ISTR file cannot be imported.


## Sample Code

```psj {4}
#Please set path to your sample FrontISTR folder.
folderpath="C:/Temp/SampleFrontISTR"

Home.ImportResults.FrontISTR(folderpath)
```
