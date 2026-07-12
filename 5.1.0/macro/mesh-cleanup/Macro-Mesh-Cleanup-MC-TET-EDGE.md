---
id: MC_TET_EDGE
title: MC_TET_EDGE()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Command for cleaning tetrahedral mesh elements by edge length.

## Syntax

```psj
MC_TET_EDGE(cursor[] crlElements, int iCondition, double dLimitValue, int iMode, int iNonManifold, int iKeepSurfMesh, int iKeepSurfMeshMode)
```

## Inputs

### `1. Cursor[]`

The list of target element cursors.

### `2. Int`

The cleanup condition.

### `3. Double`

The cleanup threshold value.

### `4. Int`

The cleanup mode.
- 0: Standard
- 1: Aggressive

### `5. Int`

Whether to include non-manifold elements.
- 0: Exclude
- 1: Include

### `6. Int`

The keeping method of surface mesh.
- 0: Default, no keep.
- 1: Keep Surface Mesh for all the mesh.
- 2: Keep Surface Mesh at Freeze Mesh area.

### `7. Int`

The keeping mode of surface mesh.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MC_TET_EDGE([Elem(126, 151, 163)], 0, 0.1, 0, 0, 0, 3)
```
