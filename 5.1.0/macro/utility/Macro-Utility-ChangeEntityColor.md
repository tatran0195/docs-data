---
id: ChangeEntityColor
title: ChangeEntityColor()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Change the colors of the selected entities.

## Syntax

```psj
ChangeEntityColor(Cursor[], color entityColor)
```

## Inputs

### `1. Cursor[]`

A list of entity to change color.

### `2. Color`

Specify the color to change.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ChangeEntityColor([11:703,11:704], 8421440)
```
