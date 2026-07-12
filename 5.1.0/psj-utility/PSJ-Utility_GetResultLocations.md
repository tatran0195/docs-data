---
id: JPT-GetResultLocations
title: JPT.GetResultLocations()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get all the available data location existing on the inputted result type and direction
---

## Description

Get all the available data location existing on the inputted result type and direction.

## Syntax

```psj
JPT.GetResultLocations(PostAnalysisType,
                       resultSet,
                       timeStep,
                       resultName,
                       componentName)
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

### `componentName`

- A _String_ specifying a specific direction of the result (Such as X, Y, Z, etc.).
- This is a required input.

## Return Code

A _List of Integer_ containing all the available [PostResultDataLoc](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-loc-types) of the inputted result type and it's direction.

## Sample Code

```psj {5-11}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result_location = \
    JPT.GetResultLocations(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                           1,
                           1,
                           "Stress",
                           "XX")

JPT.Debugger(result_location)
#2: JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT
#4: JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT_NODE
```
