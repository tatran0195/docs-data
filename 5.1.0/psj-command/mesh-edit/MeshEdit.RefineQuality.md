---
id: MeshEdit-RefineQuality
title: MeshEdit.RefineQuality()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Resolve poor-quality mesh within the selected face/element/node set by relocating mesh nodes.
---

## Description

Resolve poor-quality mesh within the selected face/element/node set by relocating mesh nodes.

## Syntax

```psj
MeshEdit.RefineQuality(iMetric, crlFaces, crlElems, crlNodes)
```

Ribbon: <menuselection>MeshEdit &#187; RefineQuality</menuselection>

## Inputs

### `iMetric`

- An _Integer_ specifying the metric.
- This is a required input.

### `crlFaces`

- A _List of Cursor_ specifying the face.
- This is a required input.

### `crlElems`

- A _List of Cursor_ specifying the element.
- This is a required input.

### `crlNodes`

- A _List of Cursor_ specifying the node.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.RefineQuality(iMetric, crlFaces, crlElems, crlNodes)
```
