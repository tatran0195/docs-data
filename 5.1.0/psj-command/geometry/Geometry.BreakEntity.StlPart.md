---
id: Geometry-BreakEntity-StlPart
title: Geometry.BreakEntity.StlPart()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Break STL part entity
---

## Description

This method separates the _STL_ parts into multiple bodies.

## Syntax

```psj
Geometry.BreakEntity.StlPart(crlParts, iMinNoOfFacet=0, iBreakMethod=0)
```

Ribbon: <menuselection>Geometry &#187; Break Entity &#187; STL Part</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying STL parts to be separated.
- This is a required input.

### `iMinNoOfFacet`

- An _Integer_ specifying the minimum number of facets to be considered as an entity.
- The default value is 0.

### `iBreakMethod`

- An _Integer_ specifying the break method.
- If _iBreakMethod=0_, separating using the Face based method.
- If _iBreakMethod=1_, separating using the Facet based method. This method separates on a facet basis, ignoring face configurations.
- The default value is 0.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()

Geometry.BreakEntity.StlPart(crlParts=[Part(1)], iMinNoOfFacet=0, iBreakMethod=0)
```
