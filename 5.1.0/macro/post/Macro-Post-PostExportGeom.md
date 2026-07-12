---
id: PostExportGeom
title: PostExportGeom()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Export deformed shape by Post deformation as stl files.

## Syntax

```psj
PostExportGeom(string folder, bool bUseUnit)
```

## Inputs

### `1. string `

Export file path.

### `2. bool `

Use document unit.

## Return Code

- "1": Succeeded.
- "0": Failed.

## Sample Code

```psj
PostExportGeom("C:/Users/TechnoStar/Desktop/temp", 1)
```
