---
id: SetDisplayCommonLBCVisualize
title: SetDisplayCommonLBCVisualize()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Set common LBCs' display.

## Syntax

```psj
SetDisplayCommonLBCVisualize(int DisplayModeOfConstraint, int DisplayModeOfRBE2RBE3, int DisplayModeOfMPC, int DisplayModeOfSpring, int DisplayModeOfMass, int DisplayModeOfBush)
```

## Inputs

### `1. int`

Set display mode of Constraint.
- 0: Original
- 1: Visualize

### `2. int`

Set display mode of RBE2/RBE3.
- 0: Original
- 1: Visualize

### `3. int`

Set display mode of MPC.
- 0: Original
- 1: Visualize


### `4. int`

Set display mode of Spring.
- 0: Original
- 1: Visualize

### `5. int`

Set display mode of Mass.
- 0: Original
- 1: Visualize

### `6. int`

Set display mode of Bush.
- 0: Original
- 1: Visualize

## Return Code

No return code.

## Sample Code

```psj
SetDisplayCommonLBCVisualize(1, 1, 1, 1, 1, 1)
```
