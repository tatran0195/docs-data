---
id: Post-OptimizationToolkit-EnableOptimizationMode
title: Post.OptimizationToolkit.EnableOptimizationMode()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Enable the shape display function based on nodal density ratio or density ratio.
---

## Description

Enable the shape display function based on nodal density ratio or density ratio.

## Syntax

```psj
Post.OptimizationToolkit.EnableOptimizationMode(...)
```

Macro: EnableOptimizationRenderMode

Ribbon: <menuselection>Post &#187; OptimizationToolkit &#187; EnableOptimizationMode</menuselection>

## Inputs

### `bOptimizationMode`

- A _Boolean_ specifying whether or not enables optimization mode.
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {16}
# Import arbitrary topology optimization result
Home.ImportResults.ADVC("C:/Temp/ADVCResult", iImportType=1)

Post.ShowContour(
    crPostJob=TSVPostJob(1), 
    lContourSettings=[
        PostContourSetting(postResultKey=PostResultKey(
            iAnalysisType=11, 
            iResultSet=10, 
            iTimeStep=-1, 
            strResultName="DensityRatio", 
            strResultCompName="DensityRatio", 
            iResultPos=2), 
        postDataOp=PostDataOp(iResultLocation=2, iOptionCoord=1))])

Post.OptimizationToolkit.EnableOptimizationMode()

Post.OptimizationToolkit.OptimizedShape(dTopologyDensity=0.75)
```

