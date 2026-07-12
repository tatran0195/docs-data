---
id: Home-ExportPV
title: Home.ExportPV()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Export PV File
---

## Description

Export PV File

## Syntax

```psj
Home.ExportPV(...)
```

Macro: [Export_Post_Viewer_File](../../macro/home/Export_Post_Viewer_File)

Ribbon: <menuselection>Home &#187; ExportPV</menuselection>

## Inputs

### `iGroupType`

- An _Integer_ specifying the group type. 
- The default value is 0.

### `strFileName`

- A _String_ specifying the file.
- The default value is "".

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code
```psj
import os

program_path=JPT.GetAppPathInfo(JPT.PathType.PROGRAM_PATH)
temp_path=JPT.GetAppPathInfo(JPT.PathType.TEMP_PATH)

Home.ImportResults.Nastran(
    strPath=os.path.join(
        program_path, 
        'SampleData/PSJ/PSJ-Utility/PostSample/101_solid.op2')
)

Groups.RightClick.PropertyGroup()

Home.ExportGeometrySurface(strFolderName=temp_path)
Post.ShowContour(
    crPostJob=TSVPostJob(1), 
    lContourSettings=[
        PostContourSetting(
            postResultKey=PostResultKey(
                iAnalysisType=1, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Stress", 
                strResultCompName="Mises", 
                iResultPos=4), 
        postDataOp=PostDataOp(
            iResultLocation=1, 
            iOptionConversion=1, 
            iOptionContinuous=8)
        )
    ]
)

Post.ShowDeformation(
        crPostJob=TSVPostJob(1), 
        postResultKey=PostResultKey(
            iAnalysisType=1, 
            iResultSet=1, 
            iTimeStep=1, 
            strResultName="Stress", 
            strResultCompName="Mises"))

Home.ExportPV(
    iGroupType=3, 
    strFileName=os.path.join(temp_path,'pv_test.tspv')
)
```
