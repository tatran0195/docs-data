---
id: Geometry-ShowAdjacent-Faces
title: Geometry.ShowAdjacent.Faces()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Expand the selection in all directions, regardless of the shape of surrounding features or the angle at which objects are joined. It obtained by recursively finding adjacent faces at an angle of less than or equal to the specified angle
---

## Description

Expand the selection in all directions, regardless of the shape of surrounding features or the angle at which objects are joined.
It obtained by recursively finding adjacent faces at an angle of less than or equal to the specified angle.

## Syntax

```psj
Geometry.ShowAdjacent.Faces(...)
```

Ribbon: <menuselection>Geometry &#187; Show Adjacent &#187; Faces</menuselection>

## Inputs

### `dAngle`

- A _Double_ specifying the angle between elements in degree. The adjacent faces that are at an angle of less than or equal to _dAngle_ will be selected.
- The default value is 0.0.

### `bIncludeStopFaces`

- A _Boolean_ specifying whether to add the stop faces to the selection list or not.
- The default value is _False_.

### `iNumOfLayers`

- An _Integer_ specifying the number of adjacent layers to be searched.
- The default value is 1.

### `crlStartFaces`

- A _List of Cursor_ specifying a sequence of start faces.
- The default value is [].

### `crlStopFaces`

- A _List of Cursor_ specifying a sequence of stop faces.
- The default value is [].

## Return Code

A _List of Cursor_ specifying a sequence of adjacent faces.

## Sample Code

```psj {2}
Geometry.Part.Cube()
adjacent_faces = Geometry.ShowAdjacent.Faces(dAngle=0, iNumOfLayers=100, crlStartFaces=[Face(26)])
JPT.Debugger(adjacent_faces)
```
