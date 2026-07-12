---
id: Exchange-AssembleSolidMesh
title: Exchange.AssembleSolidMesh()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Assemble solid mesh parts
---

## Description

Assemble solid mesh parts.

## Syntax

```psj
Exchange.AssembleSolidMesh(...)
```

Macro: 

Ribbon: <menuselection>Exchange &#187; AssembleSolidMesh</menuselection>

## Inputs

### `crNewPart`

- A _Cursor_ specifying the new assembly part.
- The default value is _None_.

### `crlAssembleParts`

- A _List of Cursor_ specifying the original assembly part.
- The default value is [].

### `crlNewFaces`

- A _List of Cursor_ specifying the face to be shared on the new assembly part.
- The default value is [].

### `crlAssembleFaces`

- A _List of Cursor_ specifying the face to be shared on the original assembly part.
- The default value is [].

### `dTolerance`

- A _Double_ specifying the tolerance value.
- The default value is 0.0.

### `iConnectPosition`

- An _Integer_ specifying the position to create the shared face.
  - 0: Mid
  - 1: Mater
- The default value is 0.

### `iRemeshLayer`

- An _Integer_ specifying the number of layers to be remeshed around the new shared face.
- The default value is 2.

### `bRemeshAuto`

- A _Boolean_ specifying whether to set the mesh size automatically.
- The default value is _True_.

### `dAvg`

- A _Double_ specifying the average mesh size.
- The default value is 0.0.

### `dMin`

- A _Double_ specifying the minimum mesh size.
- The default value is 0.0.

### `dMax`

- A _Double_ specifying the maximum mesh size.
- The default value is 0.0.

## Return Code

A _Boolean_ specifying the function successfully executed or not.

## Sample Code

```psj {34,35}
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.0101, 0.0, 0.0], strName="Cube_2", iPartColor=14903267)
Meshing.AdjustCircleVertex(crlParts=[Part(2)], bInModeSurfaceMesh=True)
Meshing.SetMeshAttribute(
    crlParts=[Part(2)], 
    surfaceMesh=SURFACE_MESH(
        dAvgElemSize=0.0015,
         dGeomAngle=0.7853981634, 
         iPerformanceMode=1, 
         dAutoMergeTinyFacesAngle=0.5235987756, 
         bGeomApprox=True))
Meshing.SurfaceMeshing(
    crlParts=[Part(2)], 
    surfaceMesh=SURFACE_MESH(
        dAvgElemSize=0.0015, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bGeomApprox=True), 
    iThreadNum=16)
Meshing.SolidMeshing(
    rlParts=[Part(2, 1)], 
    dGradingFactor=1.05, 
    dStretchLimit=0.1, 
    iSpeedVsQual=1, 
    iRegion=1, 
    bSafeMode=False, 
    iParallel=16, 
    bInternalMeshOnly=False, 
    iPartColor=65280)

# Assemble solid mesh
ret = Exchange.AssembleSolidMesh(crNewPart=Part(2), crlAssembleParts=[Part(1)], dTolerance=0.0002, 
    iConnectPosition=1, bRemeshAuto=False, dAvg=0.0012, dMin=0.0001, dMax=0.002)
print(assemble_sretolid)
```
