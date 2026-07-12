---
id: JPT-GetResultNames
title: JPT.GetResultNames()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/

description: Get all the available result type existing on the model
---

## Description

Get all the available result type existing on the model.

## Syntax

```psj
JPT.GetResultNames(PostAnalysisType,
                   resultSet,
                   timeStep,
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

### `BoolType`

- An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ specifying whether to use the name of the current language setting.
  - _True_: Use the name of the current language setting.
  - _False_: Use the English name.
- This is a required input.

  :::tip
  You also can input **1** or **True** instead of inputting JPT.BoolType.TRUE_VAL  
  You also can input **0** or **False** instead of inputting JPT.BoolType.FALSE_VAL
  :::

## Return Code

A _List of String_ containing all the available result types existing on the model.

## Sample Code

```psj {5-9}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

#Get All Result Names in all steps and increments
steps=JPT.GetResultSteps()
for step in steps:
    incs=JPT.GetResultIncrements(step.first, step.third)
    for inc in incs:
        result_name = JPT.GetResultNames(step.first,    #analysis type
                                         step.third,    #result set
                                         inc,           #time step
                                         JPT.BoolType.TRUE_VAL)

        JPT.Debugger(result_name)
```
