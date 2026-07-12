---
id: JPT-Exec
title: JPT.Exec()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Run Jupiter macro
---

## Description

Run Jupiter macro.

## Syntax

```psj
JPT.Exec(macroCommand)
```

## Inputs

### `macroCommand`

- A _String_ specifying the macro command.
- This is a required input.

## Return Code

Based on the output of the inputted macro command.

## Sample Code

```psj {2,3}
# Create a cube and store its cursor
createdCube = JPT.Exec('CreateCube([0, 0, 0], [0.01, 0.01, 0.01], \
                        [10, 10, 10], "Cube_1", 12999622, 0:0)')
JPT.Debugger(createdCube) # Return a string object with value = 3:1
```
