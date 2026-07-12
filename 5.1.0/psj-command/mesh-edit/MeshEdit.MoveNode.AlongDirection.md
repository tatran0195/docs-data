---
id: MeshEdit-MoveNode-AlongDirection
title: MeshEdit.MoveNode.AlongDirection()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

## Syntax

```psj
MeshEdit.MoveNode.AlongDirection(crlNodes=[], crElem=None, crFace=None, vecDirection=[0,0,0], dMagnitude=0.0, bDestination=False)
```

Ribbon: <menuselection>MeshEdit &#187; MoveNode &#187; AlongDirection</menuselection>

## Inputs

### `crlNodes`

- A _List of Cursor_ specifying the node.
- The default value is [].

### `crElem`

- A _Cursor_ specifying the element.
- The default value is None.

### `crFace`

- A _Cursor_ specifying the face.
- The default value is None.

### `vecDirection`

- A _Vector_ specifying the direction.
- The default value is [0,0,0].

### `dMagnitude`

- A _Double_ specifying the magnitude.
- The default value is 0.0.

### `bDestination`

- A _Boolean_ specifying the destination.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.AlongDirection(crlNodes=[], crElem=None, crFace=None, vecDirection=[0,0,0], dMagnitude=0.0, bDestination=False)
```
