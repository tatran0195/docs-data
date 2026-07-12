---
id: ImportGroup
title: ImportGroup()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Import Group written in CSV file.

## Syntax

```psj
ImportGroup(String filePath, Cursor SubGroup)
```

## Inputs

### `1. String[]`

Specify the csv file of group definition.

### `2. Cursor`

Specify the subGroup by cursor.

## Return Code

None.

## Sample Code

```psj
ImportGroup(["C:/Temp/group_file.csv"], 0:0)
```
