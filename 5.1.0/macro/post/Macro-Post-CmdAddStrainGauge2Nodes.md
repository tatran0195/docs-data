---
id: CmdAddStrainGauge2Nodes
title: CmdAddStrainGauge2Nodes()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Execute Strain Gauge - 2 Nodes.

## Syntax

```psj
CmdAddStrainGauge2Nodes(int node1, int node2, double Width, double Height, double AmendFactor, string GaugeName)
```
## Inputs

### `1. int `

Target node1.

### `2. int `

Target node2.

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
CmdAddStrainGauge2Nodes(8365, 8608, 0.005, 0.005, 1, "")
```
