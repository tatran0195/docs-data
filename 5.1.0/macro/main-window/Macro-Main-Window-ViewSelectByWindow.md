---
id: ViewSelectByWindow
title: ViewSelectByWindow()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Select all targets in the same plane as the selected targets.

## Syntax

```psj
ViewSelectByWindow(int TargetType)
```

## Inputs

### `1. Int`

An Integer specifying the target type to be selected.

## Return Code

A Cursor List specifying the selected faces or 2D elements.

## Sample Code

```psj
ViewSelectByWindow(3)
```
