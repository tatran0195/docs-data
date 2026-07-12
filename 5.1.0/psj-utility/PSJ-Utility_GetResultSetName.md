---
id: JPT-GetResultSetName
title: JPT.GetResultSetName()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get the name of Result Set (Subcase)
---

## Description

Get the name of Result Set (Subcase).

## Syntax

```psj
JPT.GetResultSetName(PostAnalysisType,
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

A _String_ specifying the name of Result Set (Subcase).

## Sample Code

```psj {5}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result_set_name = JPT.GetResultSetName(1,1)
JPT.Debugger(result_set_name)
```
