---
id: Properties-ThicknessDistribution
title: Properties.ThicknessDistribution()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Properties view Thickness Distribution
---

## Description

Properties view Thickness Distribution

## Syntax

```psj
Properties.ThicknessDistribution(dMax=1, dMin=0, iByEach=0, dlThicknessValueSet=[])
```

Ribbon: <menuselection>Properties &#187; ThicknessDistribution</menuselection>

## Inputs

### `dMax`

- A _Double_ specifying the maximum.
- The default value is 1.

### `dMin`

- A _Double_ specifying the minimum.
- The default value is 0.

### `iByEach`

- An _Integer_ specifying the by each.
- The default value is 0.

### `dlThicknessValueSet`

- A _Double List_ specifying the thickness value set.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.ThicknessDistribution(dMax=1, dMin=0, iByEach=0, dlThicknessValueSet=[])
```
