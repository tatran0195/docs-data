---
id: JPT-CastDItemToDLoadBC
title: JPT.CastDItemToDLoadBC()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Convert DItem object to DLoadBC object to get the information of the selected coordinate system
---

## Description

Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DLoadBC](../data-type/psj-utility/pre-utility/built-in-types/DLoadBC)_ object to get the information of the selected coordinate system.

## Syntax

```psj
JPT.CastDItemToDLoadBC(DItemObject)
```

## Inputs

### `DItemObject`

- A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.
- This is a required input.

## Return Code

A _[DLoadBC](../data-type/psj-utility/pre-utility/built-in-types/DLoadBC)_ object (Boundary condition with relating information).

## Sample Code

```psj {12}
# Prepare simple sample
Geometry.Part.Cube(iPartColor=6409934)
BoundaryConditions.Pressure.General(crlTargets=[Face(26)])
JPT.ViewFitToModel()

# Get LBC object (Pressure) as DItem object from the created list of DItem objects
listDItemLoadBCs = JPT.GetAllByTypeID(JPT.DItemType.LBC_G_PRESSURE)
dItemLoadBC = listDItemLoadBCs[0]
JPT.Debugger(dItemLoadBC)

# Convert from the above DItem object to DLoadBC object
dLoadBC = JPT.CastDItemToDLoadBC(dItemLoadBC)
JPT.Debugger(dLoadBC)
```
