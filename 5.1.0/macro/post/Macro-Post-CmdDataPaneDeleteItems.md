---
id: CmdDataPaneDeleteItems
title: CmdDataPaneDeleteItems()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Delete all the data in specified tab of Watch Data Window.

## Syntax

```psj
CmdDataPaneDeleteItems(int Tab, int[] items)
```

## Inputs

### `1. int `

Tab ID.

### `2. int [] `

ID list of delete line.

## Return Code

Nothing.

## Sample Code

```psj
CmdDataPaneDeleteItems(1, [1,2,3,4])
```
