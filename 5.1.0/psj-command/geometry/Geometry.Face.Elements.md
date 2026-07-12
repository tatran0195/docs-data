---
id: Geometry-Face-Elements
title: Geometry.Face.Elements()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create faces from the selected elements
---

## Description

Create faces from the selected elements.

## Syntax

```psj
Geometry.Face.Elements(...)
```

Macro: [CreateFaceByElem](../../macro/geometry/CreateFaceByElem)

Ribbon: <menuselection>Geometry &#187; Face &#187; Elements</menuselection>

## Inputs

### `crlElems`

- A _List of Cursor_ specifying the surface elements to be moved to the new surface.
- This is a required input.

### `bSharedFace`

- A _Boolean_ whether to create a shared face. If _bSharedFace=True_, the _crlElems_ argument must specify shared elements.
- The default value is _False_.

## Return Code

A _List of Cursor_ specifying the new created faces.

## Sample Code

```psj {3,4,5,6,7,8,9,10}
Geometry.Part.Cube()

created_face = Geometry.Face.Elements(crlElems=[Elem(1008,
                                                    1007,
                                                    989,
                                                    990,
                                                    1005,
                                                    1006,
                                                    988,
                                                    987)])

JPT.Debugger(created_face)
```
