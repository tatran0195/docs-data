---
id: Properties-Property1DBeamSimple
title: Properties.Property1DBeamSimple()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

## Syntax

```psj
Properties.Property1DBeamSimple(strName, iId, crSection=None, crMat=None, vecOrient=[DFLT_DBL,DFLT_DBL,DFLT_DBL], crlTargets=[], crEdit=None)
```

Macro: [Property1DBeamSimple](../../macro/properties/Property1DBeamSimple)

Ribbon: <menuselection>Properties &#187; Property1DBeamSimple</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name.
- This is a required input.

### `iId`

- An _Integer_ specifying the ID.
- This is a required input.

### `crSection`

- A _Cursor_ specifying the section.
- The default value is None.

### `crMat`

- A _Cursor_ specifying the material.
- The default value is None.

### `vecOrient`

- A _Vector_ specifying the orient.
- The default value is [DFLT_DBL,DFLT_DBL,DFLT_DBL].

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
Properties.Property1DBeamSimple(strName, iId, crSection=None, crMat=None, vecOrient=[DFLT_DBL,DFLT_DBL,DFLT_DBL], crlTargets=[], crEdit=None)
```
