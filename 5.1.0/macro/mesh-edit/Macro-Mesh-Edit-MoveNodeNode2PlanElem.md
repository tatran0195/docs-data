---
id: MoveNodeNode2PlanElem
title: MoveNodeNode2PlanElem()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Move Nodes from Node to Element plane

## Syntax

```psj
MoveNodeNode2PlanElem(int[] iNodeKey, int[] iElemkey)
```

## Inputs

### `1. Int[]`

Node key cursor([Node ID])

### `2. Int[]`

Element key cursor([Elem ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MoveNodeNode2PlanElem([187], [883])
```
