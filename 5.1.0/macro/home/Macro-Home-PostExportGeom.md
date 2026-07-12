---
id: PostExportGeom
title: PostExportGeom()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Export geometry surface.

## Syntax

```psj
PostExportGeom(str strFolderName, bool bUseUnit)
```

## Inputs

### `1. str`

- A string specifying the path to forder name.

### `2. bool`

- A boolean specifying whether or not use unit.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
PostExportGeom("path/to/the/folder", 1)
```
