---
id: Geometry-Transform-ThreePoints
title: Geometry.Transform.ThreePoints()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Move the parts by selecting three pairs of nodes. The selected parts are moved onto the target position in a one-to-one correspondence between source and target
---

## Description

Move the parts by selecting three pairs of nodes. The selected parts are moved onto the target position in a one-to-one correspondence between source and target.

## Syntax

```psj
Geometry.Transform.ThreePoints(...)
```

Ribbon: <menuselection>Geometry &#187; Transform &#187; ThreePoints</menuselection>

## Inputs

### `crlTargetParts`

- A _List of Cursor_ specifying the parts to be transformed.
- This is a required input.

### `poslOriginalPoints`

- A _List of Vector_ specifying the original points using for movement.
  Three points are required corresponding to three original points.
- This is a required input.

### `poslNextPoints`

- A _List of Vector_ specifying the next points using for movement. Three points are required corresponding to three next points, respectively to the three original pointed defined in [`poslOriginalPoints`](#posloriginalpoints).
- This is a required input.

### `bCreateNewPart`

- A _Boolean_ specifying whether to copy the transformed parts to new parts.
  - If _True_, a new part is copied to new location.
  - If _False_, the original part is moved to new location.
- The default value is _False_.

### `bCopyLBC`

- A _Boolean_ specifying whether to copy load boundary conditions from the existing parts to new parts. This argument will only affect the functionality when _`bCreateNewPart`_=_True_.
- The default value is _False_.

### `bCopyProperty`

- A _Boolean_ selecting whether to copy property from the existing part to new parts. This argument will only affect the functionality when _`bCreateNewPart`_=_True_.
- The default value is _False_.

### `bCopyReference`

- A _Boolean_ selecting whether to copy reference from the existing part to new parts. This argument will only affect the functionality when _`bCreateNewPart`_=_True_.
- The default value is _False_.

## Return Code

A _List of Cursor_ specifying the created parts.

## Sample Code

```psj {6,7,8,9,10,11,12,13,14,15,16}
target_part = Geometry.Part.Cube()
move_part = Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], 
                               strName="Cube_2", 
                               iPartColor=6409934)

created_parts = Geometry.Transform.ThreePoints(crlTargetParts=[move_part],
                                               poslOriginalPoints=[[0.022, 0, 0.01], 
                                                                   [0.022, 0.01, 0.01], 
                                                                   [0.012, 0, 0.01]],
                                               poslNextPoints=[[0.01, 0, 0.01], 
                                                               [0, 0, 0.01], 
                                                               [0, 0.01, 0.01]],
                                               bCreateNewPart=True, 
                                               bCopyLBC=True, 
                                               bCopyProperty=True,
                                               bCopyReference=True)

JPT.Debugger(created_parts)
```
