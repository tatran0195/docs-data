---
id: Capture_CopyToClipboardTileWindow
title: Capture_CopyToClipboardTileWindow()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Copy tiled image of Main Window to clipboard.
This function works only if Jupiter is running with foreground mode.

## Syntax

```psj
Capture_CopyToClipboardTileWindow(bool WhiteBG)
```

## Inputs

### `1. Bool`

White background bool flag true = 1, false = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Capture_CopyToClipboardTileWindow(0)
```
