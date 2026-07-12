---
id: ViewSelectReverse
title: ViewSelectReverse()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Select all targets of the same type as the specified target that are displayed in the current document.

## Syntax

```psj
ViewSelectReverse(int TargetType, cursor[] Targets)
```

## Inputs

### `1. Int`

An Integer specifying the target type to be selected.

### `2. Cursor[]`

A Cursor List specifying the targets.

## Return Code

A List of Cursor specifying the selected entities in revert.

## Sample Code

```psj
ViewSelectReverse(3,[])
```
