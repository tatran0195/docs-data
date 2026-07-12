---
id: Geometry-MakeFillet
title: Geometry.MakeFillet()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create face-face fillet
---

## Description

This method creates a smooth transition surface between two adjacent faces, which need to share at least one edge.

## Syntax

```psj
Geometry.MakeFillet(crlEdges, dRadius=1.0)
```

Ribbon: <menuselection>Geometry &#187; Make Fillet</menuselection>

## Inputs

### `crlEdges`

- A _List of Cursor_ specifying shared edges between adjacent faces.
- This is a required input.

### `dRadius`

- A _Double_ specifying the radius applied to the entire given edges.
- The default value is 1.0.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()

Geometry.MakeFillet(crlEdges=[Edge(17, 19)])
```
