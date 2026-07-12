---
id: HexModeling-BoxMesh
title: HexModeling.BoxMesh()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Box hex mesh creator for parts
---

## Description

Box hex mesh creator for parts

## Syntax

```psj
HexModeling.BoxMesh(...)
```

Ribbon: <menuselection>HexModeling &#187; BoxMesh</menuselection>

## Inputs

### `ilPartIds`

- A _List of Integer_ specifying the part ids.
- This is a required input.

### `dMeshSize`

- A _Double_ specifying the mesh size.
- This is a required input.

### `strMaterialName`

- A _String_ specifying the material name.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {2}
Geometry.Part.Cube()
HexModeling.BoxMesh(ilPartIds=[1], dMeshSize=0.002, strMaterialName="")
```
