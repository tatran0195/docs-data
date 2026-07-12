---
id: MeshEdit-MergeNodes
title: MeshEdit.MergeNodes()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Merge nodes
---

## Description

Merge nodes

## Syntax

```psj
MeshEdit.MergeNodes(dTolerance=0.01, iKeepType=0, crlTargets=[], bGroup=False, bEquivalence=True)
```

Ribbon: <menuselection>MeshEdit &#187; MergeNodes</menuselection>

## Inputs

### `dTolerance`

- A _Double_ specifying the tolerance.
- The default value is 0.01.

### `iKeepType`

- An _Integer_ specifying the keep type.
- The default value is 0.

### `crlTargets`

- A _List of Cursor_ specifying the target.
- The default value is [].

### `bGroup`

- A _Boolean_ specifying the group.
- The default value is False.

### `bEquivalence`

- A _Boolean_ specifying the equivalence.
- The default value is True.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MergeNodes(dTolerance=0.01, iKeepType=0, crlTargets=[], bGroup=False, bEquivalence=True)
```
