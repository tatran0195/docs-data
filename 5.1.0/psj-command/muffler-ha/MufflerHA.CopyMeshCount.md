---
id: MufflerHA-CopyMeshCount
title: MufflerHA.CopyMeshCount()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

## Syntax

```psj
MufflerHA.CopyMeshCount(crlMasterEdge, crlSlaveEdge, strBaseName)
```

Ribbon: <menuselection>MufflerHA &#187; CopyMeshCount</menuselection>

## Inputs

### `crlMasterEdge`

- A _List of Cursor_ specifying the master edge.
- This is a required input.

### `crlSlaveEdge`

- A _List of Cursor_ specifying the slave edge.
- This is a required input.

### `strBaseName`

- A _String_ specifying the base name.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MufflerHA.CopyMeshCount(crlMasterEdge, crlSlaveEdge, strBaseName)
```
