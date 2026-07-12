---
id: ChangeTopologyFace
title: ChangeTopologyFace()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Change Topology Face

## Syntax

```psj
ChangeTopologyFace(int[] taFaceKey, int[] taBodyKey, bool bCreateNewBody)
```

## Inputs

### `1. Int[]`

Face key cursor([Face ID])

### `2. Int[]`

Part key cursor([Part ID])

### `3. Bool`

Create new part bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ChangeTopologyFace([8], [2], 1)
```
