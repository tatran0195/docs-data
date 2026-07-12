---
id: Tools-ResultToLoad
title: Tools.ResultToLoad()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Export the selected result name to solver information (as solver keyword card) for the selected entities. Depending on selection of convert load type, the analysis result will be exported to solver card information respectively.
---

## Description

Export the selected result name to solver information (as solver keyword card) for the selected entities. Depending on selection of convert load type, the analysis result will be exported to solver card information respectively.

## Syntax

```psj
Tools.ResultToLoad(...)
```

Macro: [CmdExportLoad](../../macro/tools/CmdExportLoad)

Ribbon: <menuselection>Tools &#187; ResultToLoad</menuselection>

## Inputs

### `crlTargets`

- A _List of Cursor_ specifying the selected entities. The entities can be Part, Face, Node, Element or Group.
- This is a required input.

### `listPostStepItem`

- A _List of [POST_STEP_ITEM](../../data-type/psj-command/parameter-types/POST_STEP_ITEM)_ specifying the attributes of each Post Step Item.
- The default value is POST_STEP_ITEM().

### `vecResultLoad`

- A _Vector of [RESULT_LOAD](../../data-type/psj-command/parameter-types/RESULT_LOAD)_ specifying the components of the selected result.
- The default value is RESULT_LOAD().

### `strExportPath`

- A _String_ specifying the path of file to be exported.
- This is a required input.

### `iSolverType`

- An _Integer_ specifying the solver type.
- The default value is 2 (Nastran).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {25-34}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\Post\\Static_Renkon.op2"
Home.ImportResults.Nastran(strPath= samplePath, dFaceAngle=60.16, dEdgeAngle=60.16, bReadLoadAndConstraint=True, 
                            bReadConnection=True, bCreateResultsAtMidNode=True)
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=1, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Displacement", 
                strResultCompName="Translational", 
                iResultPos=1), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=1))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=1, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))

# Result to load
sampleFile = Tools.ResultToLoad(crlTargets=[Face(10)], 
                                postStepItem=POST_STEP_ITEM(
                                    iAnalysisType=1, 
                                    iResultSet=1, 
                                    iTimeStep=1), 
                                vecResultLoad=[RESULT_LOAD(
                                    iVrType=6, 
                                    strResultName="Displacement", 
                                    strLoadName="Enforced Displacement")], 
                                strExportPath="C:/temp/ResultToLoadFile")
JPT.Debugger(sampleFile)
```
