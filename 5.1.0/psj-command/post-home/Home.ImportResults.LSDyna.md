---
id: Home-ImportResults-LSDyna
title: Home.ImportResults.LSDyna()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import LS-Dyna result file.
---

## Description

Import LS-Dyna result file. Compressed by FEMZIP is not available.

## Syntax

```psj
Home.ImportResults.LSDyna(...)
```

Macro: [ImportLSDyna](../../macro/home/ImportLSDyna)

Ribbon: <menuselection>Home &#187; ImportResults &#187; LSDyna</menuselection>

## Inputs

### `strPath`

- A _String_ specifying LS Dyna result file path.
- This is a required input.

### `iImportType`

- An _Integer_ specifying import type. For LS-Dyna, it is always set to 1. 
- The default value is 1.

### `dFaceAngle`

- A _Double_ specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0 (degree).

### `dEdgeAngle`

- A _Double_ specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0 (degree).


- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The LS-Dyna file (\*.d3plot file) is imported successfully.
  - False: The LS-Dyna file file (\*.d3plot file) cannot be imported.


## Sample Code

```psj {4}
#Please set path to your sample universal file.
filepath="C:/Temp/d3plot"

Home.ImportResults.LSDyna(filepath)
```
