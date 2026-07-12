---
id: JPT-GetTimeStepInfoName
title: JPT.GetTimeStepInfoName()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get the name of Time Step Info
---

## Description

Get the name of Time Step Info.

## Syntax

```psj
JPT.GetTimeStepInfoName(PostAnalysisType,
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

A _String_ specifying the name of Time Step information.

## Sample Code

```psj {5}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

time_step_info_name = JPT.GetTimeStepInfoName(2,1,1)
JPT.Debugger(time_step_info_name) # Mode 1, Freq=3.235953e+04
```
