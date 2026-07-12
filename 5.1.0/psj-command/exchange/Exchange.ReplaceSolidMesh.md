---
id: Exchange-ReplaceSolidMesh
title: Exchange.ReplaceSolidMesh()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Replace an adjacent solid part.
---

## Description

Replace an adjacent solid part.

## Syntax

```psj
Exchange.ReplaceSolidMesh(...)
```

Macro: 

Ribbon: <menuselection>Exchange &#187; ReplaceSolidMesh</menuselection>

## Inputs

### `crlSourceFace`

- A _List of Cursor_ specifying source face (base model side).
- This is a required input.

### `crlTargetFace`

- A _List of Cursor_ specifying target face (echange part side).
- This is a required input.

### `dTolerance`

- A _Double_ specifying tolerance between source face and target face.
- This is a required input.

## Return Code

A _Boolean_ specifying the function successfully executed or not.

## Sample Code

```psj {19-22}
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(
    dlOrigin=[0.01, 0.0, 0.0],
    ilAxialNodes=[4, 4, 4],
    strName="Cube_3",
    iPartColor=12867524)

Meshing.SolidMeshing(crlParts=[Part(1,2)],
    bTet10=True,
    dGradingFactor=1.05,
    dStretchLimit=0.1,
    iSpeedVsQual=1,
    iRegion=1,
    bSafeMode=False,
    iParallel=16,
    bInternalMeshOnly=False,
    iPartColor=65280)

ret=Exchange.ReplaceSolidMesh(
    crlSourceFace=[Face(24)],
    crlTargetFace=[Face(49)],
    dTolerance=0.0005)
print(ret)
```
