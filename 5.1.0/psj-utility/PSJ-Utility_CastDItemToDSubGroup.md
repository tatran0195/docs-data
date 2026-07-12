---
id: JPT-CastDItemToDSubGroup
title: JPT.CastDItemToDSubGroup()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Convert DItem object to DSubGroup object
---

## Description

Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DSubGroup](../data-type/psj-utility/pre-utility/built-in-types/DSubGroup)_ object to get the information of the selected group.

## Syntax

```psj
JPT.CastDItemToDSubGroup(DItemObject)
```

## Inputs

### `DItemObject`

- A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.
- This is a required input.

## Return Code

A _[DSubGroup](../data-type/psj-utility/pre-utility/built-in-types/DSubGroup)_ object (SubGroup with relating information).

## Sample Code

```psj {24}
# Prepare model
Geometry.Part.Cube(iPartColor=7697908)

Geometry.Part.Cube(
    dlOrigin=[0.01, 0.0, 0.0], 
    strName="Cube_2", 
    iPartColor=14903267)

mating_faces=Assemble.FindMatingFaceEx(
    crlTaBodies=[Part(1, 2)], 
    dMatingTol=0.000222222)

Assemble.AssembleFaceEx(
    ilPairFaceToMakeShareFace=mating_faces, 
    dTolerance=0.000222222, 
    iTypeConnectPos=0)

# Get Sub Group object as DItem object from the created list of DItem objects
listDItemSubGroups = JPT.GetAllByTypeID(JPT.DItemType.SUP_GROUP)
dItemSubGroup = listDItemSubGroups[0]
JPT.Debugger(dItemSubGroup)

# Convert from the above DItem object to DGroup object
dSubGroup = JPT.CastDItemToDSubGroup(dItemSubGroup)
JPT.Debugger(dSubGroup)
```
