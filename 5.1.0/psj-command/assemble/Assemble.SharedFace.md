---
id: Assemble-SharedFace
title: Assemble.SharedFace()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create an assembled face/shared face group
---

## Description

Create an assembled face/shared face group.

## Syntax

```psj
Assemble.SharedFace(...)
```

Macro: [CreateSharedFace](../../macro/assemble/CreateSharedFace)

Ribbon: <menuselection>Assemble &#187; Shared Face</menuselection>

## Inputs

This function does not contains any input values.

## Return Code

A _List of Cursor_ specifying the created shared faces.

## Sample Code

```psj {21}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=15658599)
Geometry.Part.Cube(dlOrigin=[0.01, 0.01, 0.0], 
                   strName="Cube_3", 
                   iPartColor=14903267)

Assemble.FindMatingFaceEx(crlTaBodies=[Part(1, 
                                            2, 
                                            3)], 
                          dMatingTol=0.000222222)
Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace=[48, 
                                                   73, 
                                                   49, 
                                                   24], 
                        dTolerance=0.000222222, 
                        iTypeConnectPos=0, 
                        bFitEdge=True)

created_shared_faces = Assemble.SharedFace()

JPT.Debugger(created_shared_faces)
```
