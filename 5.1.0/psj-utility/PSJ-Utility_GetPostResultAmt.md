---
id: JPT-GetPostResultAmt
title: JPT.GetPostResultAmt()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get Physical Amount information of the specify result
---

## Description

Get Physical Amount information of the specify result.

## Syntax

```psj
JPT.GetPostResultAmt(PostAnalysisType,
                     resultSet,
                     timeStep,
                     resultName,
                     componentName,
                     PostResultDataLoc)
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

### `PostResultDataLoc`

- An _Enum_ specifying the _[PostResultDataLoc](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-loc-types)_ describing the location of result (Such as on node, on element, etc.).
- This is a required input.

## Return Code

An _Integer_ specifying the [Physical Amount](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-amt-types) type of the working result.

## Sample Code

```psj {6-11}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, \
                               1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

amt_info = JPT.GetPostResultAmt(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                               1,
                               1,
                               "Stress",
                               "XX",
                               JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT_NODE)
JPT.Debugger(amt_info)
```
