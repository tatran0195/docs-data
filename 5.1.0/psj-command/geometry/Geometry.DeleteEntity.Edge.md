---
id: Geometry-DeleteEntity-Edge
title: Geometry.DeleteEntity.Edge()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Delete the selected edge entities
---

## Description

Delete the selected edge entities.

## Syntax

```psj
Geometry.DeleteEntity.Edge(...)
```

Ribbon: <menuselection>Geometry &#187; Delete Entity &#187; Edge</menuselection>

## Inputs

### `crlEdges`

- A _List of Cursor_ specifying edges to be deleted.
- This is a required input.

## Return Code

True if success, or False if fail.

## Sample Code

```psj {3}
Geometry.Part.Cube()

flag = Geometry.DeleteEntity.Edge(crlEdges=[Edge(15, 18, 19)])

JPT.Debugger(flag)
```
