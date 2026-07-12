---
id: ImportFrontISTR
title: ImportFrontISTR()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Import FrontISTR result file.

## Syntax

```psj
ImportFrontISTR(str strPath, int iImportType, double dFaceAngle, double dEdgeAngle)
```

## Inputs

### `1. str`

- A String specifying FrontISTR result folder path.

### `2. int`

- An Integer specifying import type.

### `3. double`

- A Double specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

### `4. double`

- A Double specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportFrontISTR("path/to/the/file", 1, 60.0, 60.0)
```