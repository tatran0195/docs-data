---
id: ViewMakeUserFrame 
title: ViewMakeUserFrame()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create a new user frame

## Syntax

```psj
ViewMakeUserFrame(string nameOfFrame, int StartPointX, int StartPointY, int endPointX, int EndPointY, bool Mode )
```

## Inputs

### `1. string`

Name of the user frame.

### `2. int`

Specify start point in x direction.

### `3. int`

Specify start point in y direction.

### `4. int`

Specify end point in x direction (start point x + width).

### `5. int`

Specify end point in y direction (start point y + height).

### `6. bool`

Specify Single or Mutiple mode.
- 0 : Single
- 1 : Multiple

## Return Code

No return value.

## Sample Code

```psj
ViewMakeUserFrame("New_Frame_1 ((Multiple))", 294, 128, 588, 257, 1)
```
