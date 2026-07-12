---
id: Home-ImportMesh-Universal
title: Home.ImportMesh.Universal()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import an Universal file (*.unv) to the Jupiter Database (Mesh, boundary conditions, etc.)
---

## Description

Import an Universal file (\*.unv) to the Jupiter Database (Mesh, boundary conditions, etc.).

## Syntax

```psj
Home.ImportMesh.Universal(...)
```
Macro: [ImportUnv](../../macro/home/ImportUnv), [ImportUniversalMesh](../../macro/home/ImportUniversalMesh)
 
Ribbon: <menuselection>Home &#187; ImportMesh &#187; Universal</menuselection>


## Inputs

### `strlPaths`

- A _List of String_ specifying a list of the Universal files (\*.unv file) which will be used for importing.
- This is a required input.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Universal file (\*.unv file) is imported successfully.
  - False: The Universal file (\*.unv file) cannot be imported.

## Sample Code

```psj {19}
from os import environ

unv_file_path = environ["Temp"] + "/TechnoStar/Exported_Universal_File_EXPORT_unv.bdf"

Geometry.Part.Cube(ilAxialNodes=[3, 3, 3])
Meshing.SolidMeshing(crlParts=[Part(1)], bTet10=True, 
                    dGradingFactor=1.0, 
                    dStretchLimit=0.1, 
                    iSpeedVsQual=1, 
                    bSafeMode=False, 
                    iParallel=8, 
                    bInternalMeshOnly=False, 
                    iPartColor=65280)

Home.EXPORT_UNIVERSAL(strFileName=unv_file_path, crlParts=[Part(1)])

JPT.CreateNewDocument()

import_status = Home.ImportMesh.Universal(strlPaths=[unv_file_path])

JPT.Debugger(import_status)
```
