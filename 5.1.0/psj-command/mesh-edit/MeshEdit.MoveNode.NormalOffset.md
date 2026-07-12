---
id: MeshEdit-MoveNode-NormalOffset
title: MeshEdit.MoveNode.NormalOffset()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Move node(s) in Normal Direction of plane
---

## Description

Move node(s) in Normal Direction of plane

## Syntax

```psj
MeshEdit.MoveNode.NormalOffset(dMagnitude=0.0, ilNodeList=[])
```

Ribbon: <menuselection>MeshEdit &#187; MoveNode &#187; NormalOffset</menuselection>

## Inputs

### `dMagnitude`

- A _Double_ specifying the magnitude.
- The default value is 0.0.

### `ilNodeList`

- A _List of Integer_ specifying the node list.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.NormalOffset(dMagnitude=0.0, ilNodeList=[])
```
