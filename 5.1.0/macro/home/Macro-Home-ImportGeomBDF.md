---
id: ImportGeomBDF
title: ImportGeomBDF()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Import Geometry bdf file

## Syntax

```psj
ImportGeomBDF(string[] vecPath, bool use_unit)
```

## Inputs

### `1. String[]`

Path directory

### `2. Bool`

Use unit True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportGeomBDF(["D:/test.bdf"], 1)
```
