---
id: Calculation-FreqResp-SaveAnalysis
title: Calculation.FreqResp.SaveAnalysis()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Save the results of a frequency response analysis (*.tsdv)
---

## Description

Save the results of a frequency response analysis (*.tsdv).

## Syntax

```psj
Calculation.FreqResp.SaveAnalysis(...)
```

Macro: [CmdSaveOpenTsdv](../../macro/calculation/CmdSaveOpenTsdv)

Ribbon: <menuselection>Calculation &#187; FreqResp &#187; SaveAnalysis</menuselection>

## Inputs

### `strPath`

- A _String_ specifying the path of file to be saved.
- This is a required input.

### `crlTargets`

- A _List of Cursor_ specifying the specified analysis targets to be saved.
- This is a required input.

### `bBdfMode`

- A _Boolean_ specifying whether to use the BDF mode.
- The default value is _False_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {19}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate_eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create a load condition
Calculation.FreqResp.LoadCondition(strName="FRQLoad_1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                    dAmplitude=10.0, crlTargets=[Node(1516)])

# Create a load case
Calculation.FreqResp.LoadCaseCondition(crTargetAnalysis=PostFreqAnalysis(1), strName="LoadCase_1", 
                            crlSelectedLoad=[PostFreqLoad(1)], dlTargetFactor=[1.0])

# Create a response condition
Calculation.FreqResp.ResponseCondition(crTargetAnalysis=PostFreqAnalysis(1), dDampingFactor=0.02, 
                                        dStyleParamMid=10.0, dStyleParamBot=200.0, 
                                        strlResultNames=["TZ"], crlTargets=[Node(1516, 1016)])

# Save analysis (Please set path to your temp folder.)
Calculation.FreqResp.SaveAnalysis(strPath="C:/temp/TransRespAnalysis.tsdv", crlTargets=[PostFreqAnalysis(1)])
```
