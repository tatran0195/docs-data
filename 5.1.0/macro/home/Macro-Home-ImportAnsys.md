---
id: ImportAnsys
title: ImportAnsys()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Import Ansys file

## Syntax

```psj
ImportAnsys(string[] vecPath, double faceAngle, double edgeAngle)
```

## Inputs

### `1. String[]`

Path directory

### `2. Double`

Face angle

### `3. Double`

Edge angle

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportAnsys(["D:/Test.dat"], 1.0472, 1.0472)
```
