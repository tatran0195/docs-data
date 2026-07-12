---
id: MeshEdit-Deform
title: MeshEdit.Deform()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Deform mesh by specifying source and destination face pairs.
---

## Description

Deform mesh by specifying source and destination face pairs.

## Syntax

```psj
MeshEdit.Deform(...)
```

Macro: [GeometryDeform](../../macro/mesh-edit/GeometryDeform)

Ribbon: <menuselection>MeshEdit &#187; Deform</menuselection>

## Inputs

### `crlFaceSrcObverse`

- A _List of Cursor_ specifying the source faces (obverse).
- The default value is [].

### `crlFaceDstReverse`

- A _List of Cursor_ specifying the destination faces (reverse).
- The default value is [].

### `crlFaceSrcReverse`

- A _List of Cursor_ specifying the source faces (reverse).
- The default value is [].

### `crlFaceDstObverse`

- A _List of Cursor_ specifying the destination faces (obverse).
- The default value is [].

### `crlFaceFixed`

- A _List of Cursor_ specifying the fixed faces.
- The default value is [].

### `dDistEffect`

- A _Double_ specifying the deformation influence distance.
- The default value is 0.02.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj
# Prepare model and view
Geometry.Part.Cube(
  dlLength=[0.01, 0.01, 0.001],
  ilAxialNodes=[10, 10, 3],
  iPartColor=7463537
)
Geometry.Part.Cube(
  dlOrigin=[0.0, 0.0, 0.002],
  strName="Cube_2",
  iPartColor=7961077
)
JPT.ViewFitToModel()
JPT.Exec('ViewShowMesh(1)')

# Deform mesh
MeshEdit.Deform(
  crlFaceSrcObverse=[Face(26)],
  crlFaceDstObverse=[Face(51)],
  crlFaceFixed=[Face(25)]
)
```
