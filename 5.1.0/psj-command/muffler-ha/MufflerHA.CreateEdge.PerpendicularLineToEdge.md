---
id: MufflerHA-CreateEdge-PerpendicularLineToEdge
title: MufflerHA.CreateEdge.PerpendicularLineToEdge()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Unknown Description
---

## Description

Unknown Description

## Syntax

```psj
MufflerHA.CreateEdge.PerpendicularLineToEdge(crNode, crEdge, crlFaces, bBreakFace)
```

Ribbon: <menuselection>MufflerHA &#187; CreateEdge &#187; PerpendicularLineToEdge</menuselection>

## Inputs

### `crNode`

- A _Cursor_ specifying the node.
- This is a required input.

### `crEdge`

- A _Cursor_ specifying the edge.
- This is a required input.

### `crlFaces`

- A _List of Cursor_ specifying the face.
- This is a required input.

### `bBreakFace`

- A _Boolean_ specifying the break face.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MufflerHA.CreateEdge.PerpendicularLineToEdge(crNode, crEdge, crlFaces, bBreakFace)
```
