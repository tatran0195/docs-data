---
id: HexModeling-BallHexa
title: HexModeling.BallHexa()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: hexa modeling ball hexa
---

## Description

Hexa modeling ball hexa

## Syntax

```psj
HexModeling.BallHexa(...)
```

Ribbon: <menuselection>HexModeling &#187; BallHexa</menuselection>

## Inputs

### `crPart`

- A _Cursor_ specifying the part.
- This is a required input.

### `vecCenter`

- A _Vector_ specifying the center.
- The default value is [0.0,0.0,0.0].

### `dRadius`

- A _Double_ specifying the radius.
- The default value is 5.0.

### `dMeshSize`

- A _Double_ specifying the mesh size.
- The default value is 0.5.

### `iType`

- An _Integer_ specifying the type.
- The default value is 0.

### `iLayer`

- An _Integer_ specifying the layer.
- The default value is 3.

### `bMakeCenterNode`

- A _Boolean_ specifying the make center node.
- The default value is _True_.

### `strName`

- A _String_ specifying the part name.
- The default value is "HexBall_1".

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {1-2}
HexModeling.BallHexa(crPart=None, vecCenter=[0.0,0.0,0.0], dRadius=5.0, dMeshSize=0.5, iType=0, 
    iLayer=3, bMakeCenterNode=True, strPartName="HexBall_1")
```
