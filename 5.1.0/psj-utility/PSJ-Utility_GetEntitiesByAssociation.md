---
id: JPT-GetEntitiesByAssociation
title: JPT.GetEntitiesByAssociation()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get list of objects by associating from the inputted entity ID and its type
---

## Description

Get _List of Objects_ by associating from the inputted entity ID and its type.

## Syntax

```psj
JPT.GetEntitiesByAssociation(DItemType, AssociateType, entityID)
```

## Inputs

### `DItemType`

- An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.
- This is a required input.

### `AssociateType`

- An _Enum_ specifying the _[AssociateType](../data-type/psj-utility/pre-utility/enumeration-types/associate-types)_ describing the association type in Jupiter.
- This is a required input.

### `entityID`

- An _Integer_ specifying the ID of which is used as a starting entity.
- This is a required input.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of associated entities.

## Sample Code

```psj {6}
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get all the associating faces existing on the part with ID = 1
listAssociatedEntities = JPT.GetEntitiesByAssociation(JPT.DItemType.BODY, JPT.AssociateType.AS_FACE, 1)
JPT.Debugger(listAssociatedEntities) # return value is a list DItem has size = 6
```
