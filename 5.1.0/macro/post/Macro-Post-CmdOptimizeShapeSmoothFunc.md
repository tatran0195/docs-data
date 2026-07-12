---
id: CmdOptimizeShapeSmoothFunc
title: CmdOptimizeShapeSmoothFunc()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Smoothing topology optimization result

## Syntax

```psj
CmdOptimizeShapeSmoothFunc(cursor [], cursor [], double tol, int nlayer, int cycle, double factor, double meshSize, bool keep)
```
## Inputs
### `1. cursor[]  `

Designed parts

### `2. cursor[] `

Non-designed parts

### `3. double `

Tolerance of density

### `4. int  `

Number of remove layer

#### `5. int `

Number of looping

#### `6. double `

factor

#### `7. double `

Mesh size

### `8. bool  `

Keep shared nodes

## Return Code

Nothing.

## Sample Code

```psj
CmdOptimizeShapeSmoothFunc([3:1], [], 0.670000, 1, 50, 0.300000, 0.002845, 0)
```
