---
id: HexSweepCurve
title: HexSweepCurve()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create Hex mesh by curve sweep

## Syntax

```psj
HexSweepCurve(int[] nFaceIds, int[] nEdgeIds, double dMeshSize)
```

## Inputs

### `1. Int[]`

Face Id array for circular sweep

### `2. Int[]`

Edge Id array for circular sweep

### `3. Double`

Mesh Size

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
HexSweepCurve([247], [44], 0.0001)
```
