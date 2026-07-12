---
id: Home-ExportResultToTXT
title: Home.ExportResultToTXT()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Export the selected result file to text format (*.txt)
---

## Description

Export the selected result file to text format (*.txt).

## Syntax

```psj
Home.ExportResultToTXT(...)
```

Macro: [PostExportToTxt](../../macro/home/PostExportToTxt)

Ribbon: <menuselection>Home &#187; ExportResultToTXT</menuselection>

## Inputs

### `strFileName`

- A _String_ specifying the file path to be exported.
- This is a required input.

### `iSpliterType`

- An _Integer_ specifying the method to delimit output values.
     - 0: Space ( )
     - 1: Comma (,)
     - 2: Semicolon (;)
- The default value is 0.

### `bAppend`

- A _Boolean_ specifying whether to append the results to the specified file.
- The default value is _False_.

### `crlJobs`

- A _List of Cursor_ specifying the post job.
- The default value is [].

### `ilAnalysisTypes`

- A _List of Integer_ specifying the analysis type.
- The default value is [].

### `ilResultSets`

- A _List of Integer_ specifying the result set.
- The default value is [].

### `ilTimeSteps`

- A _List of Integer_ specifying the time step.
- The default value is [].

### `ilResultTypes`

- A _List of Integer_ specifying the result type.
- The default value is [].

### `ilResultPos`

- A _List of Integer_ specifying result position.
- The default value is [].

### `strlResultNames`

- A _List of String_ specifying the result name.
- The default value is [].

### `strlCompNames`

- A _List of String_ specifying the component name.
- The default value is [].

### `strlNames`

- A _List of String_ specifying the result name.
- The default value is [].

### `strlTypes`

- A _List of String_ specifying the result type.
- The default value is [].

### `crlEdit`

- A _List of Cursor_ specifying the edit target.
- The default value is [].

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {6-18}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16) 

# Export result to txt
exportFile = Home.ExportResultToTXT(strFileName="C:/temp/ExportTXT.txt", 
                                    iSpliterType=1, 
                                    crlJobs=[TSVPostJob(1, 1)], 
                                    ilAnalysisTypes=[1, 1], 
                                    ilResultSets=[1, 1], 
                                    ilTimeSteps=[1, 1], 
                                    ilResultTypes=[3, 4], 
                                    ilResultPos=[1, 1], 
                                    strlResultNames=["", ""], 
                                    strlCompNames=["", ""], 
                                    strlNames=["RX", "RY"], 
                                    strlTypes=["TYPE_VIRTUAL_RESULT_ITEM", "TYPE_VIRTUAL_RESULT_ITEM"], 
                                    crlEdit=[Unknown(0, 0)])
JPT.Debugger(exportFile )
```
