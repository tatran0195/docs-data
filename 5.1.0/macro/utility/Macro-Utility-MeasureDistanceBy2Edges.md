---
id: MeasureDistanceBy2Edges
title: MeasureDistanceBy2Edges()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Measure the distance between the two edges

## Syntax

```psj
MeasureDistanceBy2Edges(cursor edge,cursor node,Integer N)
```

## Inputs

### `1. Cursor`

edge cursor(5:_,_=edge id)

### `2. Cursor`

edge cursor(5:_,_=edge id)

### `3. Integer N`

specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureDistanceBy2Edges(5:18,5:11,6)
```
