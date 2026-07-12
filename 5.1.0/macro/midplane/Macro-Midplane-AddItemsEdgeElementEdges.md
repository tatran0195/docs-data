---
id: AddItemsEdgeElementEdges
title: AddItemsEdgeElementEdges()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Add Items Edge from Element Edges

## Syntax

```psj
AddItemsEdgeElementEdges(elemEdge[] ElemEdge, bool BreakFace)
```

## Inputs

### `1. ElemEdge []`

Target Element Edges for Creating New Edge

### `2. Bool`

Break Face. true = 1,false = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateEdgeByElemEdge([10:172-10:180, 10:180-10:188, 10:188-10:196], 1)
```
