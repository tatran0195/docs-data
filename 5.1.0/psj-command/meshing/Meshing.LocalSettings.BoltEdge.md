---
id: Meshing-LocalSettings-BoltEdge
title: Meshing.LocalSettings.BoltEdge()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set the mesh setting for bolt edges (Define the settings before surface mesh creation)
---

## Description

Set the mesh setting for bolt edges (Define the settings before surface mesh creation)

## Syntax

```psj
Meshing.LocalSettings.BoltEdge(...)
```

Macro: 

Ribbon: <menuselection>Meshing &#187; LocalSettings &#187; BoltEdge</menuselection>

## Inputs

### `iCircleDivision`

- An _Integer_ specifying number of division in circumferential direction.
- The default value is 0.

### `crlTargets`

- A _List of Cursor_ specifying  the target Edges of the local mesh setting.
- The default value is [].

## Return Code

A _Cursor_ specifying the created local mesh setting if success, or None if fail.


## Sample Code

```psj {2}
Geometry.Part.Cylinder()
Meshing.LocalSettings.BoltEdge(iCircleDivision=8, crlTargets=[Edge(2, 1)])
```
