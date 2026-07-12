---
id: JPT-CastToDItem
title: JPT.CastToDItem()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Convert the selected object to DItem object
---

## Description

Convert the selected object to _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to get all the related information.

## Syntax

```psj
JPT.CastToDItem(Object)
```

## Inputs

### `Object`

- An _Object_ in Jupiter such as _[DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_, _[DFace](../data-type/psj-utility/pre-utility/built-in-types/DFace)_, _[DElem](../data-type/psj-utility/pre-utility/built-in-types/DElem)_, _[DEdge](../data-type/psj-utility/pre-utility/built-in-types/DEdge)_, _[DGroup](../data-type/psj-utility/pre-utility/built-in-types/DGroup)_, _[DNode](../data-type/psj-utility/pre-utility/built-in-types/DNode)_, etc.
- This is a required input.

## Return Code

A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object (Base object with all the information).

## Sample Code

```psj {11}
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get Part object as DBody object from the created list of DBody objects
listDBodyParts = JPT.GetAllParts()
dBodyPart = listDBodyParts[0]
JPT.Debugger(dBodyPart)

# Convert from the above DBody object to DItem object
dItemPart = JPT.CastToDItem(dBodyPart)
JPT.Debugger(dItemPart)
```
