---
id: MeshEdit-MoveNode-RefineQuality
title: MeshEdit.MoveNode.RefineQuality()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: MeshEdit RefineQuality
---

## Description

MeshEdit RefineQuality

## Syntax

```psj
MeshEdit.MoveNode.RefineQuality(iMetric=0, crlFaces=[], crlElems=[], crlNodes=[])
```

Ribbon: <menuselection>MeshEdit &#187; MoveNode &#187; RefineQuality</menuselection>

## Inputs

### `iMetric`

- An _Integer_ specifying the metric.
- The default value is 0.

### `crlFaces`

- A _List of Cursor_ specifying the face.
- The default value is [].

### `crlElems`

- A _List of Cursor_ specifying the element.
- The default value is [].

### `crlNodes`

- A _List of Cursor_ specifying the node.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.RefineQuality(iMetric=0, crlFaces=[], crlElems=[], crlNodes=[])
```
