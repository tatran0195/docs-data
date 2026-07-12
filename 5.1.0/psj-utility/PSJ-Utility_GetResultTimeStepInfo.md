---
id: JPT-GetResultTimeStepInfo
title: JPT.GetResultTimeStepInfo()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get the relating information of the inputted result step with it's time step
---

## Description

Get the relating information of the inputted result step with it's time step.

## Syntax

```psj
JPT.GetResultTimeStepInfo(PostAnalysisType,
                          resultSet,
                          timeStep)
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

## Return Code

A _[PostTimeStepInfo](../data-type/psj-utility/post-utility/post-built-in-types/post-time-step-info)_ object specifying the information relating to the inputted time step.

## Sample Code

```psj {5-8}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result_time_step_info = JPT.GetResultTimeStepInfo(JPT.PostAnalysisType.POST_ANALYSIS_MODAL,
                                           1,
                                           10)

JPT.Debugger(result_time_step_info)

print(result_time_step_info.mode)
print(result_time_step_info.time)
print(result_time_step_info.freq)
```
