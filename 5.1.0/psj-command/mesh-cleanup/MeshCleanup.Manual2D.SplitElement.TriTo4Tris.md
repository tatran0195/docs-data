---
id: MeshCleanup-Manual2D-SplitElement-TriTo4Tris
title: MeshCleanup.Manual2D.SplitElement.TriTo4Tris()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Convert a single triangle element into four triangular elements.
---

## Description

Convert a single triangle element into four triangular elements.

## Syntax

```psj
MeshCleanup.Manual2D.SplitElement.TriTo4Tris(...)
```

Ribbon: <menuselection>MeshCleanup &#187; Manual2D &#187; SplitElement &#187; TriTo4Tris</menuselection>

## Inputs

### `crlElems`

- A _List of Cursor_ specifying the element.
- The default value is [].

### `crDatumNode0`

- A _Cursor_ specifying the datum node0.
- The default value is None.

### `crDatumNode1`

- A _Cursor_ specifying the datum node1.
- The default value is None.

### `iMethod`

- An _Integer_ specifying the method.
- The default value is 0.

### `iAutoExecute`

- An _Integer_ specifying the auto execute.
- The default value is 0.

### `iAutoTransition`

- An _Integer_ specifying the auto transition.
- The default value is 0.

### `iCADProject`

- An _Integer_ specifying the CAD project.
- The default value is 0.

### `iMergeNode`

- An _Integer_ specifying the merge node.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{4}
# Prepare model
Geometry.Part.Cube(ilAxialNodes=[3, 3, 3], iPartColor=7463537)

# Devide Triangle Element 76 into 4 smaller trianbles.
MeshCleanup.Manual2D.SplitElement.TriTo4Tris(crlElems=[Elem(76)], iMethod=8, iAutoExecute=1, iMergeNode=1)
```
