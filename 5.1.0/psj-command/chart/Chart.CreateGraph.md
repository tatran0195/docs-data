---
id: Chart-CreateGraph
title: Chart.CreateGraph()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Make a graph of post result curve
---

## Description

Make a graph of post result curve.

## Syntax

```psj
Chart.CreateGraph(...)
```

Macro: [PostCreateGraph](../../macro/chart/PostCreateGraph)

Ribbon: <menuselection>Chart &#187; CreateGraph</menuselection>

## Inputs

### `crTargetCurve`

- A _Cursor_ specifying the post result curve.
- The default value is _None_.

### `iNumData`

- An _Integer_ specifying the number of data markers to plot the graph.
- The default value is 0.

### `strLineTitle`

- A _String_ specifying the chart line title.
- The default value is "".

### `dlAxisDataX`

- A _List of Double_ specifying the data value on X-Axis. 
- The default value is [].

### `dlAxisDataY`

- A _List of Double_ specifying the data value on Y-Axis.
- The default value is [].

### `strChartTitle`

- A _String_ specifying the chart title.
- The default value is "".

### `strAxisTitleX`

- A _String_ specifying the X-axis title.
- The default value is "".

### `strAxisTitleY`

- A _String_ specifying the Y-axis title
- The default value is "".

### `bNewChart`

- A _Boolean_ specifying whether to plot graph on a new chart window
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {20-24}
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
respCondition = Calculation.FreqResp.ResponseCondition(crTargetAnalysis=PostFreqAnalysis(1), 
                                                        dDampingFactor=0.02, dStyleParamMid=10.0, 
                                                        dStyleParamBot=200.0, strlResultNames=["TZ"], 
                                                        crlTargets=[Node(1516)])

# Plot chart
newChart = Chart.CreateGraph(crTargetCurve=PostFreqResultCurve(1), 
                            strChartTitle="Frequency Analysis Displacement", 
                            strAxisTitleX="Frequency", 
                            strAxisTitleY="Amplitude", 
                            bNewChart=False)
JPT.Debugger(newChart)
```
