---
id: MeshEditExtractSurfaces
title: MeshEditExtractSurfaces()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Extract Surfaces

## Syntax

```psj
MeshEditExtractSurfaces(Cursor[] Face Cursor, double Angle, string New Body Name)
```

## Inputs

### `1. Cursor[]`

Target Faces for Extraction

### `2. Double`

Extracting Angle for Adjacent Faces

### `3. String`

Extracted Body Name

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeshEditExtractSurfaces([6:22, 6:23, 6:26], 1.0472, "New Body")
```
