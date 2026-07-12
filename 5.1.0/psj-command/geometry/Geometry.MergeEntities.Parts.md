---
id: Geometry-MergeEntities-Parts
title: Geometry.MergeEntities.Parts()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Merge several parts into a single part. The first selected part will be retained, others will be merged into the first part. Load conditions and material properties, etc., which have been set on faces and edges, will be updated to the merged part automatically
---

## Description

Merge several parts into a single part. The first selected part will be retained, others will be merged into the first part.
Load conditions and material properties, etc., which have been set on faces and edges, will be updated to the merged part automatically.

## Syntax

```psj
Geometry.MergeEntities.Parts(...)
```

Macro: [MergePart](../../macro/geometry/MergePart)

Ribbon: <menuselection>Geometry &#187; Merge Entities &#187; Parts</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the parts to be merged.
- This is a required input.

### `dMergeTolerance`

- A _Double_ specifying the maximum distance between nodes of the given parts that will be merged.
- The default value is 1e-5.

### `bRemoveSharedFace`

- A _Boolean_ specifying whether to remove the shared faces between the given parts after merging.
- The default value is _True_.

## Return Code

A _Cursor_ specifying the merged part.

## Sample Code

```psj {4,5}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0],
                   strName="Cube_2")
merged_part = Geometry.MergeEntities.Parts(crlParts=[Part(1, 2)],
                                           dMergeTolerance=1e-05)
JPT.Debugger(merged_part)
```
