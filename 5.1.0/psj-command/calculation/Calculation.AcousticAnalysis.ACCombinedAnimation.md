---
id: Calculation-AcousticAnalysis-ACCombinedAnimation
title: Calculation.AcousticAnalysis.ACCombinedAnimation()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Perform the animation with physical quantities that select deformation, contour color, and vector separately
---

## Description

Perform the animation with physical quantities that select deformation, contour color, and vector separately.

## Syntax

```psj
Calculation.AcousticAnalysis.ACCombinedAnimation(...)
```

Macro: [ACCombinedAnimation](../../macro/calculation/ACCombinedAnimation)

Ribbon: <menuselection>Calculation &#187; AcousticAnalysis &#187; ACCombinedAnimation</menuselection>

## Inputs

### `iTimeStep`

- An _Integer_ specifying the time step.
- The default value is 1.

### `iAnalysisType`

- An _Integer_ specifying the analysis type.
- The default value is 1.

### `strName`

- A _String_ specifying the subcase name.
- The default value is "FluidPressure".

### `bDeformation`

- A _Boolean_ specifying whether to use the deformation result.
- The default value is _True_.

### `bContour`

- A _Boolean_ specifying whether to display the contour.
- The default value is _True_.

### `bVector`

- A _Boolean_ specifying whether to display the vector.
- The default value is _True_.

### `iContour`

- An _Integer_ specifying the contour option.
    - 0: Fluid Pressure
    - 1: Acoustic Intensity Normal
- The default value is 0.

### `iVector`

- An _Integer_ specifying the vector option.
    - 0: Fluid Velocity
    - 1: Instantaneous Intensity
- The default value is 0.

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

# AcousticAnalysis.ACCombinedAnimation
Calculation.AcousticAnalysis.ACCombinedAnimation(iTimeStep=2, iAnalysisType=4, strName="Subcase 201")
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=4, 
                iResultSet=201, 
                iTimeStep=2, 
                strResultName="Fluid Pressure", 
                strResultCompName="P", 
                iResultPos=1), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=1, 
                iOptionComplex=16))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=4, 
                    iResultSet=201, 
                    iTimeStep=2, 
                    strResultName="Fluid Pressure", 
                    strResultCompName="P"), 
                    postDataOption=PostDataOp(iOptionComplex=16))
```
