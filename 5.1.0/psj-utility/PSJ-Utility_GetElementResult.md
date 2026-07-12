---
id: JPT-GetElementResult
title: JPT.GetElementResult()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get all elements with the loaded element results that satisfy a condition
---

## Description

Get elements with loaded results satisfy a condition.

## Syntax

```psj
JPT.GetElementResult(PostDataRangeType,
                     resultValue,
                     adjustment)
```

## Inputs

### `PostDataRangeType`

- An _Enum_ specifying the _[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_ describing the condition to get the element results.
- This is a required input.

### `resultValue`

- A _Double_ specifying the referenced value.
- This is a required input.

### `adjustment`

- A _Double_ specifying the adjustment to the referenced value _[resultValue](#resultvalue)_:
  - If _[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_ is a scalar type (i.e. EQ, NE, LT, GT, LE, GE), then the range to get the result is from (resultValue - adjustment) to (resultValue + adjustment)
  - If _[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_ is a range type (i.e. IR, OR, IRE, ORE), then the range to get the result is from (resultValue) to (adjustment)
- The default value is 1E-5.

## Return Code

A _List of Cursor_ containing elements with loaded element results satisfy the given condition.

## Sample Code

```psj {11,15}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, Max Principal Stress, 2}, {2, 1, 0, 0, 0, 0, \
                             0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                             0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, \
                             0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')

# Create a elemental group whose element results greater than 1 (tolerance=10E-3)
list_element_1= JPT.GetElementResult(JPT.PostDataRangeType.GT,1,10E-3)
Tools.Group.CreateGroup(strGroupName="Group_Element_1", crlTargets=list_element_1)

# Create a elemental group whose element results in range (1,5)
list_element_2= JPT.GetElementResult(JPT.PostDataRangeType.IR,1,5)
Tools.Group.CreateGroup(strGroupName="Group_Element_2", crlTargets=list_element_2)
```
