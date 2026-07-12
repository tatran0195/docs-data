---
id: Calculation-FFTAnalysis-CopyCondition
title: Calculation.FFTAnalysis.CopyCondition()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a copy of the specified FFT condition 
---

## Description

Create a copy of the specified FFT condition.

## Syntax

```psj
Calculation.FFTAnalysis.CopyCondition(...)
```

Macro: 

Ribbon: <menuselection>Calculation &#187; FFTAnalysis &#187; CopyCondition</menuselection>

## Inputs

### `crPostFFTCondition`

- A _Cursor_ specifying FFT Condition.
- This is a required input.

## Return Code

- A _Boolean_ specifying whether the function succeeded or not.
  - True: Succeeded.
  - False: Failed.

## Sample Code

```psj {5}
# This code needs PostFFTCondition by using 
# Calculation.FFTAnalysis.SetCondition. 
# i.e.
# firstBore=Calculation.FFTAnalysis.SetCondition(...)

Calculation.FFTAnalysis.CopyCondition(crPostFFTCondition=firstBore)
```
