---
id: Home-ExportGeometrySurface
title: Home.ExportGeometrySurface()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Export the file in Geometry Surface for Post format (*.stl)
---

## Description

Export the file in Geometry Surface for Post format (*.stl)

## Syntax

```psj
Home.ExportGeometrySurface(...)
```

Macro: [PostExportGeom](../../macro/home/PostExportGeom)

Ribbon: <menuselection>Home &#187; ExportGeometrySurface</menuselection>

## Inputs

### `strFolderName`

- A _String_ specifying the path of folder.
- This is a required input.

### `bUseUnit`

- A _Boolean_ specifying whether to use unit when exporting.
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {6}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16) 

# Export Geometry Surface for Post
exportFile = Home.ExportGeometrySurface(strFolderName="C:\\temp")
JPT.Debugger(exportFile)
```
