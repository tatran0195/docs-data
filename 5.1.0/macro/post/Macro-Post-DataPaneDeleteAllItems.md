---
id: DataPaneDeleteAllItems
title: DataPaneDeleteAllItems()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Delete all items in specific pane of Watch Data Window.

## Syntax

```psj
DataPaneDeleteAllItems(int pane)
```

## Inputs

### `1. int `

Pane number. 1: Node, 2: Element, 3: Position, 3: Node Plot Scan, 4: Element Plot Scan, 5: Position Plot Scan, 6: Strain Gauge, 7: Peak Search, 8: Max/Min, 9: Area Max/Min, 10: Fatigue Strentgh, 11: Compare.

## Return Code

Nothing.

## Sample Code

```psj
DataPaneDeleteAllItems(1)
```
