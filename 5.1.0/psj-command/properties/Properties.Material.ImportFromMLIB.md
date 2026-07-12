---
id: Properties-Material-ImportFromMLIB
title: Properties.Material.ImportFromMLIB()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import materials from a .mlib file into the library database.
---

## Description

Import materials from a .mlib file into the library database.

## Syntax

```psj
Properties.Material.ImportFromMLIB(...)
```

Macro: ImportFromMLIB

Ribbon: <menuselection>Properties &#187; Material &#187; ImportFromMLIB</menuselection>

## Inputs

### `strFileName`

- A _String_ specifying path of .mlib file.
- The default value is "".

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
# Import .mlib file from a shared folder on a network machine
Properties.Material.ImportFromMLIB(strFileName=r"\\NetworkMachine\shared_folder\sample.mlib")
```
