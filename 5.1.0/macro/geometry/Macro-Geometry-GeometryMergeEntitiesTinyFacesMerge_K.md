---
id: GeometryMergeEntitiesTinyFacesMerge_K
title: GeometryMergeEntitiesTinyFacesMerge_K()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Merge tiny faces either by extending the user selection or using only the selected faces.

## Syntax

```psj
GeometryMergeEntitiesTinyFacesMerge_K(string method, cursor[] targets, double minFace [3:1], 0, 0.001, 30, 0, 1, [], [])
```

## Inputs

### `1. String`

The method use to merge. Possible values are _AUTO_, _SELECT_, _MERGE_, _RESTORE_.

### `2. Cursor[]`

The parts or faces to be merged.

### `3. Double`

The minimum face width in meter. This argument is used when _strMethod_ has the value _AUTO_ or _SELECT_.

### `4. Double`

The maximum face width in meter. This argument is used when _strMethod_ has the value _AUTO_ or _SELECT_.

### `5. Double`

The angle between faces in degree. This argument is used when _strMethod_ has the value _AUTO_ or _MERGE_.

### `6. Bool`

Whether to refer to the local setting or not.

### `7. Bool`

Whether or not create a reference part.

### `8. cursor[]`

The reference parts.

### `9. cursor[]`

The reference edge.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
GeometryMergeEntitiesTinyFacesMerge_K("AUTO", [3:1], 0, 0.001, 30, 0, 1, [], [])
```
