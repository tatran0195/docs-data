---
id: MeasureDistanceByEdge_Node
title: MeasureDistanceByEdge_Node()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Measure the distance between the Edge and the Note

## Syntax

```psj
MeasureDistanceByEdge_Node(cursor edge,cursor node,Integer N)
```

## Inputs

### `1. Cursor`

edge cursor(5:_,_=edge id)

### `2. Cursor`

node cursor(10:_,_=node id)

### `3. Integer N`

specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureDistanceByEdge_Node(5:18,10:459,6)
```
