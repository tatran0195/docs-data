---
id: Test-ZGeometryTest-ShellAssy
title: Test.ZGeometryTest.ShellAssy()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Unknown Description
---

## Description

Unknown Description

## Syntax

```psj
Test.ZGeometryTest.ShellAssy(taPart=[], crlFaces=[], _iMeshType=0, _bSelfIntersection=False, _iMethod=3, _dGapTol=2.1)
```

Ribbon: <menuselection>Test &#187; ZGeometryTest &#187; ShellAssy</menuselection>

## Inputs

### `taPart`

- A _TA_PART_ specifying the part.
- The default value is [].

### `crlFaces`

- A _List of Cursor_ specifying the face.
- The default value is [].

### `_iMeshType`

- A \__I_MESH_TYPE_ specifying the mesh type.
- The default value is 0.

### `_bSelfIntersection`

- A \__B_SELF_INTERSECTION_ specifying the self intersection.
- The default value is False.

### `_iMethod`

- A \__I_METHOD_ specifying the method.
- The default value is 3.

### `_dGapTol`

- A \__D_GAP_TOL_ specifying the gap tolerance.
- The default value is 2.1.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.ZGeometryTest.ShellAssy(taPart=[], crlFaces=[], _iMeshType=0, _bSelfIntersection=False, _iMethod=3, _dGapTol=2.1)
```
