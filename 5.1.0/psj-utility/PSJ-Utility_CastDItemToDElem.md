---
id: JPT-CastDItemToDElem
title: JPT.CastDItemToDElem()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Convert DItem object to DElem object
---

## Description

Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DElem](../data-type/psj-utility/pre-utility/built-in-types/DElem)_ object to get the information of the selected element.

## Syntax

```psj
JPT.CastDItemToDElem(DItemObject)
```

## Inputs

### `DItemObject`

- A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.
- This is a required input.

## Return Code

A _[DElem](../data-type/psj-utility/pre-utility/built-in-types/DElem)_ object (Element with relating information).

## Sample Code

```psj {11}
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get Element object as DItem object from the created list of DItem objects
listDItemElems = JPT.GetAllByTypeID(JPT.DItemType.ELEM)
dItemElem = listDItemElems[0]
JPT.Debugger(dItemElem)

# Convert from the above DItem object to DElem object
dElem = JPT.CastDItemToDElem(dItemElem)
JPT.Debugger(dElem)
```
