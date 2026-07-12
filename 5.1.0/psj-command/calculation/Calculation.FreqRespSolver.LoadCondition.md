---
id: Calculation-FreqRespSolver-LoadCondition
title: Calculation.FreqRespSolver.LoadCondition()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set the steady-state excitation input for frequency response (Solver) 
---

## Description

Set the steady-state excitation input for frequency response (Solver).

## Syntax

```psj
Calculation.FreqRespSolver.LoadCondition(...)
```

Macro: [DYNAMIC_FREQ_ANALYSIS_LOAD_SOLVER](../../macro/calculation/DYNAMIC_FREQ_ANALYSIS_LOAD_SOLVER)

Ribbon: <menuselection>Calculation &#187; FreqRespSolver &#187; LoadCondition</menuselection>

## Inputs

### `iAnalysisType`

- An _Integer_ specifying the analysis type.
- The default value is 0.

### `crTargetAnalysis`

- A _Cursor_ specifying the target analysis. A new analysis is created if this parameter is set as None.
- The default value is _None_.

### `crCoordinate`

- A _Cursor_ specifying the output coordinate system.
- The default value is _None_.

### `strName`

- A _String_ specifying the name of load condition to be created.
- The default value is "FRQLOAD".

### `iLoadDirection`

- An _Integer_ specifying the direction of vibration.
- The default value is 0.

### `dlForce`

- A _List of Double_ specifying the vector of vibration force.
- The default value is [1,0,0].

### `dAmplitude`

- A _Double_ specifying the amplitude of vibration force.
- The default value is 1.0.

### `dDelay`

- A _Double_ specifying the value of time delay (seconds).
- The default value is 0.0.

### `dPhase`

- A _Double_ specifying the value of phase delay (angle).
- The default value is 0.0.

### `bBf`

- A _Boolean_ specifying whether to use frequency-dependent load as Table input.
- The default value is _False_.

### `dBf`

- A _Double_ specifying the value of frequency-dependent load (Bf).
- The default value is 1.0.

### `crBfCurve`

- A _Cursor_ specifying the field data of frequency-dependent load.
- The default value is _None_.

### `bFf`

- A _Boolean_ specifying whether to use frequency-dependent phase as Table input.
- The default value is _False_.

### `dFf`

- A _Double_ specifying the value of Frequency-dependent phase.
- The default value is 0.0.

### `crFfCurve`

- A _Cursor_ specifying the field data of frequency-dependent phase.
- The default value is _None_.

### `crlTargets`

- A _List of Cursor_ specifying the selected nodes which can be assigned the load condition.
- The default value is [].

### `iLoadType`

- An _Integer_ specifying the load type.
    - 0: Force
    - 1: Displacement
    - 2: Velocity
    - 3: Acceleration
- The default value is 0.

### `crEdit`

- A _Cursor_ specifying an existing load condition
    - If this parameter is used, the specified load condition will be modified.
    - If it is left None, a new load condition will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created frequency load condition (Solver).

## Sample Code

```psj {6-10}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Command\\PostSample\\freq-solver\\103.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create Frequency Analysis Load - Solver
loadCondition = Calculation.FreqRespSolver.LoadCondition(strName="FRQLoad_1", 
                                                        iLoadDirection=2, 
                                                        dlForce=[0.0, 0.0, 10.0], 
                                                        dAmplitude=10.0, 
                                                        crlTargets=[Node(514)])
JPT.Debugger(loadCondition) # for checking the return value
```
