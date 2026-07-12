---
id: CmdMarkupFacePoint
title: CmdMarkupFacePoint()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Add note to selected FacePoint.

## Syntax

```psj
 CmdMarkupFacePoint([int Element, float xpos, float ypos, float zpos])
```

## Inputs

List of set of 1-4.

### `1. int  `

Element ID where indicated position belongs to.


### `2. float  `

x position in the view (global coordinate).


### `3. float  `

y position in the view (global coordinate).


### `4. float  `

z position in the view (global coordinate).


## Return Code

Nothing.

## Sample Code

```psj
CmdMarkupFacePoint([[2746, 7.959929, 4.940016, 10.000000]])
```
