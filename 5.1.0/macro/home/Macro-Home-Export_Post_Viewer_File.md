---
id: Export_Post_Viewer_File
title: Export_Post_Viewer_File()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Export geometry surface.

## Syntax

```psj
Export_Post_Viewer_File(int iGroupType, str strFileName)
```

## Inputs

### `1. int`

- A integer specifying group type. 

### `2. str`

- A string specifying file name.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Export_Post_Viewer_File(0, "strFileName")
```
