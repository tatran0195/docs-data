---
id: ImportMarcMesh
title: ImportMarcMesh()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Import a Marc file (.t16, .t19) to the Jupiter Database (Mesh, boundary conditions, etc.)

## Syntax

```psj
ImportMarcMesh(str strPath, double dFaceAngle, double dEdgeAngle)
```

## Inputs

### `1. str`

- A String specifying the Marc file (*.t16, *.t19 files) which will be used for importing.

### `2. double`

- A double specifying face angle.


### `3. double`

- A double specifying edge angle.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportMarcMesh("path/to/the/file", 60.0, 60.0)
```