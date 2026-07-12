---
id: Post-UnloadContour
title: Post.UnloadContour()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Unload result from current model.
---

## Description

Unload result from current model.

## Syntax

```psj
Post.UnloadContour(...)
```

Macro: ShowContour()

Ribbon: <menuselection>Post &#187; UnloadContour</menuselection>

## Inputs

This utility function does not require any input value.

## Return Code

True if success, or False if failed.

## Sample Code

```psj {26}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath)

# Load result
Post.ShowContour(
    crPostJob=TSVPostJob(1), 
    lContourSettings=[
        PostContourSetting(
            postResultKey=PostResultKey(
                iAnalysisType=1, iResultSet=1, iTimeStep=1, strResultName="Displacement", 
                strResultCompName="Translational", iResultPos=1), 
                postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])

Post.ShowDeformation(
    crPostJob=TSVPostJob(1), 
    postResultKey=PostResultKey(
        iAnalysisType=1, 
        iResultSet=1, 
        iTimeStep=1, 
        strResultName="Displacement", 
        strResultCompName="Translational"))
Post.EnableMiddleNodes()

# Unload result
Post.UnloadContour()
```
