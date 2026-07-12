---
id: MuxWeld-Prop3DWeldBead
title: MuxWeld.Prop3DWeldBead()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: create Property 3D Weld Bead
---

## Description

Create Property 3D Weld Bead

## Syntax

```psj
MuxWeld.Prop3DWeldBead(strName="Bead_1", crMaterial=None, crlTargets=[], crEdit=None)
```

Ribbon: <menuselection>MuxWeld &#187; Prop3DWeldBead</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name.
- The default value is "Bead_1".

### `crMaterial`

- A _Cursor_ specifying the material.
- The default value is None.

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
MuxWeld.Prop3DWeldBead(strName="Bead_1", crMaterial=None, crlTargets=[], crEdit=None)
```
