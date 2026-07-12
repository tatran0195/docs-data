---
id: Geometry-Part-Elems
title: Geometry.Part.Elems()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: create part from element
---

## Description

Create part from element

## Syntax

```psj
Geometry.Part.Elems(crlElems, strName)
```

Ribbon: <menuselection>Geometry &#187; Part &#187; Elems</menuselection>

## Inputs

### `crlElems`

- A _List of Cursor_ specifying the element.
- This is a required input.

### `strName`

- A _String_ specifying the part name.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Elems(crlElems, strName)
```
