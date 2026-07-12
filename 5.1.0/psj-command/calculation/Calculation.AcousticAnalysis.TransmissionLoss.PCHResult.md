---
id: Calculation-AcousticAnalysis-TransmissionLoss-PCHResult
title: Calculation.AcousticAnalysis.TransmissionLoss.PCHResult()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Read a Punch file (*.pch) containing information on the coupled surfaces output from a Nastran structural-acoustic coupled calculation and create a nodal group on the acoustic model
---

## Description

Read a Punch file (*.pch) containing information on the coupled surfaces output from a Nastran structural-acoustic coupled calculation and create a nodal group on the acoustic model.

## Syntax

```psj
Calculation.AcousticAnalysis.TransmissionLoss.PCHResult(...)
```

Macro: [AcousticTLPCHResult](../../macro/calculation/AcousticTLPCHResult)

Ribbon: <menuselection>Calculation &#187; AcousticAnalysis &#187; TransmissionLoss &#187; PCHResult</menuselection>

## Inputs

### `strPath`

- A _String_ specifying the path of (*.pch) file.
- This is a required input.

## Return Code

A _Cursor_ specifying the created PHC result.

## Sample Code

```psj {9}
# Please set path to your sample Nastran Vibro-Acoustic file and Punch file.
ResultFile="C:/Temp/Sample.op2"
PunchFile="C:/Temp/PunchSample.pch"

# Prepare result model
Home.ImportResults.Nastran(strPath=ResultFile, dFaceAngle=60.16, dEdgeAngle=60.16, bIsVibro=True)

# PCH result
PCHResult = Calculation.AcousticAnalysis.TransmissionLoss.PCHResult(strPath=PunchFile)
JPT.Debugger(PCHResult)
```
