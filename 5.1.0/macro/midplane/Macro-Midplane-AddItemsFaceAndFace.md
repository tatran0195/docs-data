---
id: AddItemsFaceAndFace
title: AddItemsFaceAndFace()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Add Items Edge by projecting Extend Face's Edge at the extended end of Reference Face

## Syntax

```psj
AddItemsFaceAndFace(Cursor[] Face, int Extend Type)
```

## Inputs

### `1. Cursor []`

Face List

### `2. Int`

Extend Type [Extend,Intersect]

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AddItemsEdgeFaceandFace([6:62, 6:51],0)
```
