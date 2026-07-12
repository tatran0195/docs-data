---
id: Home-ImportResults-Radioss
title: Home.ImportResults.Radioss()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import Open Radioss result file.
---

## Description

Import Open Radioss result file.

## Syntax

```psj
Home.ImportResults.Radioss(...)
```

Macro: [ImportRadioss](../../macro/home/ImportRadioss)

Ribbon: <menuselection>Home &#187; ImportResults &#187; Radioss</menuselection>

## Inputs

### `strlPaths`

- A _List of String_ specifying Open Radioss result file path.
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

### `bReadLoadAndConstraint`

- A _Boolean_ specifying whether or not to read loads and constraint.
- The default value is _False_.

### `bReadConnection`

- A _Boolean_ specifying whether or not to read connections.
- The default value is _False_.

### `bCreateResultsAtMidNode`

- A _Boolean_ specifying whether or not create result at Mid Nodes.
- The default value is _False_.
- The default value is _False_.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Open Radioss file is imported successfully.
  - False: The Open Radioss cannot be imported.

## Sample Code

```psj {4}
# Please set path to your sample radioss file.
filepath="C:/Temp/result.A001"

Home.ImportResults.Radioss(filepath)
```
