---
id: ShowHideAllToolbar
title: ShowHideAllToolbar()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Show/hide the toolbar on working document.

## Syntax

```psj
ShowHideAllToolbar(int Type, bool Show)
```

## Inputs

### `1. int`

An Integer specifying toolbar type to be shown/hidden. 

### `2. bool`

A Boolean specifying whether to show/hide the toolbar.

## Return Code

- "1": The function can be executed.
- "0": The function cannot be executed.

## Sample Code

```psj
ShowHideAllToolbar(0, True)
```
