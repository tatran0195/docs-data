---
id: MeshEdit-Import
title: MeshEdit.Import()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Move nodes deformation
---

## Description

Move nodes deformation

## Syntax

```psj
MeshEdit.Import(iSolverType=0, strFilePath="", iStep=0, dScale=1.0)
```

Ribbon: <menuselection>MeshEdit &#187; Import</menuselection>

## Inputs

### `iSolverType`

- An _Integer_ specifying the solver type.
- The default value is 0.

### `strFilePath`

- A _String_ specifying the file path.
- The default value is "".

### `iStep`

- An _Integer_ specifying the step.
- The default value is 0.

### `dScale`

- A _Double_ specifying the scale.
- The default value is 1.0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.Import(iSolverType=0, strFilePath="", iStep=0, dScale=1.0)
```
