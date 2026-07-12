---
id: SetPartAppearance
title: SetPartAppearance()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Set appearance of a part.

## Syntax

```psj
SetPartAppearance(Cursor[] tacursor, String Type, Bool Show)
```

## Inputs

### `1. Cursor[]`

Cursor list of target entities

### `2. String`

- A _String_ specifying appearance target.
    - "Surface"
    - "Mesh"
    - "Edge"
    - "Node"

### `3. Bool`

-A _Boolean_ specifying Show or Hide.
- The default value is _True_ (Show).

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
SetPartAppearance([3:1], "Mesh", 1)
```
