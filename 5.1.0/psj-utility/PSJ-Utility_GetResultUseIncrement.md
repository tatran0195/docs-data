---
id: JPT-GetResultUseIncrement
title: JPT.GetResultUseIncrement()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Check whether the result having any increment or not
---

## Description

Check whether the result has any increment or not.

## Syntax

```psj
JPT.GetResultUseIncrement(PostAnalysisType,
                          resultSet)
```

## Inputs

### `PostAnalysisType`

- An _Enum_ specifying the _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.
- This is a required input.

### `resultSet`

- An _Integer_ specifying the step ID of the imported result.
- This is a required input.

## Return Code

A _Boolean_ specifying the existence of the increment of the inputted time step.

## Sample Code

```psj {5-6}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

is_increment_exist = \
    JPT.GetResultUseIncrement(JPT.PostAnalysisType.POST_ANALYSIS_MODAL, 1)

JPT.Debugger(is_increment_exist)
```
