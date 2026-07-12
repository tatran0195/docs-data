---
id: AddUserResultDefine
title: AddUserResultDefine()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Add user result to the current Jupiter Database.

## Syntax

```psj
UsersResult(str[] strlPath, bool bExportLog)
```

## Inputs

### `1. str[]`

- A List of String specifying user result files.

### `2. bool`

- A Boolean specifying whether or not

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
UsersResult(["path/to/the/file"], 1)
```