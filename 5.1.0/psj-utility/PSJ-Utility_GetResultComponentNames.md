---
id: JPT-GetResultComponentNames
title: JPT.GetResultComponentNames()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get all the available result direction of the inputted result type
---

## Description

Get all the available result directions of the inputted result type.

## Syntax

```psj
JPT.GetResultComponentNames(PostAnalysisType,
                            resultSet,
                            timeStep,
                            resultName,
                            BoolType)
```

## Inputs

### `PostAnalysisType`

- An _Enum_ specifying the _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.
- This is a required input.

### `resultSet`

- An _Integer_ specifying the step ID of the imported result.
- This is a required input.

### `timeStep`

- An _Integer_ specifying the time step of the imported result.
- This is a required input.

### `resultName`

- A _String_ specifying the type of result (Such as Displacement, Stress, etc.).
- This is a required input.

### `BoolType`

- An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the selection:
  - _True_: Select the inputted entity with its ID.
  - _False_: Deselect the inputted entity with its ID.
- This is a required input.

## Return Code

A _List of String_ containing all the available data directions of the inputted result type.

## Sample Code

```psj {5-10}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

steps=JPT.GetResultSteps()
for step in steps:
    incs=JPT.GetResultIncrements(step.first, step.third)
    for inc in incs:
        result_comp_name = JPT.GetResultComponentNames(step.first,     # analysis type
                                                       step.third,     # result set
                                                       inc,            # time step
                                                       "Displacement", # result name
                                                       JPT.BoolType.TRUE_VAL)

        JPT.Debugger(result_comp_name)

```
