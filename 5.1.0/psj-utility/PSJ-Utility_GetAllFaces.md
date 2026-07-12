---
id: JPT-GetAllFaces
title: JPT.GetAllFaces()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get all the information of all existing faces
---

## Description

Get all the information of all existing faces.

## Syntax

```psj
JPT.GetAllFaces()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[FaceVector](../data-type/psj-utility/pre-utility/built-in-types/FaceVector)_ object or _List of [DFace](../data-type/psj-utility/pre-utility/built-in-types/DFace)_ objects containing all the information of all the existing faces.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the information of all existing faces
listDFaces = JPT.GetAllFaces()
JPT.Debugger(listDFaces)

# Print all the related information of each existing face in list
for face in listDFaces:
    JPT.Debugger(face)
```
