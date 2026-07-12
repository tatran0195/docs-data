---
id: Export_Post_Viewer_File
title: Export_Post_Viewer_File()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Export file for PV.

## Syntax

```psj
Export_Post_Viewer_File(int GroupType, string FilePath)
```

## Inputs

### `1. int `

Output Group by 0: No specification, 1: Element, 2: Material, 3: Property.

### `2. string `

Export file path.

## Return Code

Nothing.

## Sample Code

```psj
Export_Post_Viewer_File(1, "C:/Temp/Data.tspv")
```
