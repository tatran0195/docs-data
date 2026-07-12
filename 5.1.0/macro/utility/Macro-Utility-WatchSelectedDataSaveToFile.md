---
id: WatchSelectedDataSaveToFile
title: WatchSelectedDataSaveToFile()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Save information of watch data docking window.

## Syntax

```psj
WatchSelectedDataSaveToFile(string csvFilePath)
```

## Inputs

### `1. string`

Path of save file (.csv)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
WatchSelectedDataSaveToFile("C:/Temp/sample.csv")
```
