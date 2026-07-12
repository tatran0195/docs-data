---
id: ImportInpToPost
title: ImportInpToPost()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Import inp mesh as Post document.

## Syntax

```psj
ImportInpToPost(string FilePath, float faceAngle, float edgeAngle, int ImportType)
```
## Inputs

### `1. string  `

File path.

### `2. float  `

Face Angle.

### `3. float  `

Edge Angle.

### `4. int  `

Import Type
0: Standard Abaqus Inp
1: Standard Abaqus Inp by Property

## Return Code

Nothing.

## Sample Code

```psj
ImportInpToPost(["C:/Temp/Data.inp"], 1.0472, 1.0472, 1)
```
