---
id: MoveNodeDeform
title: MoveNodeDeform()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Move nodes based on solver result.

## Syntax

```psj
MoveNodeDeform(int solerType, string SolverResult, int step, double scale)
```

## Inputs

### `1. Int`

Solver type. 0: Nastran, 1: ADVC, 2: Abaqus, 3: Abaqus610.

### `2. String`

Path for solver result.

### `3. int`

Indicate the number of step(subcase).

### `4. Double`

Scale the magnitude of the result.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MoveNodeDeform(0, "C:/Temp/NastranData.op2", 0, 1)
```
