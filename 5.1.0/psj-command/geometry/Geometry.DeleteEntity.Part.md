---
id: Geometry-DeleteEntity-Part
title: Geometry.DeleteEntity.Part()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Delete part entities
---

## Description

Delete part entities.

## Syntax

```psj
Geometry.DeleteEntity.Part(...)
```

Ribbon: <menuselection>Geometry &#187; Delete Entity &#187; Part</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying parts to be deleted.
- This is a required input.

## Return Code

True if success, or False if fail.

## Sample Code

```psj {3}
cube = Geometry.Part.Cube()

flag = Geometry.DeleteEntity.Part(crlParts=[cube])

JPT.Debugger(flag)
```
