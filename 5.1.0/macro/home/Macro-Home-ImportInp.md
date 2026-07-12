---
id: ImportInp
title: ImportInp()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Import Abaqus INP file

## Syntax

```psj
ImportInp(string[] m_vecPath,double m_faceAngle,double m_edgeAngle, int iImportType)
```

## Inputs

### `1. String[]`

Multiple files Path

### `2. Double`

Face angle

### `3. Double`

Edge angle

### `4. Int`

Import type

- 0: Standard Abaqus Inp
- 1: Standard Abaqus Inp by Property

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportInp(["D:/Test.inp"], 1.0472, 1.0472, 1)
```
