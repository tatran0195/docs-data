---
id: ViewPartsTransparency
title: ViewPartsTransparency()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Change the color of the selected part.

## Syntax

```psj
ChangeBodyColor(Cursor[] parts, double transparency)
```

## Inputs

### `1. Cursor[]`

A list of cursor specify parts.

### `2. double`

Specify transparency of the parts.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ViewPartsTransparency([3:1], 0.2)
```
