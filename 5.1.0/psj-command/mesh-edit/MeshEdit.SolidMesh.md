---
id: MeshEdit-SolidMesh
title: MeshEdit.SolidMesh()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Command for converting surface mesh of specified parts to solid mesh.
---

## Description

Command for converting surface mesh of specified parts to solid mesh.

## Syntax

```psj
MeshEdit.SolidMesh(...)
```

Ribbon: <menuselection>MeshEdit &#187; SolidMesh</menuselection>

Macro: [ElementConv_Solid](../../macro/mesh-edit/ElementConv_Solid)

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the target parts.
- The default value is [].

### `iType`

- An _Integer_ specifying the solid element conversion type.
  - 0: To Linear (Tet4/Penta5/Hex8/Pyramid5)
  - 1: To Quadratic (Tet10/Penta15/Hex20/Pyramid13)
  - 2: Hexa to Penta5
  - 3: Hexa/Penta to Tet4
- The default value is 1.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj
# Prepare model and view
HexModeling.BallHexa(crPart=None, dRadius=0.005, dMeshSize=0.001, strPartName="HexBall_1")
JPT.ViewFitToModel()
JPT.Exec('ViewShowMesh(1)')

# Convert to Tet4
MeshEdit.SolidMesh(crlParts=[Part(1)], iType=3)
```
