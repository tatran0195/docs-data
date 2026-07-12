---
id: JPT-GetElemsByKind
title: JPT.GetElemsByKind()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get a list of element by inputting their kind (1D, 2D, 3D, etc.)
---

## Description

Get a _List of Elements_ by inputting their kind (1D, 2D, 3D, etc.).

## Syntax

```psj
JPT.GetElemsByKind(ElemKind)
```

## Inputs

### `ElemKind`

- An _Enum_ specifying the _[ElemKind](../data-type/psj-command/element-types)_ of elements in Jupiter.
- This is a required input.

## Return Code

An _[ElemVector](../data-type/psj-utility/pre-utility/built-in-types/ElemVector)_ object or _List of [DElem](../data-type/psj-utility/pre-utility/built-in-types/DElem)_ objects containing all the information of the related elements having the element kind is the same as the inputted element kind.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the information of all existing 2D elements
list2DElems = JPT.GetElemsByKind(JPT.ElemKind.ELEMKIND_2D)
JPT.Debugger(list2DElems)

# Print all the related information of each existing 2D element in list
for elem in list2DElems:
    JPT.Debugger(elem)
```
