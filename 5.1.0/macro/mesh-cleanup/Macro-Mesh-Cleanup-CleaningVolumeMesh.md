---
id: CleaningVolumeMesh
title: CleaningVolumeMesh()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Cleanup tetrahedral mesh by Metric:Volume.

## Syntax

```psj
CleaningVolumeMesh(cursor[] crlParts, cursor[] crlElems, double dLimitValue, int iMode)
```

## Inputs

### `1. Cursor[]`

The list of target part cursors.

### `2. Cursor[]`

The list of target element cursors.

### `3. Double`

The cleaning threshold value (e.g., minimum volume).

### `4. Int`

The cleaning mode.
- 0: Standard
- 1: Aggressive
- 2: Remove

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CleaningVolumeMesh([Part(1)], [], 2e-09, 1)
```
