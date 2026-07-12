---
id: JPT-GetResultIncrements
title: JPT.GetResultIncrements()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get all the existing increments of the inputted result step
---

## Description

Get all the existing increments of the inputted result step.

## Syntax

```psj
JPT.GetResultIncrements(PostAnalysisType,
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

A _List of Integer_ containing all the existing increments of the inputted result type with it's step.

## Sample Code

```psj {5-8}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result_increments = \
    JPT.GetResultIncrements(JPT.PostAnalysisType.POST_ANALYSIS_MODAL,
                            1)

JPT.Debugger(result_increments)
```
