---
id: MeshEdit-SurfaceMesh
title: MeshEdit.SurfaceMesh()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Command for converting solid mesh of specified parts to surface mesh.
---

## Description

Command for converting solid mesh of specified parts to surface mesh.

## Syntax

```psj
MeshEdit.SurfaceMesh(...)
```

Ribbon: <menuselection>MeshEdit &#187; SurfaceMesh</menuselection>

Macro: [ElementConv_Surface](../../macro/mesh-edit/ElementConv_Surface)

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the target parts.
- The default value is [].

### `iType`

- An _Integer_ specifying the surface element conversion type.
  - 0: To Linear (Tri3/Quad4)
  - 1: To Quadratic (Tri6/Quad8)
  - 2: Tri3
  - 7: Split (Tri6to4Tri3s/Quad8to4Quad4s)
- The default value is 1.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj
# Prepare model and view
Geometry.Part.Cube(iPartColor=6409934)
Meshing.AdjustCircleVertex(
  crlParts=[Part(1)],
  bInModeSurfaceMesh=True
)
Meshing.SetMeshAttribute(
  crlParts=[Part(1)],
  surfaceMesh=SURFACE_MESH(
    dAvgElemSize=0.003,
    dGeomAngle=0.7853981634,
    iPerformanceMode=1,
    dAutoMergeTinyFacesAngle=0.5235987756,
    bOutputQuadMesh=True,
    bGeomApprox=True
  )
)
Meshing.SurfaceMeshing(
  crlParts=[Part(1)],
  surfaceMesh=SURFACE_MESH(
    dAvgElemSize=0.003,
    dGeomAngle=0.7853981634,
    iPerformanceMode=1,
    dAutoMergeTinyFacesAngle=0.5235987756,
    bOutputQuadMesh=True,
    bGeomApprox=True
  ),
  iThreadNum=16
)
JPT.ViewFitToModel()
JPT.Exec('ViewShowMesh(1)')

# Convert to Quad8
MeshEdit.SurfaceMesh(crlParts=[Part(1)])
```
