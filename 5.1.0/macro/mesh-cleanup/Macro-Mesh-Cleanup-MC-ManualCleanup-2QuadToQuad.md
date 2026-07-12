---
id: MC_ManualCleanup_2QuadToQuad
title: MC_ManualCleanup_2QuadToQuad()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Merge two Quad elements into one Quad element

## Syntax

```psj
MC_ManualCleanup_2QuadtoQuad(cursor[] elemList)
```

## Inputs

### `1. Cursor[]`

Target element cursor([11:Element ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MC_ManualCleanup_2QuadToQuad([11:1047, 11:1045])
```
