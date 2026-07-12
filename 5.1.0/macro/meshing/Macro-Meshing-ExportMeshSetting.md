---
id: ExportMeshSetting
title: ExportMeshSetting()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Save local setting

## Syntax

```psj
ExportMeshSetting(string fname,int type)
```

## Inputs

### `1. String`

the file name to save local setting

### `2. Int`

the save mode, in this function the value is fixed to 3

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ExportMeshSetting("D:/test.xml", 3)
```
