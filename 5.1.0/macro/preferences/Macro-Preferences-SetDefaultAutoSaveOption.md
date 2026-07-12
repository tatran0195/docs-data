---
id: SetDefaultAutoSaveOption
title: SetDefaultAutoSaveOption()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Set auto save options.

## Syntax

```psj
SetDefaultAutoSaveOption(int Flag, int Interval, int NumberOfSaveFiles)
```

## Inputs

### `1. int`

Enable auto save.
- 0: OFF
- 1: ON

### `2. int`

Interval of auto save (minutes).

### `3. int`

Number of save files.

## Return Code

No return code.

## Sample Code

```psj
SetDefaultAutoSaveOption(1, 15, 2)
```
