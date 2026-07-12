---
id: GeomEditAdjustOrientation
title: GeomEditAdjustOrientation()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Adjust Orientation

## Syntax

```psj
GeomEditAdjustOrientation(cursor[] taBody, cursor[] taFace, cursor[] taElem)
```

## Inputs

### `1. Cursor[]`

Target body cursor([3:Part ID])

### `2. Cursor[]`

Target face cursor([6:Face ID])

### `3. Cursor[]`

Target element cursor([11:Elem ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
GeomEditAdjustOrientation([], [6:40], [11:182])
```
