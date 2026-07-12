---
id: Geometry-MergeEntities-TinyFacesMerge
title: Geometry.MergeEntities.TinyFacesMerge()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Merge tiny faces either by extending the user selection or using only the selected faces
---

## Description

Merge tiny faces either by extending the user selection or using only the selected faces.

## Syntax

```psj
Geometry.MergeEntities.TinyFacesMerge(...)
```

Macro: [GeometryMergeEntitiesTinyFacesMerge_K](../../macro/geometry/GeometryMergeEntitiesTinyFacesMerge_K)

Ribbon: <menuselection>Geometry &#187; Merge Entities &#187; Tiny Faces Merge</menuselection>

## Inputs

### `strMethod`

- A _String_ specifying the method use to merge. Possible values are _AUTO_, _SELECT_, _MERGE_, _RESTORE_.
- The default value is _AUTO_.

### `crlTargets`

- A _List of Cursor_ specifying the parts or faces to be merged.
- The default value is [].

### `dMinFaceWidth`

- A _Double_ specifying the minimum face width in meter. This argument is used when _strMethod_ has the value _AUTO_ or _SELECT_.
- The default value is 0.0.

### `dMaxFaceWidth`

- A _Double_ specifying the maximum face width in meter. This argument is used when _strMethod_ has the value _AUTO_ or _SELECT_.
- The default value is 0.001.

### `dFaceAngle`

- A _Double_ specifying the angle between faces in degree. This argument is used when _strMethod_ has the value _AUTO_ or _MERGE_.
- The default value is 30.

### `bReferLocalSetting`

- A _Boolean_ specifying whether to refer to the local setting or not.
- The default value is _False_.

### `bCreateRefPart`

- A _Boolean_ specifying whether or not create a reference part.
- The default value is _False_.

### `crlRefPart`

- A _List of Cursor_ specifying the reference parts.
- The default value is [].

### `crlRefEdge`

- A _List of Cursor_ specifying the reference edge.
- The default value is [].
## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- _True_: The function is executed successfully.
- _False_: The function cannot be executed.

## Sample Code

```psj {15,16}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube_2",
                   iPartColor=6409934)
Geometry.Edge.Angle([CursorPair(Node(945), Node(953))])
Geometry.Edge.Angle([CursorPair(Node(464), Node(472))])
Geometry.Edge.Angle([CursorPair(Node(79), Node(432))])
Geometry.Edge.Angle([CursorPair(Node(96), Node(487))])
Geometry.Edge.Angle([CursorPair(Node(470), Node(479))])
Geometry.Edge.Angle([CursorPair(Node(471), Node(479))])
Geometry.Edge.Angle([CursorPair(Node(946), Node(954))])
Geometry.Edge.Angle([CursorPair(Node(953), Node(954))])
Geometry.Edge.Angle([CursorPair(Node(961), Node(962))])
Geometry.Edge.Angle([CursorPair(Node(953), Node(962))])
merged_entities = Geometry.MergeEntities.TinyFacesMerge(crlTargets=[Part(1, 2)],
                                                        bCreateRefPart=True)
JPT.Debugger(merged_entities)
```
