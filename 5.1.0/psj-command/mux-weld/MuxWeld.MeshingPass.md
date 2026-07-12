---
id: MuxWeld-MeshingPass
title: MuxWeld.MeshingPass()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: sweep cross section to create welding
---

## Description

Sweep cross section to create welding

## Syntax

```psj
MuxWeld.MeshingPass(crPart=None, crlEdges=[], dMeshSize=0.0)
```

Ribbon: <menuselection>MuxWeld &#187; MeshingPass</menuselection>

## Inputs

### `crPart`

- A _Cursor_ specifying the part.
- The default value is None.

### `crlEdges`

- A _List of Cursor_ specifying the edge.
- The default value is [].

### `dMeshSize`

- A _Double_ specifying the mesh size.
- The default value is 0.0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MuxWeld.MeshingPass(crPart=None, crlEdges=[], dMeshSize=0.0)
```
