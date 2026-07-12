---
id: CmdImportTSVPost
title: CmdImportTSVPost()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Import Result or Mesh file to Post Document

## Syntax

```psj
CmdImportTSVPost(string FilePath, int solverType, int importType, float faceAngle, float edgeAngle)
```

## Inputs
### `1. string  `

File path

### `2. int `

_[Solver type](../../data-type/psj-utility/post-utility/enumeration-types/post-job-type.md)_.

### `3. int  `

Import type

### `4. float  `

Face Angle

### `5. float  `

Edge Angle

## Return Code

Nothing.

## Sample Code

```psj
CmdImportTSVPost("C:/Temp/sample.dat", 9, 1, 1.0472, 1.0472)
```
