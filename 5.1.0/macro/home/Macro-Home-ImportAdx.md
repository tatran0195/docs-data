---
id: ImportAdx
title: ImportAdx()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Import adx files

## Syntax

```psj
ImportAdx(string[] vecPath, double faceAngle, double edgeAngle)
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
ImportAdx(["D:/Test.adx"], 1.0472, 1.0472)
```
