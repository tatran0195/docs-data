---
id: CmdDistancePlot
title: CmdDistancePlot()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Distance Plot.

## Syntax

```psj
CmdDistancePlot(int Node1, int Node2, PostStepItem [] stepItem, bool DistXYZ, bool PosXYZ )
```

## Inputs

### `1. int  `

Node 1 ID

### `2. int  `

Node 2 ID

### `3. PostStepItem [] `

Source results.

PostStepItems are:
1. int - Analysis type. 
2. int - Result set.
3. int - Time step.

### `4. bool `

X, Y, Z Distance Plot flag.

### `5. bool `

X, Y, Z Position Plot flag.

## Return Code

Nothing.

## Sample Code

```psj
CmdDistancePlot(8, 2, [[1,0,0], [1,0,1], [1,0,2], [1,0,3]], 0, 1)
```
