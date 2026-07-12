---
id: Test-FindFacesInPart
title: Test.FindFacesInPart()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Find faces in part by typical description
---

## Description

Find faces in part by typical description

## Syntax

```psj
Test.FindFacesInPart(crPart, strIdentical)
```

Ribbon: <menuselection>Test &#187; FindFacesInPart</menuselection>

## Inputs

### `crPart`

- A _Cursor_ specifying the part.
- This is a required input.

### `strIdentical`

- A _String_ specifying the identical.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.FindFacesInPart(crPart, strIdentical)
```
