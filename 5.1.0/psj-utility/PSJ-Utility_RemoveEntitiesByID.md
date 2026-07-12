---
id: JPT-RemoveEntitiesByID
title: JPT.RemoveEntitiesByID()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Delete specified entity by inputting its type and its ID
---

## Description

Remove specified entity by inputting its DItem type and its ID.

## Syntax

```psj
JPT.RemoveEntitiesByID(DItemType, itemID)
```

## Inputs

### `DItemType`

- An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.
- This is a required input.

### `itemID`

- An _Integer_ specifying the ID of the target entity to be removed.
- This is a required input.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube(iPartColor=12829526)
Geometry.Part.Cube(strName="Cube_2", iPartColor=8060538)
Geometry.Part.Cube(strName="Cube_3", iPartColor=13787489)
JPT.ViewFitToModel()

# Delete Cube_2 part
JPT.RemoveEntitiesByID(JPT.DItemType.BODY, 2)
```
