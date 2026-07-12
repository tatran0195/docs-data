---
id: Post-Plot-NStepsPlot
title: Post.Plot.NStepsPlot()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Get results within multiple subcases for a particular node/element/arbitrary point and plot the graph by steps or time history
---

## Description

Get results within multiple subcases for a particular node/element/arbitrary point and plot the graph by steps or time history.

## Syntax

```psj
Post.Plot.NStepsPlot(...)
```

Macro: [CmdNStepPlotNode](../../macro/post/CmdNStepPlotNode),
       [CmdNStepPlotElement](../../macro/post/CmdNStepPlotElement),
       [CmdNStepPlotPoint](../../macro/post/CmdNStepPlotPoint)

Ribbon: <menuselection>Post &#187; Plot &#187; NStepsPlot</menuselection>

## Inputs

### `crPostJob`

- A _Cursor_ specifying the processing post job.
- This is a required input.

### `crlTargets`

- A _List of Cursor_ specifying the selected nodes to plot graph.
- This is a required input.

### `listPostStepItem`

- A _List of [POST_STEP_ITEM](../../data-type/psj-command/parameter-types/POST_STEP_ITEM)_ specifying the attributes of each Post Step Item.
- The default value is POST_STEP_ITEM().

### `bCreateMarkup`

- A _Boolean_ specifying whether to markup label for the selected note when plotting graph.
- The default value is _True_.

### `strXResult`

- A _String_ specifying the result type to display on the X-axis.
- The default value is "".

### `strXComponent`

- A _String_ specifying the direction of the selected result to display on the X-axis.
- The default value is "".

### `iDataLocation`

- An _Integer_ specifying the data location (Node & Element) that the result will display on.
- The default value is 0.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {25-33}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
# Plot the result
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Displacement", 
                strResultCompName="Translational", 
                iResultPos=1), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=4))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))

# Distance Plot (X,Y,Z Distance Plot)
Post.Plot.NStepsPlot(crPostJob=TSVPostJob(1), crlTargets=[Node(133)], listPostStepItem=[
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=1), 
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=2), 
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=3), 
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=4), 
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=5)], 
                    strXResult="Displacement", 
                    strXComponent="Translational", 
                    iDataLocation=1)
```
