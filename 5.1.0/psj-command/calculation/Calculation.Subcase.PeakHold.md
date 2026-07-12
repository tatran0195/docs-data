---
id: Calculation-Subcase-PeakHold
title: Calculation.Subcase.PeakHold()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a subcase with the maximizes stress, MISES stress, beam MAX, MIN, and AXILAL from two or more selected subcases
---

## Description

Create a subcase with the maximizes stress, MISES stress, beam MAX, MIN, and AXILAL from two or more selected subcases.

## Syntax

```psj
Calculation.Subcase.PeakHold(...)
```

Macro: [PostToolsSubcasePeakHoldEx](../../macro/calculation/PostToolsSubcasePeakHoldEx)

Ribbon: <menuselection>Calculation &#187; Subcase &#187; PeakHoldEX</menuselection>

## Inputs

### `iAnalysisType`

- An _Integer_ specifying the analysis type.
- The default value is 1.

### `bFatigue`

- A _Boolean_ specifying whether to use the fatigue calculation.
- The default value is _False_.

### `dQb`

- A _Double_ specifying the tension strength of the materia
- The default value is 270.0.

### `dQw`

- A _Double_ specifying the material fatigue limit.
- The default value is 130.0.

### `dQy`

- A _Double_ specifying the yield stress of the material.
- The default value is 165.0.

### `strSubcaseName`

- A _String_ specifying the name of new subcase to be created.
- The default value is "Subcase1PeakHold".

### `iSubcaseID`

- An _Integer_ specifying the ID of new subcase to be created.
- The default value is 1.

### `mapPeakHoldSubcases`

- A _Map of [PEAKHOLD_SUBCASE_MAP](../../data-type/psj-command/parameter-types/PEAKHOLD_SUBCASE_MAP)_ specifying the selected subcases to create peakhold results.
- The default value is PEAKHOLD_SUBCASE_MAP().

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {6-10}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Subcase.RelativeOffset
peakHold = Calculation.Subcase.PeakHold(iAnalysisType=2, 
                                        strSubcaseName="Subcase 11 Peak Hold",
                                        iSubcaseID=11, 
                                        mapPeakHoldSubcases=[PEAKHOLD_SUBCASE_MAP(
                                        iResultSet=1, 
                                        listSubcaseIDs=[1, 2, 3, 4, 5])])
JPT.Debugger(peakHold)
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2,
                iAnalysisID=1, 
                iResultSet=11, 
                iTimeStep=11, 
                strResultName="Displacement",
                strResultCompName="Translational", 
                iResultPos=1), 
                postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])
Post.EnableMiddleNodes()
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iAnalysisID=1, 
                    iResultSet=11, 
                    iTimeStep=11, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))
```
