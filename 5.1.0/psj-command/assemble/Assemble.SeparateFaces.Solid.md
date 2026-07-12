---
id: Assemble-SeparateFaces-Solid
title: Assemble.SeparateFaces.Solid()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Separate a shared face between parts into distinct faces
---

## Description

Separate a shared face between parts into distinct faces.

## Syntax

```psj
Assemble.SeparateFaces.Solid(...)
```

Ribbon: <menuselection>Assemble &#187; Separate Faces &#187; Solid</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the target parts which have shared faces between them.
- The default value is [].

### `crlFaces`

- A _List of Cursor_ specifying the target shared faces.
- The default value is [].

### `iCreateGroup`

- A _Boolean_ specifying the type of group will be created.
- The default value is 0.

## Return Code

A _List Cursor_ of separated faces if success, or _None_ if fail.

## Sample Code

```psj {9,10}
Geometry.Part.Cube(iPartColor=15658599)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=7961077)
Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace=[49, 24], 
                        dTolerance=0.001, 
                        iTypeConnectPos=0)

faces = Assemble.SeparateFaces.Solid(crlParts=[Part(1, 2)], 
                                     iCreateGroup=2)
JPT.Debugger(faces)
```
