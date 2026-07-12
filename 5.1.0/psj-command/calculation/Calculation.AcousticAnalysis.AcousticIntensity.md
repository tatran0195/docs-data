---
id: Calculation-AcousticAnalysis-AcousticIntensity
title: Calculation.AcousticAnalysis.AcousticIntensity()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create the intensity from the sound pressure and particle velocity results
---

## Description

Create the intensity from the sound pressure and particle velocity results.

## Syntax

```psj
Calculation.AcousticAnalysis.AcousticIntensity(...)
```

Macro: [AcousticIntensity](../../macro/calculation/AcousticIntensity)

Ribbon: <menuselection>Calculation &#187; AcousticAnalysis &#187; AcousticIntensity</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of the target analysis.
- The default value is "".

### `crEdit`

- A _Cursor_ specifying an existing Load condition
    - If this parameter is used, the specified Load condition will be modified.
    - If it is left None, a new Load condition will be created.
- The default value is _None_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {8}
# Please set path to your sample Nastran Vibro-Acoustic file.
filePath="C:/Temp/Sample.op2"

# Prepare result model
Home.ImportResults.Nastran(strPath=filePath, dFaceAngle=60.16, dEdgeAngle=60.16, bIsVibro=True)

# AcousticAnalysis.AcousticIntensity
Calculation.AcousticAnalysis.AcousticIntensity(strName="Subcase 201")
```
