---
id: ImportFromMLIB
title: ImportFromMLIB()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Import materials from a .mlib file into the library database.

## Syntax

```psj
ImportFromMLIB(string fileName)
```

## Inputs

### `1. string`

Path of .mlib file.


## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportFromMLIB("//NetworkMachine/shared_folder/sample.mlib")

```
