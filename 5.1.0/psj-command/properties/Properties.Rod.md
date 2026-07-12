---
id: Properties-Rod
title: Properties.Rod()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: create 1D rod property
---

## Description

Create 1D rod property

## Syntax

```psj
Properties.Rod(strName="", iPID=1, crSection=None, crMat=None, dArea=DFLT_DBL, dTorConst=DFLT_DBL, dTorStressCoeff=DFLT_DBL, dNSM=DFLT_DBL, iLocalLengthUnit=0, iLocalMassUnit=0, crlTargets=[], crEdit=None)
```

Macro: [Property1DRod](../../macro/properties/Property1DRod)

Ribbon: <menuselection>Properties &#187; Rod</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name.
- The default value is "".

### `iPID`

- An _Integer_ specifying the ID.
- The default value is 1.

### `crSection`

- A _Cursor_ specifying the section.
- The default value is None.

### `crMat`

- A _Cursor_ specifying the material.
- The default value is None.

### `dArea`

- A _Double_ specifying the area.
- The default value is DFLT_DBL.

### `dTorConst`

- A _Double_ specifying the tor const.
- The default value is DFLT_DBL.

### `dTorStressCoeff`

- A _Double_ specifying the tor stress coeff.
- The default value is DFLT_DBL.

### `dNSM`

- A _Double_ specifying the n s m.
- The default value is DFLT_DBL.

### `iLocalLengthUnit`

- An _Integer_ specifying the local length unit.
- The default value is 0.

### `iLocalMassUnit`

- An _Integer_ specifying the local mass unit.
- The default value is 0.

### `crlTargets`

- A _List of Cursor_ specifying the target.
- The default value is [].

### `crEdit`

- A _Cursor_ specifying the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Rod(strName="", iPID=1, crSection=None, crMat=None, dArea=DFLT_DBL, dTorConst=DFLT_DBL, dTorStressCoeff=DFLT_DBL, dNSM=DFLT_DBL, iLocalLengthUnit=0, iLocalMassUnit=0, crlTargets=[], crEdit=None)
```
