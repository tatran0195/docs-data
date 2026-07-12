---
id: MidPlaneEdit-Face-EdgesToEdges
title: MidPlaneEdit.Face.EdgesToEdges()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: add face by edges
---

## Description

Add face by edges

## Syntax

```psj
MidPlaneEdit.Face.EdgesToEdges(crlEdges, bImprint=False, bMultiEdges=False)
```

Ribbon: <menuselection>MidPlaneEdit &#187; Face &#187; EdgesToEdges</menuselection>

## Inputs

### `crlEdges`

- A _List of Cursor_ specifying the edge.
- This is a required input.

### `bImprint`

- A _Boolean_ specifying the imprint.
- The default value is False.

### `bMultiEdges`

- A _Boolean_ specifying the multi edges.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.Face.EdgesToEdges(crlEdges, bImprint=False, bMultiEdges=False)
```
