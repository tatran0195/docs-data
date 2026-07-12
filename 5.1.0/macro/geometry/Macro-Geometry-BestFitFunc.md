---
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
id: BestFitFunc
title: BestFitFunc()
---
## Description

Align the selected parts based on their geometric features.

## Syntax

```psj
BestFitFunc(Cursor[] crlStaticTarget, Cursor[] crlDynamicTarget, Double dError, Int iMaxCycle, int iAlgorithmsType)
```

## Inputs

### `1. Cursor[]`

A _List of Cursor_ specifying the target parts for the move operation.

### `2. Cursor[]`

A _List of Cursor_ specifying the parts to be moved.

### `3. Double`

The total difference in distance between nodes. 

### `4. Int`

The number of iterations for the matrix calculation.

### `5. Int`

The algorithms' type (always set to 0). 

## Return Code 

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BestFitFunc([3:1], [3:2], 1e-08, 400, 0)
```