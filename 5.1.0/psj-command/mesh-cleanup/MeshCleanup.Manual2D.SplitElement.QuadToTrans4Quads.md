---
id: MeshCleanup-Manual2D-SplitElement-QuadToTrans4Quads
title: MeshCleanup.Manual2D.SplitElement.QuadToTrans4Quads()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Convert a single quadrilateral element into four quadrilateral elements.
---

## Description

Convert a single quadrilateral element into four quadrilateral elements.

## Syntax

```psj
MeshCleanup.Manual2D.SplitElement.QuadToTrans4Quads(crlElems=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)
```

Ribbon: <menuselection>MeshCleanup &#187; Manual2D &#187; SplitElement &#187; QuadToTrans4Quads</menuselection>

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

```psj
MeshCleanup.Manual2D.SplitElement.QuadToTrans4Quads(crlElems=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)
```
