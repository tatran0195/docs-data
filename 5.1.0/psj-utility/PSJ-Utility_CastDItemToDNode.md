---
id: JPT-CastDItemToDNode
title: JPT.CastDItemToDNode()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Convert DItem object to DNode object
---

## Description

Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DNode](../data-type/psj-utility/pre-utility/built-in-types/DNode)_ object to get the information of the selected node.

## Syntax

```psj
JPT.CastDItemToDNode(DItemObject)
```

## Inputs

### `DItemObject`

- A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.
- This is a required input.

## Return Code

A _[DNode](../data-type/psj-utility/pre-utility/built-in-types/DNode)_ object (Node with relating information).

## Sample Code

```psj {11}
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get LBC object (Pressure) as DItem object from the created list of DItem objects
listDItemNodes = JPT.GetAllByTypeID(JPT.DItemType.NODE)
dItemNode = listDItemNodes[0]
JPT.Debugger(dItemNode)

# Convert from the above DItem object to DNode object
dNode = JPT.CastDItemToDNode(dItemNode)
JPT.Debugger(dNode)
```
