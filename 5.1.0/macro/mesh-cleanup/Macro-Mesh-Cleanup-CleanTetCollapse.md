---
id: CleanTetCollapse
title: CleanTetCollapse()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Cleanup tetrahedral mesh by Metric:Tet Collapse.

## Syntax

```psj
CleanTetCollapse(cursor[] crlElems, int iKeepSurfMesh, int iCondition, double dLimitValue, int iMode)
```

## Inputs

### `1. Cursor[]`

The list of target element cursors.

### `2. Int`

The keeping method of surface mesh.
- 0: Default, no keep.
- 1: Keep Surface Mesh for all the mesh.
- 2: Keep Surface Mesh at Freeze Mesh area.

### `3. Int`

The condition.
- 0: &lt;=, Collapse the elements to cleanup.
- 1: &gt;=, Split the elements to cleanup.
- 2: &lt;, Collapse the elements to cleanup.
- 3: &gt;, Split the elements to cleanup.

### `4. Double`

The cleaning threshold value.

### `5. Int`

The cleaning mode.
- 0: Method S
- 1: Method A
- 2: Method D

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CleanTetCollapse([Elem(126, 151, 163)], 0, 0, 0.05, 0)
```
