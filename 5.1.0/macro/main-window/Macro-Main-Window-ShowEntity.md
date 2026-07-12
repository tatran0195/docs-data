---
id: Show_Entity
title: Show_Entity()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Show/hide all hidden entities.

## Syntax

```psj
Show_Entity(cursor[] crlTargets, bool bShow)
```

## Inputs

### `1. cursor[]`

- A Cursor List specifying the target to be shown/hidden.

### `2. bool`

- A Boolean specifying whether to show or hide the selected target.

## Return Code

- "1": The function can be executed.
- "0": The function cannot be executed.

## Sample Code

```psj
Show_Entity([164:1], 0)
```
