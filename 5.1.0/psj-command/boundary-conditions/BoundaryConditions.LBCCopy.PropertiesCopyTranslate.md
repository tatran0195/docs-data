---
id: BoundaryConditions-LBCCopy-PropertiesCopyTranslate
title: BoundaryConditions.LBCCopy.PropertiesCopyTranslate()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Copy a property translate
---

## Description

Copy a property translate.

## Syntax

```psj
BoundaryConditions.LBCCopy.PropertiesCopyTranslate(...)
```

Ribbon: <menuselection>BoundaryConditions &#187; LBCCopy &#187; PropertiesCopyTranslate</menuselection>

## Inputs

### `iMethod`

- An _Integer_ specifying the method.
- The default value is 0.

### `iMatchMethod`

- An _Integer_ specifying the match method.
- The default value is 0.

### `posVecTrans`

- A _Position_ specifying the vector trans.
- The default value is [0,0,0].

### `dMagnitude`

- A _Double_ specifying the magnitude.
- The default value is 1.

### `dTrandataDoffset`

- A _Double_ specifying the trandata offset.
- The default value is 0.0.

### `dTol`

- A _Double_ specifying the tolerance.
- The default value is 1.

### `crCoord`

- A _Cursor_ specifying the coordinate.
- The default value is None.

### `crlTargets`

- A _List of Cursor_ specifying the target.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopy.PropertiesCopyTranslate(iMethod=0, iMatchMethod=0, posVecTrans=[0,0,0], dMagnitude=1, dTrandataDoffset=0.0, dTol=1, crCoord=None, crlTargets=[])
```
