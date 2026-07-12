---
id: Home-ImportResults-ADVC
title: Home.ImportResults.ADVC()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import ADVC result file.
---

## Description

Import ADVC result file.

## Syntax

```psj
Home.ImportResults.ADVC(...)
```

Macro: [ImportADVC](../../macro/home/ImportADVC)

Ribbon: <menuselection>Home &#187; ImportResults &#187; ADVC</menuselection>

## Inputs

### `strPath`

- A _String_ specifying ADVC result folder path.
- This is a required input.

### `iImportType`

- An _Integer_ specifying import type:
  - 1: Standard ADVC2 by Property
  - 2: Simple Topology
- The default value is 1.

### `dFaceAngle`

- A _Double_ specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0 (degree).

### `dEdgeAngle`

- A _Double_ specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0 (degree).

### `bADVCProcessNameRule`

- A _Boolean_ specifying whether or not ADVC process IDs defined on the ADVC side are displayed.
- The default value is _False_.

### `bDisplayNAResult`

- A _Boolean_ specifying whether or not the "NA Result Display" option in ADVC is enabled. When set to true, it shows "Data: ---" for missing data and "No data available" in watch data notes, applicable only to nodal output results. When set to false, standard data display rules apply.
- The default value is _False_.

### `strSelectResultFilePath`

- A _String_ specifying .xml file that defines which result is imported.
- The default value is "".

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The ADVC file is imported successfully.
  - False: The ADVC file cannot be imported.



## Sample Code

```psj {4}
#Please set path to your sample ADVC folder.
folderpath="C:/Temp/SampleADVC"

Home.ImportResults.ADVC(folderpath)
```
