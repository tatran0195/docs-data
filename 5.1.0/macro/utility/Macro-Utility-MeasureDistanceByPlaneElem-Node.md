---
id: MeasureDistanceByPlaneElem_Node
title: MeasureDistanceByPlaneElem_Node()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Measure Distance between Node and plane (created by element).

## Syntax

```psj
MeasureDistanceByPlaneElem_Node(cursor node,cursor edge,Integer N)
```

## Inputs

### `1. Cursor`

node cursor(10:_,_=node id)

### `2. Cursor`

edge cursor(11:_,_=edge id)

### `3. Integer N`

specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureDistanceByPlaneElem_Node(10:438,11:362,6)
```
