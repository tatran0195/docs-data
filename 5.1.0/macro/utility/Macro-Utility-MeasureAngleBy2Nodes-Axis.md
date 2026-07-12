---
id: MeasureAngleBy2Nodes_Axis
title: MeasureAngleBy2Nodes_Axis()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Measure the angle created by 2 nodes and Axis.

## Syntax

```psj
MeasureAngleBy2Nodes_Axis(cursor node1,cursor node2,Axis xyz,String Target,Integer N)
```

## Inputs

### `1. Cursor`

node cursor(10:_;_=node id)

### `2. Cursor`

node cursor(10:_;_=node id)

### `3. Axis`

unit vector([x,y,z])

### `4. String`

Target (Angle or XY or YZ or ZX or ALL)

### `5. Integer N`

specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureAngleBy2Nodes_Axis(10:331,10:323,[0,0,1],"ALL",6)
```

or

```psj
MeasureAngleBy2Nodes_Axis(10:331,10:323,[0,0,1],"Angle",6)
```
