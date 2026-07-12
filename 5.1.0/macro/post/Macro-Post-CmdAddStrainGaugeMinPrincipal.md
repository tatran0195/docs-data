---
id: CmdAddStrainGaugeMinPrincipal
title: CmdAddStrainGaugeMinPrincipal()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Execute Strain Gauge - Min principal.

## Syntax

```psj
CmdAddStrainGaugeMinPrincipal(int[] nodes, double Width, double Height, double AmendFactor, string GaugeName)
```
## Inputs

### `1. int[] `

Target nodes.

### `2. double `

Gauge Width.

### `3. double `

Gauge Height.

#### `4. double `

Amend Factor.

#### `5. string `

Gauge name.

## Return Code

Nothing.

## Sample Code

```psj
CmdAddStrainGaugeMinPrincipal([9428], 0, 0, 1, "")
```
