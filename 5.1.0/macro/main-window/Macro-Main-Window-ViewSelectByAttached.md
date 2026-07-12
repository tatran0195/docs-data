---
id: ViewSelectByAttached
title: ViewSelectByAttached()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Invert hide targets by context menu.

## Syntax

```psj
ViewSelectByAttached(int TargetType, cursor[] Targets)
```

## Inputs

### `1. Int`

An Integer specifying the target type to be selected.

### `2. Cursor[]`

A List of Cursor specifying the targets to select the attached ones from them.

## Return Code

A Cursor List specifying the selected parts (faces or 2D elements).

## Sample Code

```psj
ViewSelectByAttached(3,[])
```
