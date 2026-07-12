---
id: Test-ZGeometryTest-IntersectionCheck
title: Test.ZGeometryTest.IntersectionCheck()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Intersection check
---

## Description

Intersection check

## Syntax

```psj
Test.ZGeometryTest.IntersectionCheck(crlParts, crlFaces, crlElems, iType)
```

Ribbon: <menuselection>Test &#187; ZGeometryTest &#187; IntersectionCheck</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the part.
- This is a required input.

### `crlFaces`

- A _List of Cursor_ specifying the face.
- This is a required input.

### `crlElems`

- A _List of Cursor_ specifying the element.
- This is a required input.

### `iType`

- An _Integer_ specifying the type.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.ZGeometryTest.IntersectionCheck(crlParts, crlFaces, crlElems, iType)
```
