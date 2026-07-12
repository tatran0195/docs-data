---
id: LoadDB
title: LoadDB()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

LoadDB

## Syntax

```psj
LoadDB(string PathFile, bool bUseTmpTable)
```

## Inputs

### `1. String`

jtdb import file path

### `2. Bool`

bool Use Temp Table flag true=1, false=0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
LoadDB("D:/Test.jtdb", 0)
```
