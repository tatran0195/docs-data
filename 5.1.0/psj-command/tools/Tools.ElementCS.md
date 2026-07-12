---
id: Tools-ElementCS
title: Tools.ElementCS()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: create element coordinate system
---

## Description

Create element coordinate system

## Syntax

```psj
Tools.ElementCS(iMethod=0, iDispType=0, bDispXDir=False, bDispCoord=False, dDispScale=1, crlTargets=[])
```

Ribbon: <menuselection>Tools &#187; ElementCS</menuselection>

## Inputs

### `iMethod`

- An _Integer_ specifying the method.
- The default value is 0.

### `iDispType`

- An _Integer_ specifying the displacement type.
- The default value is 0.

### `bDispXDir`

- A _Boolean_ specifying the displacement x direction.
- The default value is False.

### `bDispCoord`

- A _Boolean_ specifying the displacement coordinate.
- The default value is False.

### `dDispScale`

- A _Double_ specifying the displacement scale.
- The default value is 1.

### `crlTargets`

- A _List of Cursor_ specifying the target.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.ElementCS(iMethod=0, iDispType=0, bDispXDir=False, bDispCoord=False, dDispScale=1, crlTargets=[])
```
