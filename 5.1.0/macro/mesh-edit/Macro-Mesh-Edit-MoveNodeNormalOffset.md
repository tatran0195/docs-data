---
id: MoveNodeNormalOffset
title: MoveNodeNormalOffset()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Move node(s) in Normal Direction of plane

## Syntax

```psj
MoveNodeNormalOffset(double posMagnitude, int[] iNodeKey)
```

## Inputs

### `1. Double`

Position magnitude

### `2. Int[]`

Node key cursor([Node ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MoveNodeNormalOffset(0.002, [1432])
```
