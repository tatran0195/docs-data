---
id: MeasureDistanceBy2Nodes
title: MeasureDistanceBy2Nodes()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Measure the distance between two nodes

## Syntax

```psj
MeasureDistanceBy2Nodes(cursor[] Cursors,String Target,Integer N)
```

## Inputs

### `1. cursor[]`

Nodes Cursor([10:*,10:**]\*,\*\* = Node ID)

### `2. String`

Target(Dist or X or Y or Z or ALL)

### `3. Integer N`

specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureDistanceBy2Nodes([10:447,10:468],"X",6)
```

```psj
MeasureDistanceBy2Nodes([10:447,10:468],"Dist",6)
```
