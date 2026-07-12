---
id: GeometryDeform
title: GeometryDeform()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Deform face

## Syntax

```psj
GeometryDeform(cursor[] taFaceSrcObverse, cursor[] taFaceDstReverse, cursor[] taFaceSrcReverse, cursor[] crlFaceDstObverse, cursor[] crlFaceFixed, double dDistEffect)

```

## Inputs

### `1. Cursor[]`

A List of Cursor specifying the face source obverse.

### `2. Cursor[]`

A List of Cursor specifying the face dst reverse.

### `3. Cursor[]`

A List of Cursor specifying the face source reverse.

### `4. Cursor[]`

A List of Cursor specifying the face dst obverse.

### `5. Cursor[]`

A List of Cursor specifying the face fixed.

### `6. double`

A Double specifying the dist effect.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
GeometryDeform([6:26], [6:21], [6:22], [6:24], [], 0.02)
```
