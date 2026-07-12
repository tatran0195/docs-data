---
id: Calculation-PeakSearch
title: Calculation.PeakSearch()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Find peak nodes with higher or lower results (peaked) than nearby vertices at each node in the model and flag them
---

## Description

Find peak nodes with higher or lower results (peaked) than nearby vertices at each node in the model and flag them.

## Syntax

```psj
Calculation.PeakSearch(...)
```

Macro: [CmdPostPeakSearch](../../macro/calculation/CmdPostPeakSearch)

Ribbon: <menuselection>Calculation &#187; PeakSearch</menuselection>

## Inputs

### `crlTargets`

- A _List of Cursor_ specifying the target. The target can be part or face.
- The default value is [].

### `crlExcludedNodes`

- A _List of Cursor_ specifying the excluded nodes.
- The default value is [].

### `iOption`

- An _Integer_ specifying the peak option.
    - 0: Max
    - 1: Min
    - 2: ABS Max
- The default value is 0.

### `dParameter`

- A _Double_ specifying the value for micro peak removal.
- The default value is 0.1.

### `bStep`

- A _Boolean_ specifying whether to use the Step option. 
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the peak nodes.

## Sample Code

```psj {27}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
# Plot the result
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2, 
                iResultSet=1, 
                iTimeStep=2, 
                strResultName="Stress", 
                strResultCompName="Max Principal Stress", 
                iResultPos=4), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=1, 
                iOptionConversion=1, 
                iOptionContinuous=8))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=2, 
                    strResultName="Stress", 
                    strResultCompName="Max Principal Stress"))

# Peak search
peakNodes = Calculation.PeakSearch(bStep=False)
print(peakNodes)
```
