---
id: MainWindow-RightClick-MergeFaces
title: MainWindow.RightClick.MergeFaces()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Merge Faces
---

## Description

Merge Faces

## Syntax

```psj
MainWindow.RightClick.MergeFaces(crlFaces, bIsMergeEdge=False, bRemoveNonBoundEdge=True)
```

Ribbon: <menuselection>MainWindow &#187; RightClick &#187; MergeFaces</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the face.
- This is a required input.

### `bIsMergeEdge`

- A _Boolean_ specifying the is merge edge.
- The default value is False.

### `bRemoveNonBoundEdge`

- A _Boolean_ specifying the remove non boundary edge.
- The default value is True.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MainWindow.RightClick.MergeFaces(crlFaces, bIsMergeEdge=False, bRemoveNonBoundEdge=True)
```
