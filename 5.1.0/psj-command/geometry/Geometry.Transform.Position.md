---
id: Geometry-Transform-Position
title: Geometry.Transform.Position()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Transform parts by changing their position
---

## Description

This method moves the parts by selecting three pairs of nodes. The given parts move onto a target position in a one-one correspondence between source and target.

## Syntax

```psj
Geometry.Transform.Position(crlParts, veclPoint=[[0.0, 0.0, 0.0]], bCreateNewPart=False, bCopyLBC=False,
    bCopyProperty=False)
```

Macro: [PositionBody](../../macro/geometry/PositionBody)

Ribbon: <menuselection>Geometry &#187; Transform &#187; Position</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the parts to be transformed.
- This is a required input.

### `veclPoint`

- A _List of Vector_ specifying the points using for movement. Six points are required corresponding to three pairs of nodes respectively. Each pair is in a one-one correspondence between target and source.
- The default value is [[0.0,0.0,0.0]].

### `bCreateNewPart`

- A _Boolean_ specifying whether to copy the transformed parts to new parts.
- The default value is _False_.

### `bCopyLBC`

- A _Boolean_ specifying whether to copy load boundary conditions from the existing part to new parts. This argument will only affect the functionality when _bCreateNewPart=True_.
- The default value is _False_.

### `bCopyProperty`

- A _Boolean_ selecting whether to copy property from the existing part to new parts. This argument will only affect the functionality when _bCreateNewPart=True_.
- The default value is _False_.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube(iPartColor=14540142)

Geometry.Part.Wedge(vecOrigin=[0.01, 0.01, 0.01], iPartColor=6678885)

Geometry.Transform.Position(crlParts=[Part(1)], veclPoint=[[0.0, 0.0, 10.0], [10.0, 0.0, 10.0],
    [0.0, 10.0, 10.0], [10.0, 10.0, 20.0], [20.0, 10.0, 20.0], [10.0, 20.0, 20.0]])
```
