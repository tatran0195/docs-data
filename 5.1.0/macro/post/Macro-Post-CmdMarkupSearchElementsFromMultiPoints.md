---
id: CmdMarkupSearchElementsFromMultiPoints
title: CmdMarkupSearchElementsFromMultiPoints()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Search nearest elements from indicated positions and put notes at the elementss.

## Syntax

```psj
CmdMarkupSearchElementsFromMultiPoints(vector[] positions)
```

## Inputs

### `1. vector[] `

List of search position [x,y,z].

## Return Code

### `1. bool []`

List of succeed(1) or failed(0).

## Sample Code

```psj
CmdMarkupSearchElementsFromMultiPoints([0.000000, 0.000000, 0.000000],[0.000000, 5.000000, 0.000000],[10.000000, 5.000000, 0.000000],[10.000000, 10.000000, 5.000000])
>> [1,1,1,1]
```
