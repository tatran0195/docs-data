---
id: Test-CreateElementForWelding
title: Test.CreateElementForWelding()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create weld elements
---

## Description

Create weld elements

## Syntax

```psj
Test.CreateElementForWelding(crlSrcElems, crlDstElems, crlSideElems, crlParts, crMaterial)
```

Ribbon: <menuselection>Test &#187; CreateElementForWelding</menuselection>

## Inputs

### `crlSrcElems`

- A _List of Cursor_ specifying the source elems.
- This is a required input.

### `crlDstElems`

- A _List of Cursor_ specifying the dst elems.
- This is a required input.

### `crlSideElems`

- A _List of Cursor_ specifying the side elems.
- This is a required input.

### `crlParts`

- A _List of Cursor_ specifying the part.
- This is a required input.

### `crMaterial`

- A _Cursor_ specifying the material.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.CreateElementForWelding(crlSrcElems, crlDstElems, crlSideElems, crlParts, crMaterial)
```
