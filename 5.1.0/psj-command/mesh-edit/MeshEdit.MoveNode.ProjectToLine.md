---
id: MeshEdit-MoveNode-ProjectToLine
title: MeshEdit.MoveNode.ProjectToLine()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: move node by project to line
---

## Description

Move node by project to line

## Syntax

```psj
MeshEdit.MoveNode.ProjectToLine(crlRefNodes=[], crlObjNodes=[], iType=0)
```

Ribbon: <menuselection>MeshEdit &#187; MoveNode &#187; ProjectToLine</menuselection>

## Inputs

### `crlRefNodes`

- A _List of Cursor_ specifying the reference nodes.
- The default value is [].

### `crlObjNodes`

- A _List of Cursor_ specifying the object nodes.
- The default value is [].

### `iType`

- An _Integer_ specifying the type.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.ProjectToLine(crlRefNodes=[], crlObjNodes=[], iType=0)
```
