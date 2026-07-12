---
id: Properties-Gasket
title: Properties.Gasket()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: create property 3d gasket
---

## Description

Create property 3d gasket

## Syntax

```psj
Properties.Gasket(strName, crMaterial, dThickX, dThickY, dThickZ, crlTargets, crEdit=None, iStData=0, iFLG=0)
```

Macro: [Prop3DGasket](../../macro/properties/Prop3DGasket)

Ribbon: <menuselection>Properties &#187; Gasket</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name.
- This is a required input.

### `crMaterial`

- A _Cursor_ specifying the material.
- This is a required input.

### `dThickX`

- A _Double_ specifying the thickness x.
- This is a required input.

### `dThickY`

- A _Double_ specifying the thickness y.
- This is a required input.

### `dThickZ`

- A _Double_ specifying the thickness z.
- This is a required input.

### `crlTargets`

- A _List of Cursor_ specifying the target.
- This is a required input.

### `crEdit`

- A _Cursor_ specifying the edit.
- The default value is None.

### `iStData`

- An _Integer_ specifying the st data.
- The default value is 0.

### `iFLG`

- An _Integer_ specifying the value FLG.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Gasket(strName, crMaterial, dThickX, dThickY, dThickZ, crlTargets, crEdit=None, iStData=0, iFLG=0)
```
