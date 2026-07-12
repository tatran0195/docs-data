---
id: JPT-GetEntitiesByAdjacent
title: JPT.GetEntitiesByAdjacent()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get list of objects by adjacency based on the stop angle
---

## Description

Get _List of Objects_ by adjacency based on the stop angle.

## Syntax

```psj
JPT.GetEntitiesByAdjacent(DItemType, entityID, angleValue)
```

## Inputs

### `DItemType`

- An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.
- This is a required input.

### `entityID`

- An _Integer_ specifying the ID of the starting entity.
- This is a required input.

### `angleValue`

- An _Integer_ specifying the stop angle between entities for searching.
- This is a required input.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of found entities.

## Sample Code

```psj {6}
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get the faces relating to the face with ID = 26 based on angle = 30
adjacentFaces = JPT.GetEntitiesByAdjacent(JPT.DItemType.FACE, 26, 30)
JPT.Debugger(adjacentFaces)
```
