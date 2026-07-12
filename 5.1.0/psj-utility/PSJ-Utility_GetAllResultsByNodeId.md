---
id: JPT-GetAllResultsByNodeId
title: JPT.GetAllResultsByNodeId()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get all result values of specified Node by ID
---

## Description

Get all result values of specified Node by ID.

## Syntax

```psj
JPT.GetAllResultsByNodeId(nodeID)
```

## Inputs

### `nodeID`

- An _Integer_ specifying the ID of Node to be checked the result value.
- This is a required input.

### `bReturnBlank`

- A _Boolean_ specifying the option to express the blank value. 
- The default value is False.


## Return Code

A List specifying all results of Node.

## Sample Code

```psj {11}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XX, 4}, \
                            {1, 1, 0, 0, 16, 0, 0, 0.000000, 0}, 0, \
                            {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, \
                            {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')

# Get the result values of Node ID = 60
valuesNodeID = JPT.GetAllResultsByNodeId(60)
for data in valuesNodeID:
    type, id, value= data
    print(f'Type:{type} ID:{id} Value:{value}')
```
