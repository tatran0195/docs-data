---
id: SetHidingElementFactor
title: SetHidingElementFactor()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Set Optimized Shape value and result that is threshold for being a hidden element.

## Syntax

```psj
SetHiddingElementFactor(float OptimizedShape, string ResultName)
```

## Inputs

### `1. float `

Specify Optimized Shape value to hide element.

### `2. string `

Specify result to use as hiding elemet source. "NodalDensityRatio" or "DensityRatio".

## Return Code

Nothing.

## Sample Code

```psj
SetHidingElementFactor(0.28, "NodalDensityRatio")

```
