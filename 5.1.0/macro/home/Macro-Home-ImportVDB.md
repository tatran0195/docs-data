---
id: ImportVDB
title: ImportVDB()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Import TSV VDB file

## Syntax

```psj
ImportVDB(string SourceFilePath, string SaveFolderPath)
```

## Inputs

### `1. String`

Path of file to import

### `2. String`

Path directory to save

:::note
If this parameter is not indicated, converted files are saved under Temp folder.
:::

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportVDB("D:/Source.vdb","D:/ConvertedMyFile/")
```
