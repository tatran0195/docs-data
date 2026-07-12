---
id: HexBoxMesh
title: HexBoxMesh()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Box hex mesh creator for parts

## Syntax

```psj
HexBoxMesh(int[] taBodyKey, double dMeshSize, string sMaterialName)
```

## Inputs

### `1. Int[]`

Body ID

### `2. Double`

Box mesh size

### `3. String`

Material Name

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
HexBoxMesh([1], 0.002, "Magnesium_Alloy")
```
