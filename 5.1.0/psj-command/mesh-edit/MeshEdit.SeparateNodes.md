---
id: MeshEdit-SeparateNodes
title: MeshEdit.SeparateNodes()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Separate nodes
---

## Description

Separate nodes

## Syntax

```psj
MeshEdit.SeparateNodes(crlShareNodes=[], crlTargets=[], iKeepNodeIDsOn=0)
```

Ribbon: <menuselection>MeshEdit &#187; SeparateNodes</menuselection>

## Inputs

### `crlShareNodes`

- A _List of Cursor_ specifying the share nodes.
- The default value is [].

### `crlTargets`

- A _List of Cursor_ specifying the target.
- The default value is [].

### `iKeepNodeIDsOn`

- An _Integer_ specifying the keep node i ds on.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.SeparateNodes(crlShareNodes=[], crlTargets=[], iKeepNodeIDsOn=0)
```
