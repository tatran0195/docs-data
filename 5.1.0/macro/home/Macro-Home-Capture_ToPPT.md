---
id: Capture_ToPPT
title: Capture_ToPPT()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Save the display window of Jupiter to an image file in pptx.

## Syntax

```psj
Capture_ToPPT(bool bAutoCapture, int[] listAdjust)
```

## Inputs

### `1. Bool`

Specify whether crop image to the displayed entity range.

### `2. int[]`

Specify the left, top, right and bottom margins from the minimized area.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Capture_ToPPT(0, [0,0,0,0])
```
