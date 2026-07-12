---
id: MeshEdit-MoveNode-StraightenMidnodes
title: MeshEdit.MoveNode.StraightenMidnodes()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: move node by straighten_mid_nodes
---

## Description

Move node by straighten_mid_nodes

## Syntax

```psj
MeshEdit.MoveNode.StraightenMidnodes(crlParts=[], crlFaces=[], crlEdges=[], crlNodes=[])
```

Ribbon: <menuselection>MeshEdit &#187; MoveNode &#187; StraightenMidnodes</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the part.
- The default value is [].

### `crlFaces`

- A _List of Cursor_ specifying the face.
- The default value is [].

### `crlEdges`

- A _List of Cursor_ specifying the edge.
- The default value is [].

### `crlNodes`

- A _List of Cursor_ specifying the node.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.StraightenMidnodes(crlParts=[], crlFaces=[], crlEdges=[], crlNodes=[])
```
