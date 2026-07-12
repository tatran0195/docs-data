---
id: Home-Windows-FrameCancel
title: Home.Windows.FrameCancel()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Reset placement of document windows to the original.
---

## Description

Reset placement of document windows to the original (full window).

## Syntax

```psj
Home.Windows.FrameCancel(...)
```

Macro: [FrameLessCancel](../../macro/home/FrameLessCancel)

Ribbon: <menuselection>Home &#187; Windows &#187; Cancel</menuselection>

## Inputs

This function does not require any input value.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not.
  - True: The function successfully executed.
  - False: The function cannot be executed.

## Sample Code

```psj {7}
# Prepare 2 JPT documents
JPT.CreateNewDocument()
JPT.CreateNewDocument()
Home.Windows.TileHorizontal(iMode=0)

# Cancel to the full window display.
Home.Windows.FrameCancel()
```
