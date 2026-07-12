---
id: MeshEdit-DeleteNode
title: MeshEdit.DeleteNode()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Delete floating nodes in db
---

## Description

Delete floating nodes in db

## Syntax

```psj
MeshEdit.DeleteNode(crlNodes=[], bRemoveVertex=True)
```

Ribbon: <menuselection>MeshEdit &#187; DeleteNode</menuselection>

## Inputs

### `crlNodes`

- A _List of Cursor_ specifying the node.
- The default value is [].

### `bRemoveVertex`

- A _Boolean_ specifying the remove vertex.
- The default value is True.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.DeleteNode(crlNodes=[], bRemoveVertex=True)
```
