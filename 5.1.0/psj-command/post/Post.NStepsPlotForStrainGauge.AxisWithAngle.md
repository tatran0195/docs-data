---
id: Post-NStepsPlotForStrainGauge-AxisWithAngle
title: Post.NStepsPlotForStrainGauge.AxisWithAngle()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Display a graph of the stress/strain at the entered rotation angle from the first defined axis on a two-axis plane
---

## Description

Display a graph of the stress/strain at the entered rotation angle from the first defined axis on a two-axis plane.

## Syntax

```psj
Post.NStepsPlotForStrainGauge.AxisWithAngle(...)
```

Macro: [CmdPlotStrainGaugeAxisAngle](../../macro/post/CmdPlotStrainGaugeAxisAngle)

Ribbon: <menuselection>Post &#187; NStepsPlotForStrainGauge &#187; AxisWithAngle</menuselection>

## Inputs

### `crPostJob`

- A _Cursor_ specifying the processing post job.
- This is a required input.

### `listPostStepItem`

- A _List of [POST_STEP_ITEM](../../data-type/psj-command/parameter-types/POST_STEP_ITEM)_ specifying the attributes of each Post Step Item.
- The default value is POST_STEP_ITEM().

### `crlTargets`

- A _List of Cursor_ specifying the selected nodes to get the result and plot chart.
- This is a required input.

### `strXAxisType`

- A _String_ specifying the result type to plot on X-axis.
- This is a required input.

### `strYAxisType`

- A _String_ specifying the result type to plot on Y-axis.
- This is a required input.

### `iFirstAxis`

- An _Integer_ specifying  the first axis from maximum principal stress, minimum principal stress, and middle principal stress.
- The default value is 0.

### `iSecondAxis`

- An _Integer_ specifying the second axis from the minimum principal stress and the middle principal stress.
- The default value is 0.

### `dAngle`

- A _Double_ specifying the value of rotation angle.
- The default value is 0.0.

### `dLength`

- A _Double_ specifying the length of the selection when the node is picked.
- The default value is 0.0.

### `dWidth`

- A _Double_ specifying the width of the selection when the node is picked.
- The default value is 0.0.

### `dAmendFactor`

- A _Double_ specifying the coefficient for correction that is used for strain analysis results.
- The default value is 1.0.

### `iPhaseType`

- An _Integer_ specifying the way to get the phase information when obtaining the strain (stress) in the specified direction for the frequency response result.
    - 0: User Defined
    - 1: Peak (Max)
    - 2: Peak (Min)
- The default value is 0.

### `dPhaseAngle`

- A _Double_ specifying the value of phase angle.
- The default value is 0.0.

### `bCreateMarkup`

- A _Boolean_ specifying whether to markup label for the selected node when plotting graph.
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {6-24}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\111_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# NStepsPlotForStrainGauge > AxisWithAngle
plot = Post.NStepsPlotForStrainGauge.AxisWithAngle(
    crPostJob=TSVPostJob(1), 
    listPostStepItem=[
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=1), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=2), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=3), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=4), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=5), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=6), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=7), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=8), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=9), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=10)], 
    crlTargets=[Node(113, 111)], 
    strXAxisType="Time/Freq(Default)", 
    strYAxisType="Stress(Node)", 
    iSecondAxis=1, 
    dLength=0.002, 
    dWidth=0.001)
JPT.Debugger(plot)
```
