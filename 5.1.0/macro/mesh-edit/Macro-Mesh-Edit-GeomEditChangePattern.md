---
id: GeomEditChangePattern
title: GeomEditChangePattern()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Change Pattern

## Syntax

```psj
GeomEditChangePattern(int[] Face Key, int Pattern Type)
```

## Inputs

### `1. Int[]`

Target Faces for Change Pattern

### `2. Int`

Change Pattern Type[Standard/Union Jack]

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
GeomEditChangePattern([24, 26], 1))
```
