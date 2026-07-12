---
id: MeshCleanup-Manual2D-Equivalence
title: MeshCleanup.Manual2D.Equivalence()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Equivalence Nodes
---

## Description

Equivalence Nodes

## Syntax

```psj
MeshCleanup.Manual2D.Equivalence(crlNodes, iTypeEquiva=0, dTolerance=1.0)
```

Ribbon: <menuselection>MeshCleanup &#187; Manual2D &#187; Equivalence</menuselection>

## Inputs

### `crlNodes`

- A _List of Cursor_ specifying the node.
- This is a required input.

### `iTypeEquiva`

- An _Integer_ specifying the type equiva.
- The default value is 0.

### `dTolerance`

- A _Double_ specifying the tolerance.
- The default value is 1.0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.Equivalence(crlNodes, iTypeEquiva=0, dTolerance=1.0)
```
