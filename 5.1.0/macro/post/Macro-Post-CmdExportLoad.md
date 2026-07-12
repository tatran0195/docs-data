---
id: CmdExportLoad
title: CmdExportLoad()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Export Load as file.

## Syntax

```psj
CmdExportLoad(cursor[] taEntity, int analysisType, int resultSet, int timeStep, vecResultLoad [] ResultLoads, int SolverType, string ExportFile)
```

## Inputs

### `1. cursor[] `

Target entity.

### `2. int `

Analysis type.

### `3. int `

Result set. 

### `4. int `

Time step.

### `5. ResultLoad [] `
ResultLoad consisted by:
1. vrType - vr type,
2. string - Result name,
3. string - Load name.

#### `6. int `

Solver type.

#### `7. string `

Exported file name.

## Return Code

Nothing.

## Sample Code

```psj
CmdExportLoad([10:1008], 1,1,1, [[6, Displacement,Initial Displacement]], 2, "C:/Temp/data.dat")
```
