---
id: CmdAddStrainGaugeNodePoint
title: CmdAddStrainGaugeNodePoint()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Execute Strain Gauge - Node-Point.

## Syntax

```psj
CmdAddStrainGaugeNodePoint(int node, vector position, double Width, double Height, double AmendFactor, string GaugeName)
```
## Inputs

### `1. int `

Target node1.

### `2. vector `

position x,y,z.

### `3. double `

Gauge Width.

### `4. double `

Gauge Height.

#### `5. double `

Amend Factor.

#### `6. string `

Gauge name.

## Return Code

Nothing.

## Sample Code

```psj
CmdAddStrainGaugeNodePoint(8647, [-0.00256365, -0.00125307, 0.000465], 5, 5, 1, "")
```
