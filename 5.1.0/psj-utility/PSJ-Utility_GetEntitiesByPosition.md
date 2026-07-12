---
id: JPT-GetEntitiesByPosition
title: JPT.GetEntitiesByPosition()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get the entity satisfying the given conditions (X, Y, Z)
---

## Description

Get the entity satisfying the given conditions (X, Y, Z).

## Syntax

```psj
JPT.GetEntitiesByPosition(AssociateType, xCoordValue, yCoordValue, zCoordValue)
```

## Inputs

### `AssociateType`

- An _Enum_ specifying the _[AssociateType](../data-type/psj-utility/pre-utility/enumeration-types/associate-types)_ describing the association type in Jupiter.
- This is a required input.

### `xCoordValue`

- A _Double_ specifying the value in X coordinate in millimeters [mm] in the Cartesian coordinate system..
- This is a required input.

### `yCoordValue`

- A _Double_ specifying the value in Y coordinate in millimeters [mm] in the Cartesian coordinate system..
- This is a required input.

### `zCoordValue`

- A _Double_ specifying the value in Z coordinate in millimeters [mm] in the Cartesian coordinate system..
- This is a required input.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing the information of the satisfied entity.

Note that to get the satisfied entity, please get the second element of the created _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_.

## Sample Code

```psj {6}
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get the information of the created cube
selPart = JPT.GetEntitiesByPosition(JPT.AssociateType.AS_BODY, 10, 10, 10)
JPT.Debugger(selPart[0]) # second element of the created list
```
