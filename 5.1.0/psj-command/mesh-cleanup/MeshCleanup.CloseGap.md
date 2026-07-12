---
id: MeshCleanup-CloseGap
title: MeshCleanup.CloseGap()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: MeshCleanup Cleanup CloseGap
---

## Description

MeshCleanup Cleanup CloseGap

## Syntax

```psj
MeshCleanup.CloseGap(crlPartsCur=[], dDistanceTol=0.01)
```

Ribbon: <menuselection>MeshCleanup &#187; CloseGap</menuselection>

## Inputs

### `crlPartsCur`

- A _List of Cursor_ specifying the part cur.
- The default value is [].

### `dDistanceTol`

- A _Double_ specifying the distance tolerance.
- The default value is 0.01.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.CloseGap(crlPartsCur=[], dDistanceTol=0.01)
```
