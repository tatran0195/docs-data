---
id: Tools-BySelection-SelectionOrder
title: Tools.BySelection.SelectionOrder()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Renumber by selection order
---

## Description

Renumber by selection order

## Syntax

```psj
Tools.BySelection.SelectionOrder(crlTargets=[], iType=0, iMethod=0, iStartID=1, iIncrementStep=1, bAscending=True)
```

Ribbon: <menuselection>Tools &#187; BySelection &#187; SelectionOrder</menuselection>

## Inputs

### `crlTargets`

- A _List of Cursor_ specifying the target.
- The default value is [].

### `iType`

- An _Integer_ specifying the type.
- The default value is 0.

### `iMethod`

- An _Integer_ specifying the method.
- The default value is 0.

### `iStartID`

- An _Integer_ specifying the start ID.
- The default value is 1.

### `iIncrementStep`

- An _Integer_ specifying the increment step.
- The default value is 1.

### `bAscending`

- A _Boolean_ specifying the ascending.
- The default value is True.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.BySelection.SelectionOrder(crlTargets=[], iType=0, iMethod=0, iStartID=1, iIncrementStep=1, bAscending=True)
```
