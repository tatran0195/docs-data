---
id: CreateNode
title: CreateNode()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create nodes

## Syntax

```psj
CreateNode(double[3] taNodeCoord, int[] taNodeKey)
```

## Inputs

### `1. Double[]`

Coordinate point([xi, yi, zi])

### `2. Int[]`

Input Node key ([Node ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateNode([[0, 0.005, 0.012],[0, 0.005, 0.020]], [1018,1019])
```
