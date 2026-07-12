---
id: Geometry-DeleteEntity-Face
title: Geometry.DeleteEntity.Face()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Delete face entities
---

## Description

Delete face entities.

## Syntax

```psj
Geometry.DeleteEntity.Face(...)
```

Ribbon: <menuselection>Geometry &#187; Delete Entity &#187; Face</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying faces to be deleted.
- This is a required input.

## Return Code

True if success, or False if fail.

## Sample Code

```psj {3}
Geometry.Part.Cube()

flag = Geometry.DeleteEntity.Face(crlFaces=[Face(26)])

JPT.Debugger(flag)
```
