---
id: CmdChartSetDBParam
title: CmdChartSetDBParam()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Set dB Param.

## Syntax

```psj
CmdChartSetDBParam(int type, double refValue, double frontParam)
```

## Inputs

### `1. int `

dB Type. 1:dB, 2:SPL.

### `2. double `

Reference Value

### `3. double `

Front Parameter

## Return Code

Nothing.

## Sample Code

```psj
CmdChartSetDBParam(1, 1, 20)
```
