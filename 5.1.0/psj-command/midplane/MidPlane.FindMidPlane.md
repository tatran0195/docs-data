---
id: MidPlane-FindMidPlane
title: MidPlane.FindMidPlane()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create mid-planes for the specified parts.
---

## Description

Create mid-planes for the specified parts.

## Syntax

```psj
MidPlane.FindMidPlane(...)
```

Macro: FindMidPlane

Ribbon: <menuselection>MidPlane &#187; FindMidPlane</menuselection>

## Inputs

### `crlTargetParts`

- A _List of Cursor_ specifying parts.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {6}
Geometry.Part.Cube(dlLength=[0.001, 0.01, 0.01])
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0],
                    dlLength=[0.002, 0.01, 0.01],
                    strName="Cube_2",
                    iPartColor=6409934)
MidPlane.FindMidPlane(crlTargetParts=[Part(1, 2)])
```
