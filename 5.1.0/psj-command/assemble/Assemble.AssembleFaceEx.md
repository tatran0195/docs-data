---
id: Assemble-AssembleFaceEx
title: Assemble.AssembleFaceEx()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Make assemble faces (shared faces). User inputs the pair faces output from Assemble.FindMatingFaceEx() function, then it will return a list of new shared faces ID created.
---

## Description

Make assemble faces (shared faces).
User inputs the pair faces output from [Assemble.FindMatingFaceEx()](Assemble.FindMatingFaceEx) function, then it will return a list of new shared faces ID created.

## Syntax

```psj
Assemble.AssembleFaceEx(...)
```

Ribbon: <menuselection>Assemble &#187; Assemble Faces</menuselection>

## Inputs

### `ilPairFaceToMakeShareFace`

- A _List of Integer_ specifying the pair faces to make share face.
- This is a required input.

### `dTolerance`

- A _Double_ specifying the tolerance value.
- The default value is 0.1.

### `iTypeConnectPos`

- An _Integer_ specifying the type of connect position.
- The default value is 1.

### `bFitEdge`

- A _Boolean_ specifying the fit edge option.
- The default value is _False_.

## Return Code

A list of new shared faces ID created.

## Sample Code

```psj {9,10,11,12}
cube1 = Geometry.Part.Cube()
cube2 = Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0], 
                           strName="Cube_2", 
                           iPartColor=6409934)

pair_faces = Assemble.FindMatingFaceEx(crlTaBodies=[cube1, cube2], 
                                       dMatingTol=0.001)

share_faces = Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace = pair_faces, 
                                      dTolerance=0.001,
                                      iTypeConnectPos=0, 
                                      bFitEdge=True)

JPT.Debugger(share_faces)
```
