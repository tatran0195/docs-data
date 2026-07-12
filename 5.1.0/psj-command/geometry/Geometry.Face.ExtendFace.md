---
id: Geometry-Face-ExtendFace
title: Geometry.Face.ExtendFace()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a face extended from an edge.
---

## Description

Create a face extended from an edge.

## Syntax

```psj
Geometry.Face.ExtendFace(...)
```

Macro: ExtendFace

Ribbon: <menuselection>Geometry &#187; Face &#187; ExtendFace</menuselection>

## Inputs

### `crEdge`

- A _Cursor_ specifying source edge.
- This is a required input.

### `crFace`

- A _Cursor_ specifying target face when Metric is set "Offset" or "Cylinder".
- The default value is _None_.

### `crRefFace`

- A _Cursor_ specifying reference face when Metric is set "Cylinder", Method is "To Face".
- The default value is _None_.

### `crFirstNode`

- A _Cursor_ specifying the first node to set axis by Metric "2Nodes". 
- The default value is _None_.

### `crSecondNode`

- A _Cursor_ specifying the second node to set axis by Metric "2Nodes".
- The default value is _None_.

### `crElemEdge`

- A _CursorPair_ specifying element edge to set axis by Metric "Element Edge".
- The default value is [].

### `extendFaceDirection`

- A _Class of [EXTEND_FACE_DIRECTION](../../data-type/psj-command/parameter-types/EXTEND_FACE_DIRECTION)_ specifying the direction settings for the extended face in 3D dimension.
- The default value is [EXTEND_FACE_DIRECTION](../../data-type/psj-command/parameter-types/EXTEND_FACE_DIRECTION).

### `extendFaceMesh`

- A _Class of [EXTEND_FACE_MESH](../../data-type/psj-command/parameter-types/EXTEND_FACE_MESH)_ specifying the mesh settings for the extended face.
- The default value is [EXTEND_FACE_MESH](../../data-type/psj-command/parameter-types/EXTEND_FACE_MESH).
    
### `extendFaceOption`

- A _Class of [EXTEND_FACE_OPTION](../../data-type/psj-command/parameter-types/EXTEND_FACE_OPTION)_ specifying the geometric settings for the extended face.
- The default value is [EXTEND_FACE_OPTION](../../data-type/psj-command/parameter-types/EXTEND_FACE_OPTION).

## Return Code

A _Cursor_ specifying the new created face.

## Sample Code

```psj {2-7}
Geometry.Part.Cube()
created_face = Geometry.Face.ExtendFace(crEdge=Edge(19), 
                                      extendFaceDirection=EXTEND_FACE_DIRECTION(
                                          dComponentX=0, 
                                          dComponentZ=0), 
                                      extendFaceMesh=EXTEND_FACE_MESH(), 
                                      extendFaceOption=EXTEND_FACE_OPTION())
JPT.Debugger(created_face)
```
