---
id: SetNoteNumericDisplay
title: SetNoteNumericDisplay()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Set numeric display of notes.

## Syntax

```psj
SetNoteNumericDisplay(bool type, int width, int precision)
```

## Inputs

### `1. bool`

Type of numeric display.
- 0: Real type.
- 1: Power type.

### `2. int`

Specify numeric width.

### `2. int`

Specify numeric precision.

## Return Code

Nothing.

## Sample Code

```psj
SetNoteNumericDisplay(0, 10, 5)
```
