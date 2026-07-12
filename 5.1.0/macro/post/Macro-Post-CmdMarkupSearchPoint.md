---
id: CmdMarkupSearchPoint
title: CmdMarkupSearchPoint()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Search element from position

## Syntax

```psj
CmdMarkupSearchPoint(Real x, Real y, Real z, Real Tolerance, bool DisplayPartOnly)
```

## Inputs

### `1. Real`

X position

### `2. Real`

Y position

### `3. Real`

Z potision

### `4. Real`

Tolerance of search surface.

### `5. bool`

Restrict search target only displayed parts. true = 1,false = 0

## Return Code

- "1": If element found.
- "FALSE": If no element found.

## Sample Code

```psj
CmdMarkupSearchPoint(29.300000, 27.000000, 7.186000, 0.010000, 0)
```
