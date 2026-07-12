---
id: Calculation-Gururi-LoadCase
title: Calculation.Gururi.LoadCase()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a load case for Gururi analysis
---

## Description

Create a load case for Gururi analysis.

## Syntax

```psj
Calculation.Gururi.LoadCase(...)
```

Macro: [DYNAMIC_FREQ_ANALYSIS_LOADCASE](../../macro/calculation/DYNAMIC_FREQ_ANALYSIS_LOADCASE)

Ribbon: <menuselection>Calculation &#187; Gururi &#187; LoadCase</menuselection>

## Inputs

### `crTargetAnalysis`

- A _Cursor_ specifying the target analysis to be create a load case. A new analysis is created if this parameter is set as None.
- The default value is _None_.

### `strName`

- A _String_ specifying the name of load case to be created.
- The default value is "LoadCase1".

### `dFactor`

- A _Double_ specifying the load coefficient for the entire load cases to be created.
- The default value is 1.0.

### `iNewID`

- An _Integer_ specifying the ID of the load case to be created.
- The default value is 1.

### `crlSelectedLoad`

- A _List of Cursor_ specifying the selected loads will be used in the load case to be created.
- The default value is [].

### `dlTargetFactor`

- A _List of Double_ specifying the coefficient for each selected load in the corresponding order.
- The default value is [].

### `crEdit`

- A _Cursor_ specifying an existing load case condition
    - If this parameter is used, the specified load case condition will be modified.
    - If it is left None, a new load case condition will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created gururi load case.

## Sample Code

```psj {12-13}
# Please set path to your result sample file
samplePath = "C:/Temp/Sample.op2"

# Prepare result model
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60, dEdgeAngle=60)

# Create a load condition
Calculation.Gururi.LoadCondition(strName="FRQLoad_1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                dAmplitude=10.0, crlTargets=[Node(501)])

# Create a load case
loadCase = Calculation.Gururi.LoadCase(crTargetAnalysis=PostFreqAnalysis(1), strName="LoadCase_1", 
                                        crlSelectedLoad=[PostFreqLoad(1)], dlTargetFactor=[1.0])
JPT.Debugger(loadCase)
```
