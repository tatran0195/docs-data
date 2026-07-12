---
id: MeshCleanup-Manual2D-Collapse
title: MeshCleanup.Manual2D.Collapse()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Delete and combine 2D element
---

## Description

Delete and combine 2D element.

## Syntax

```psj
MeshCleanup.Manual2D.Collapse(crNodeRef=None, crNodeEq=None)
```

Ribbon: <menuselection>MeshCleanup &#187; Manual2D &#187; Collapse</menuselection>

## Inputs

### `crNodeRef`

- A _Cursor_ specifying the reference node.
- The default value is None.

### `crNodeEq`

- A _Cursor_ specifying the equivalence node.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {2}
Geometry.Part.Cube(strName="Cube_2", iPartColor=7434735)
MeshCleanup.Manual2D.Collapse(crNodeRef=Node(95), crNodeEq=Node(96))
```
