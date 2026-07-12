---
id: Meshing-LocalSetting-SearchTargetFaces
title: Meshing.LocalSetting.SearchTargetFaces()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Search Target Faces for Local mesh setting
---

## Description

Search Target Faces for Local mesh setting

## Syntax

```psj
Meshing.LocalSetting.SearchTargetFaces(iPartType=0, dlOrigin=[0, 0, 0], dlLength=[0.1, 0.1, 0.1],
    dlCenterPt=[0.0,0.0,0.0], dlAxisPt1=[0.0,0.0,0.1], dlAxisPt2=[0.0,0.0,0.0], bEnclosed=False)
```

Macro: [SearchTargetFacesInModel](../../macro/meshing/SearchTargetFacesInModel)

Ribbon: <menuselection>Meshing &#187; LocalSetting &#187; SearchTargetFaces</menuselection>

## Inputs

### `iPartType`

- An _Integer_ specifying the part type.
- The default value is 0.

### `dlOrigin`

- A _Double List_ specifying the original.
- The default value is [0, 0, 0].

### `dlLength`

- A _Double List_ specifying the length.
- The default value is [0.1, 0.1, 0.1].

### `dlCenterPt`

- A _Double List_ specifying the center point.
- The default value is [0.0,0.0,0.0].

### `dlAxisPt1`

- A _Double List_ specifying the axis point 1.
- The default value is [0.0,0.0,0.1].

### `dlAxisPt2`

- A _Double List_ specifying the axis point 2.
- The default value is [0.0,0.0,0.0].

### `bEnclosed`

- A _Boolean_ specifying the enclosed.
- The default value is _False_.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Meshing.LocalSetting.SearchTargetFaces(iPartType=0, dlOrigin=[0, 0, 0], dlLength=[0.1, 0.1, 0.1],
    dlCenterPt=[0.0,0.0,0.0], dlAxisPt1=[0.0,0.0,0.1], dlAxisPt2=[0.0,0.0,0.0], bEnclosed=False)
```
