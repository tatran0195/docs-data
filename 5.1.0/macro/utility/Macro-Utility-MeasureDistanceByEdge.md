---
id: MeasureDistanceByEdge
title: MeasureDistanceByEdge()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Measure the edge length

## Syntax

```psj
MeasureDistanceByEdge(cursor edge,Integer N)
```

## Inputs

### `1. Cursor`

edge cursor(5:_,_=edge id)

### `2. Integer N`

specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureDistanceByEdge(5:18,6)
```
