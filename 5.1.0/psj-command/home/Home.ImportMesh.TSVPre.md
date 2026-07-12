---
id: Home-ImportMesh-TSVPre
title: Home.ImportMesh.TSVPre()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Convert a old TSV-Pre/Designer file into one or more jtdb files.
---

## Description

Convert a old TSV-Pre/Designer file into one or more jtdb files.

## Syntax

```psj
Home.ImportMesh.TSVPre(...)
```

Macro: [ImportVDB](../../macro/home/ImportVDB)

Ribbon: <menuselection>Home &#187; ImportMesh &#187; TSVPre</menuselection>

## Inputs

### `strImportPath`

- A _String_ specifying the import path.
- The default value is "".

### `strExportPath`

- A _String_ specifying the export path.
- The default value is "".

### `ilModelIndex`

- A _List of Integer_ specifying the model index.
- The default value is None.

### `iMerge`

- An _Integer_ specifying the merge.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {8}
import os

VDB_file_path = os.path.join(
    JPT.GetAppPathInfo(JPT.PathType.PROGRAM_PATH), 
    "SampleData/PSJ/PSJ-Utility/VDBSample/sample.vdb")

export_file_path = os.environ["Temp"] + "/TechnoStar/"
Home.ImportMesh.TSVPre(strImportPath=VDB_file_path, strExportPath=export_file_path)
```
