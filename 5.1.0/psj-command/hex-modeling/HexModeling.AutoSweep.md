---
id: HexModeling-AutoSweep
title: HexModeling.AutoSweep()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Hex Modeling Auto Sweep
---

## Description

Hex Modeling Auto Sweep

## Syntax

```psj
HexModeling.AutoSweep(...)
```

Ribbon: <menuselection>HexModeling &#187; AutoSweep</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the part.
- The default value is [].

### `dMeshSize`

- A _Double_ specifying the mesh size.
- The default value is 0.0.

### `bLayers`

- A _Boolean_ specifying the layers.
- The default value is _False_.

### `iLayers`

- An _Integer_ specifying the layers.
- The default value is 2.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {1}
Geometry.Part.Cube()
HexModeling.AutoSweep(crlParts=[Part(1)], dMeshSize=0.002, iLayers=5)
```
