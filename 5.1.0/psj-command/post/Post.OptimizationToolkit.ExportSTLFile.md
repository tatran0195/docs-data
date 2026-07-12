---
id: Post-OptimizationToolkit-ExportSTLFile
title: Post.OptimizationToolkit.ExportSTLFile()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Output the currently displayed shape as an .stl file based on density threshold values.
---

## Description

Output the currently displayed shape as an .stl file based on density threshold values.

## Syntax

```psj
Post.OptimizationToolkit.ExportSTLFile(...)
```

Macro: CmdOptimizeOuterShellExport

Ribbon: <menuselection>Post &#187; OptimizationToolkit &#187; ExportSTLFile</menuselection>

## Inputs

### `strSTLPath`

- A _String_ specifying Output path to save the STL file.
- This is a required input.

### `crlBodies`

- A _list of Cursor_ identifying the parts to export.
- This is a required input.

### `dDensityRatio`

- A _Double_ specifying Density Ratio used to filter outer shell geometry. 
- The default value is 0.0.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {20}
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

# Set appropriate density value
Post.OptimizationToolkit.OptimizedShape(dTopologyDensity=0.75)

Post.OptimizationToolkit.ExportSTLFile(strSTLPath="C:/Temp/temp.stl")
```
