---
id: Post-NStepsPlotForStrainGauge-TwoPoints
title: Post.NStepsPlotForStrainGauge.TwoPoints()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Display a graph of the stress/strain in the direction of two points
---

## Description

Display a graph of the stress/strain in the direction of two points.

## Syntax

```psj
Post.NStepsPlotForStrainGauge.TwoPoints(...)
```

Macro: [CmdPlotStrainGaugeNodePoint](../../macro/post/CmdPlotStrainGaugeNodePoint),
       [CmdPlotStrainGauge2Nodes](../../macro/post/CmdPlotStrainGauge2Nodes)

Ribbon: <menuselection>Post &#187; NStepsPlotForStrainGauge &#187; TwoPoints</menuselection>

## Inputs

### `crPostJob`

- A _Cursor_ specifying the processing post job.
- This is a required input.

### `crFirstNode`

- A _Cursor_ specifying the first selected node to get the result and plot chart. This argument can be used for both 2Nodes or Node-Point selection methods.
- This is a required input.

### `crSecondNode`

- A _Cursor_ specifying the second selected node to get the result and plot chart. This argument was used incase of the selection method is 2Nodes.
- This is a required input.

### `dlPosition`

- A _List of Double_ specifying the coordinate of the face point. This argument was used incase of the selection method is Node-Point.
- This is a required input.

### `listPostStepItem`

- A _List of [POST_STEP_ITEM](../../data-type/psj-command/parameter-types/POST_STEP_ITEM)_ specifying the attributes of each Post Step Item.
- The default value is POST_STEP_ITEM().

### `strXAxisType`

- A _String_ specifying the result type to plot on X-axis.
- This is a required input.

### `strYAxisType`

- A _String_ specifying the result type to plot on Y-axis.
- This is a required input.

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

-A _Boolean_ specifying whether to mark up the selected note when plotting graph.
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {27-41,45-59}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Plot the result
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2, 
                iResultSet=1, 
                iTimeStep=2, 
                strResultName="Strain", 
                strResultCompName="Solid Max Principal Strain", 
                iResultPos=4), 
                postDataOp=PostDataOp(iResultLocation=1, 
                iOptionCoord=1, 
                iOptionConversion=1, 
                iOptionContinuous=8))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=2,
                    strResultName="Strain", 
                    strResultCompName="Solid Max Principal Strain"))

# NStepsPlotForStrainGauge > TwoPoints (2Nodes)
plotChart = Post.NStepsPlotForStrainGauge.TwoPoints(
            crPostJob=TSVPostJob(1), 
            crFirstNode=Node(113), 
            crSecondNode=Node(115), 
            listPostStepItem=[
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=1), 
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=2), 
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=3), 
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=4), 
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=5)], 
                strXAxisType="Time/Freq(Default)", 
                strYAxisType="Stress(Node)", 
            dLength=0.002, 
            dWidth=0.005, 
            iPhaseType=-1)
JPT.Debugger(plotChart)

# NStepsPlotForStrainGauge > TwoPoints (Node-Point)
plotChart = Post.NStepsPlotForStrainGauge.TwoPoints(
            crPostJob=TSVPostJob(1), 
            crFirstNode=Node(113), 
            dlPosition=[0.0176052, 0.00855172, 0.00343833], 
            listPostStepItem=[
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=1), 
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=2), 
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=3), 
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=4), 
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=5)], 
                strXAxisType="Time/Freq(Default)", 
                strYAxisType="Stress(Node)", 
            dLength=0.002, 
            dWidth=0.005, 
            iPhaseType=-1)
JPT.Debugger(plotChart)
```
