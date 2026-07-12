---
id: JPT-GetResultByNodeId
title: JPT.GetResultByNodeId()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get the result value of specified Node by ID
---

## Description

Get the result value of specified Node by ID.
If multiple result data are retrieved (e.g., Mises & Principal), please use JPT.GetAllResultsByNodeId.

## Syntax

```psj
JPT.GetResultByNodeId(nodeID)
```

## Inputs

### `nodeID`

- An _Integer_ specifying the ID of Node to be checked the result value.
- This is a required input.

## Return Code

A _Double_ specifying the result of Node.

## Sample Code

```psj {11}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Displacement, X, 1}, {1, 1, 0, \
                             0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                             {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                             {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')

# Get the result value of Node ID = 62
valueNodeID = JPT.GetResultByNodeId(62)
print("Displacement of X component of Node ID = 62: " + str(valueNodeID))
```
