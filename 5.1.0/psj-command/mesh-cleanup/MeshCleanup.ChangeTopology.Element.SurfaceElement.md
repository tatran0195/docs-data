---
id: MeshCleanup-ChangeTopology-Element-SurfaceElement
title: MeshCleanup.ChangeTopology.Element.SurfaceElement()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Assign the selected element to a different part.
---

## Description

Assign the selected element to a different part.

## Syntax

```psj
MeshCleanup.ChangeTopology.Element.SurfaceElement(ilElement, ilFace, ilPart, iCreateNewPart)
```

Ribbon: <menuselection>MeshCleanup &#187; ChangeTopology &#187; Element &#187; SurfaceElement</menuselection>

## Inputs

### `ilElement`

- A _List of Integer_ specifying the element.
- This is a required input.

### `ilFace`

- A _List of Integer_ specifying the face.
- This is a required input.

### `ilPart`

- A _List of Integer_ specifying the part.
- This is a required input.

### `iCreateNewPart`

- An _Integer_ specifying the create new part.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.ChangeTopology.Element.SurfaceElement(ilElement, ilFace, ilPart, iCreateNewPart)
```
