---
id: Home-ImportResults-WAON
title: Home.ImportResults.WAON()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import WAON result file to the Jupiter Database.
---

## Description

Import WAON result file to the Jupiter Database.

## Syntax

```psj
Home.ImportResults.WAON(...)
```

Macro: [CmdImportTSVWAONPost](../../macro/home/CmdImportTSVWAONPost)

Ribbon: <menuselection>Home &#187; ImportResults &#187; WAON</menuselection>

## Inputs

### `strPath`

- A _String_ specifying BEM file (.bdf).
- This is a required input.

### `strFPMFilePath`

- A _String_ specifying FPM file (.bdf).
- This is a required input.

### `strResultFolderPath`

- A _String_ specifying result folder.
- This is a required input.

### `iImportType`

- An _Integer_ specifying import type. For WAON file, it is always set to 1.
- The default value is 1.

### `dFaceAngle`

- A _Double_ specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0 (degree).

### `dEdgeAngle`

- A _Double_ specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0 (degree).

### `bReadLoadAndConstraint`

-A _Boolean_ specifying whether or not 
- The default value is _False_.

### `bReadConnection`

-A _Boolean_ specifying whether or not 
- The default value is _False_.

### `bCreateResultsAtMidNode`

-A _Boolean_ specifying whether or not 
- The default value is _False_.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The WAON result is imported successfully.
- False: The WAON result cannot be imported.

## Sample Code

```psj {6-11}
#Please set path to your sample WAON file.
filepath="C:/Temp/"
bem_file = filepath + "BEM.bdf"
fpm_file = filepath + "FPM.bdf"
result = base_FILEPATH + "result/"
Home.ImportResults.WAON(bem_file, 
                        fpm_file, 
                        result, 
                        bReadLoadAndConstraint=True, 
                        bReadConnection=True, 
                        bCreateResultsAtMidNode=True)
```
