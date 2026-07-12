---
id: MeshCleanup-Element-SurfaceElement
title: MeshCleanup.Element.SurfaceElement()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Change Topology Element
---

## Description

Change Topology Element

## Syntax

```psj
MeshCleanup.Element.SurfaceElement(ilElement=[], ilFace=[], ilPart=[], iCreateNewPart=0)
```

Ribbon: <menuselection>MeshCleanup &#187; Element &#187; SurfaceElement</menuselection>

## Inputs

### `ilElement`

- A _List of Integer_ specifying the element.
- The default value is [].

### `ilFace`

- A _List of Integer_ specifying the face.
- The default value is [].

### `ilPart`

- A _List of Integer_ specifying the part.
- The default value is [].

### `iCreateNewPart`

- An _Integer_ specifying the create new part.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Element.SurfaceElement(ilElement=[], ilFace=[], ilPart=[], iCreateNewPart=0)
```
