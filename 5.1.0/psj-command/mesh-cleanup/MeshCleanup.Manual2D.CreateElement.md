---
id: MeshCleanup-Manual2D-CreateElement
title: MeshCleanup.Manual2D.CreateElement()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a Tri/Quad element 
---

## Description

Create a Tri/Quad element.

## Syntax

```psj
MeshCleanup.Manual2D.CreateElement()
```

Ribbon: <menuselection>MeshCleanup &#187; Manual2D &#187; CreateElement</menuselection>

## Inputs

### `iElemType`

- An _Integer_ specifying the element type.
  - 0: Tri element
  - 1: Quad element
- The default value is 0.

### `crParentEntity`

- A _Cursor_ specifying the face to which the created element will belong.
- The default value is None.

### `crlNodes`

- A _List of Cursor_ specifying the node.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {3-4}
Geometry.Part.Cube(iPartColor=6409934)
MeshCleanup.Manual2D.DeleteElement(crlElems=[Elem(1028)])
element = MeshCleanup.Manual2D.CreateElement(crParentEntity=Face(26), 
                                            crlNodes=[Node(470, 469, 461)])
JPT.Debugger(element)
```
