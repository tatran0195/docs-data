---
id: Assemble-SeparateFaces-Shell
title: Assemble.SeparateFaces.Shell()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Separate shared Nodes for Shell that is shared between the shell parts into double nodes
---

## Description

Separate shared Nodes for Shell that is shared between the shell parts into double nodes.

## Syntax

```psj
Assemble.SeparateFaces.Shell(...)
```

Ribbon: <menuselection>Assemble &#187; Separate Faces &#187; Shell</menuselection>

## Inputs

### `iType`

- An _Integer_ specifying the type of entity to be selected.
- The default value is 0.

### `crlEntity`

- A _List of Cursor_ specifying the list of target item which will be separated.
- The default value is [].

### `bCreateGroup`

- A _Boolean_ enable/disable create group option.
- The default value is False.

## Return Code

A _List Cursor_ of separated edges if success, or _None_ if fail.

## Sample Code

```psj {8,9}
Geometry.Part.Cube(strName="Cube_1",
                   iPartColor=7697908)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube_2",
                   iPartColor=7463537)
MeshEdit.MergeNodes(crlTargets=[Part(1, 2)])

edges = Assemble.SeparateFaces.Shell(iType=1,
                                    crlEntity=[Part(1, 2)])
JPT.Debugger(edges)
```
