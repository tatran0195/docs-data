---
id: MeshCleanup-Manual3D-DeleteNode
title: MeshCleanup.Manual3D.DeleteNode()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: remove node for solid element.
---

## Description

Remove node for solid element.

## Syntax

```psj
MeshCleanup.Manual3D.DeleteNode(crlNodes)
```

Ribbon: <menuselection>MeshCleanup &#187; Manual3D &#187; DeleteNode</menuselection>

## Inputs

### `crlNodes`

- A _List of Cursor_ specifying the node.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual3D.DeleteNode(crlNodes)
```
