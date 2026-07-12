---
id: Home-ImportMesh-Marc
title: Home.ImportMesh.Marc()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import a Marc file (*.t16, *.t19) to the Jupiter Database (Mesh, boundary conditions, etc.)
---

## Description

Import a Marc file (*.t16, *.t19) to the Jupiter Database (Mesh, boundary conditions, etc.)

## Syntax

```psj
Home.ImportMesh.Marc(...)
```

Macro: [ImportMarcMesh](../../macro/home/ImportMarcMesh)

Ribbon: <menuselection>Home &#187; ImportMesh &#187; Marc</menuselection>

## Inputs

### `strPath`

- A _String_ specifying the Marc file (\*.t16, \*.t19 files) which will be used for importing.
- This is a required input.

## Return Code

A _Boolean_ specifying

## Sample Code

```psj{4}
#Prepare your data
marc_file_path="C:/Temp/sample.t16"

import_status = Home.ImportMesh.Marc(strPath=marc_file_path)
JPT.Debugger(import_status)
```
