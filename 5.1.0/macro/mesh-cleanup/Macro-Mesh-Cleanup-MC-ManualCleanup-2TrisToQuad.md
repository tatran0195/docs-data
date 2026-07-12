---
id: MC_ManualCleanup_2TrisToQuad
title: MC_ManualCleanup_2TrisToQuad()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Merge two Tri element into one Quad element

## Syntax

```psj
MC_ManualCleanup_2TrisToQuad(Cursor[] elements)
```

## Inputs

### `1. Cursor[]`

Array of only 2 Tri elements

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MC_ManualCleanup_2TrisToQuad([11:1068,11:1066])
```
