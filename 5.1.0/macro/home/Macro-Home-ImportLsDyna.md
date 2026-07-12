---
id: ImportLsDyna
title: ImportLsDyna()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Import Ls-Dyna file

## Syntax

```psj
ImportLsDyna(string[] m_vecPath,double m_faceAngle,double m_edgeAngle)
```

## Inputs

### `1. String[]`

Multiple files Path

### `2. Double`

Face angle

### `3. Double`

Edge angle

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportLsDyna(["D:/Test.k"], 1.0472, 1.0472)
```
