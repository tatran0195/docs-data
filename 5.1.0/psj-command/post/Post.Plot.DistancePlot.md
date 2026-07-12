---
id: Post-Plot-DistancePlot
title: Post.Plot.DistancePlot()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Display the distance between two nodes in multiple steps as a step or time history graph
---

## Description

Display the distance between two nodes in multiple steps as a step or time history graph.

## Syntax

```psj
Post.Plot.DistancePlot(...)
```

Macro: [CmdDistancePlot](../../macro/post/CmdDistancePlot)

Ribbon: <menuselection>Post &#187; Plot &#187; DistancePlot</menuselection>

## Inputs

### `crFirstNode`

- A _Cursor_ specifying the first selected node.
- This is a required input.

### `crSecondNode`

- A _Cursor_ specifying the second selected node.
- This is a required input.

### `listPostStepItem`

- A _List of [POST_STEP_ITEM](../../data-type/psj-command/parameter-types/POST_STEP_ITEM)_ specifying the attributes of each Post Step Item.
- The default value is POST_STEP_ITEM().

### `bDistanceXYZ`

- A _Boolean_ specifying whether to display the distance in X, Y and Z direction when plotting.
- The default value is _False_.

### `bPositionXYZ`

- A _Boolean_ specifying whether to display the coordinate values of the first and second nodes in the X, Y, and Z directions when plotting.
- The default value is _False_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {26-33,37-44}
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
Post.Plot.DistancePlot(crFirstNode=Node(127), crSecondNode=Node(133), 
                        listPostStepItem=[
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=1), 
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=2), 
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=3), 
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=4), 
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=5)], 
                        bDistanceXYZ=True)
JPT.SetActiveDocumentByName("103_solid",1)

# Distance Plot (X,Y,Z Position Plot)
Post.Plot.DistancePlot(crFirstNode=Node(127), crSecondNode=Node(133), 
                        listPostStepItem=[
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=1), 
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=2), 
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=3), 
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=4), 
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=5)], 
                        bPositionXYZ=True)
```
