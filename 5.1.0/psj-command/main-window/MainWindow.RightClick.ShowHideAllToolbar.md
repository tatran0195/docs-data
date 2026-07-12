---
id: MainWindow-RightClick-ShowHideAllToolbar
title: MainWindow.RightClick.ShowHideAllToolbar()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Show/hide the toolbar on working document
---

## Description

Show/hide the toolbar on working document.

## Syntax

```psj
MainWindow.RightClick.ShowHideAllToolbar(...)
```

Macro: [ShowHideAllToolbar](../../macro/main-window/ShowHideAllToolbar)

Ribbon: <menuselection>MainWindow &#187; RightClick &#187; ShowHideAllToolbar</menuselection>

## Inputs

### `iType`

- An _Integer_ specifying toolbar type to be shown/hidden.
    - 0: View selection toolbar.
    - 1: Main window toolbar.
- The default value is 0.

### `bShow`

- A _Boolean_ specifying whether to show/hide the toolbar.
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj
MainWindow.RightClick.ShowHideAllToolbar(bShow=True)
```
