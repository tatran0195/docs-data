---
id: Home-ExportVTFx
title: Home.ExportVTFx()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Export Geometry information or Geometry and Result information for the active document in Web Viewer format(*.vtfx)
---

## Description

Export Geometry information or Geometry and Result information for the active document in Web Viewer format(*.vtfx).

## Syntax

```psj
Home.ExportVTFx(...)
```

Macro: [ExportVTFxFile](../../macro/home/ExportVTFxFile)

Ribbon: <menuselection>Home &#187; ExportVTFx</menuselection>

## Inputs

### `strPath`

- A _String_ specifying the file path to be exported.
- The default value is "".

### `iModelType`

- An _Integer_ specifying the exporting model type.
    - 0: Pre - Export only geometry
    - 1: Post - Export geometry and selected result
- The default value is 1.

### `bExcludeBarPart`

- A _Boolean_ specifying whether to exclude the bar parts when exporting.
- The default value is _False_.

### `bSurfaceElementOnly`

- A _Boolean_ specifying not to export the 3D elements or result on 3D elements.
- The default value is _False_.

### `iData2D`

- An _Integer_ specifying the result position of 2D shell.
    - 0: Top
    - 1: Bottom
    - 3: Average
- The default value is 0.

### `lSelectedResults`

- A _List of [POST_STEP_ITEM](../../data-type/psj-command/parameter-types/POST_STEP_ITEM)_ specifying the information of the selected result.
- The default value is [].

### `bDisplayPostAddTrescaStress`

- A _Boolean_ specifying whether to display post add Tresca stress.
- The default value is _False_.

### `iCurUnitLength`

- An _Integer_ specifying the current unit of length.
- The default value is 0.

### `iCurUnitTime`

- An _Integer_ specifying the current unit of length.
- The default value is 0.

### `iCurUnitMass`

- An _Integer_ specifying the current unit of mass.
- The default value is 0.

### `iCurUnitForce`

- An _Integer_ specifying the current unit of force.
- The default value is 0.

### `iCurUnitAngle`

- An _Integer_ specifying the current unit of angle.
- The default value is 1.

### `iCurUnitTemperature`

- An _Integer_ specifying the current unit of temperature.
- The default value is 1.

### `bSetDefaultResult`

- A _Boolean_ specifying whether to set the default result. 
- The default value is _False_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {6-20}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16) 

# Export VTFx
exportFile = Home.ExportVTFx(strPath="C:/temp/ExportVTFX.vtfx", 
                            iModelType=1, 
                            bExcludeBarPart=True, 
                            iData2D=1, 
                            lSelectedResults=[PostResultKey(
                                iAnalysisType=1, 
                                iResultSet=1, 
                                iTimeStep=1, 
                                iResultType=6, 
                                strResultName="Displacement", 
                                strResultCompName="Translational", 
                                iResultPos=1)], 
                            bDisplayPostAddTrescaStress=True, 
                            iCurUnitAngle=0, 
                            iCurUnitTemperature=0)
JPT.Debugger(exportFile)
```
