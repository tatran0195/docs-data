---
id: MeshEdit-MoveNode-ProjectToPlaneElem
title: MeshEdit.MoveNode.ProjectToPlaneElem()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Move Node by Project to Plane(Elem)
---

## Description

Move Node by Project to Plane(Elem)

## Syntax

```psj
MeshEdit.MoveNode.ProjectToPlaneElem(crlNodes=[], crlElems=[])
```

Ribbon: <menuselection>MeshEdit &#187; MoveNode &#187; ProjectToPlaneElem</menuselection>

## Inputs

### `crlNodes`

- A _List of Cursor_ specifying the node.
- The default value is [].

### `crlElems`

- A _List of Cursor_ specifying the element.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.ProjectToPlaneElem(crlNodes=[], crlElems=[])
```
