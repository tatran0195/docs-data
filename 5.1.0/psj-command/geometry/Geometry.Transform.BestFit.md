---
id: Geometry-Transform-BestFit
title: Geometry.Transform.BestFit()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Align the selected parts based on their geometric features.
---

## Description

Align the selected parts based on their geometric features.

## Syntax

```psj
Geometry.Transform.BestFit(...)
```

Macro: BestFitFunc

Ribbon: <menuselection>Geometry &#187; Transform &#187; BestFit</menuselection>

## Inputs

### `crlStaticTarget`

- A _List of Cursor_ specifying the target parts for the move operation.
- This is a required input.

### `crlDynamicTarget`

- A _List of Cursor_ specifying the parts to be moved.
- This is a required input.

### `dError`

- A _Double_ specifying the total difference in distance between nodes. 
- The default value is 0.00000001.

### `iMaxCycle`

- An _Integer_ specifying the number of iterations for the matrix calculation.
- The default value is 400.

### `iAlgorithmsType`

- An _Integer_ specifying the algorithms' type. 
- It is set to 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{10-15}
# Prepare the model
Geometry.Part.Cube(
    dlLength=[0.003, 0.004, 0.005], 
    iPartColor=7463537)

Geometry.Part.Cube(
    dlLength=[0.004, 0.003, 0.005], 
    strName="Cube_2", iPartColor=15658599)

Geometry.Transform.BestFit(
    crlStaticTarget=[Part(1)], 
    crlDynamicTarget=[Part(2)], 
    dError=1e-08, 
    iMaxCycle=400, 
    iAlgorithmsType=0)
```
