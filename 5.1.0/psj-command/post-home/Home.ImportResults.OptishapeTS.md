---
id: Home-ImportResults-OptishapeTS
title: Home.ImportResults.OptishapeTS()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import Optishape-TS result file.
---

## Description

Import Optishape-TS result file.

## Syntax

```psj
Home.ImportResults.OptishapeTS(...)
```

Macro: [ImportOptishapeTS](../../macro/home/ImportOptishapeTS)

Ribbon: <menuselection>Home &#187; ImportResults &#187; OptishapeTS</menuselection>

## Inputs

### `strlPaths`

- A List of _String_ specifying Optishape-TS result file paths.
- This is a required input.

### `iImportType`

- An _Integer_ specifying import type. For Optishape-TS, it is always set to 1. 
- The default value is 1.

### `dFaceAngle`

- A _Double_ specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0 (degree).

### `dEdgeAngle`

- A _Double_ specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0 (degree).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Optishape file is imported successfully.
  - False: The Optishape file cannot be imported.

## Sample Code

```psj {5-6}
import os
#Put your result
result_data='C:/Temp/OptiShapeResult'

Home.ImportResults.OptishapeTS(
    strlPaths=[os.path.join(result_data,"sample.op2")])
```
