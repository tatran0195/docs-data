---
id: Geometry-Edge-OffsetLine
title: Geometry.Edge.OffsetLine()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create new edges by offsetting specified edges
---

## Description

Create new edges by offsetting specified edges.

## Syntax

```psj
Geometry.Edge.OffsetLine(...)
```

Macro: [ImprintOffsetLineS](../../macro/geometry/ImprintOffsetLineS)

Ribbon: <menuselection>Geometry &#187; Edge &#187; Offset Line</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the target faces on which the edges are imprinted.
- This is a required input.

### `crlEdges`

- A _List of Cursor_ specifying the edges to be offset.
- This is a required input.

### `bBreakFace`

- A _Boolean_ specifying whether to break the given faces where possible.
- The default value is _True_.

### `dOffsetDistance`

- A _Double_ specifying the offset distance.
- The default value is 0.0.

### `iLayerNumber`

- An _Integer_ specifying the number of layers to be offset.
- The default value is 1.

### `bMerge`

- A _Boolean_ specifying whether or not to merge the offset edges when the angle between them is bigger than 150 degrees.
- The default value is _True_.

### `bExtend`

- A _Boolean_ specifying whether to extend the offset edges to the nearest boundary edges.
- The default value is _True_.

### `iOffsetMethod`

- An _Integer_ specifying how to create offset edges.
  - If _iOffsetMethod=0_, create multiple offset layers using the offset distance and the number of layers.
  - If _iOffsetMethod=1_, create single offset layer using the layer offset distance.
- The default value is 0.

### `dOffsetDistance`

- A _List of Double_ specifying the layer offset distance.
- The default value is [].

### `iImprintMethod`

- An _Integer_ specifying imprint method.
  - If _iImprintMethod=0_, offset edges will be imprinted onto the face side that has the longest edges.
  - If _iImprintMethod=1_, offset edges will be imprinted onto the face side that has the shortest edges.
  - If _iImprintMethod=2_, offset edges will be imprinted onto both face sides.
- The default value is 2.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5,6}
Geometry.Part.Cube(iPartColor=6484066)

offset_lines = Geometry.Edge.OffsetLine(crlFaces=[Face(22)], 
                                        crlEdges=[Edge(19)], 
                                        dOffsetDistance=0.001, 
                                        iLayerNumber=6)

JPT.Debugger(offset_lines)
```
