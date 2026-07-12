---
id: Home-ImportMesh-LsDyna
title: Home.ImportMesh.LsDyna()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import a LS-Dyna file (*.k) to the Jupiter Database (Mesh, boundary conditions, etc.)
---

## Description

Import a LS-Dyna file (*.k) to the Jupiter Database (Mesh, boundary conditions, etc.)

## Syntax

```psj
Home.ImportMesh.LsDyna(...)
```

Macro: [ImportLsDyna](../../macro/home/ImportLsDyna)

Ribbon: <menuselection>Home &#187; ImportMesh &#187; LsDyna</menuselection>

## Inputs

### `strlPaths`

- A _List of String_ specifying a list of the LS-Dyna files (\*.k files) which will be used for importing.
- This is a required input.

### `dFaceAngle`

- A _Double_ specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0.

### `dEdgeAngle`

- A _Double_ specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The LS-Dyna file (\*.k file) is imported successfully.
  - False: The LS-Dyna file (\*.k file) cannot be imported.

## Sample Code

```psj {40}
from os import environ

lsdyna_file_path = environ["Temp"] + "/TechnoStar/Exported_LSDyna_File_EXPORT_K.k"

Geometry.Part.Cube()
Meshing.SolidMeshing(crlParts=[Part(1)],
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=12,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

BoundaryConditions.FixedConstraint(crlTargets=[Face(24)])
BoundaryConditions.Pressure.General(dPressure=5000000.0,
                                    crlTargets=[Face(23)])

Properties.Material.Add("Stainless_Steel",
                        [Density([(DENSITY, 7.75e-09)]),
                         Elastic([(YOUNGS_MODULUS, 193000.0),
                                  (POISSONS_RATIO, 0.31)])])
Properties.Solid(crlTargets=[Part(1)],
                 strName="Cube_for_testing",
                 iPropertyColor=16131973,
                 crMaterial=Material(1),
                 iCordM=-2,
                 dDynaRemeshVal1=DFLT_DBL,
                 dDynaRemeshVal2=DFLT_DBL,
                 dDispHG=DFLT_DBL,
                 iFLG=-1)

Analysis.LSDYNAJob()
Analysis.ExportLsdyna(strPath=lsdyna_file_path, 
                    crJob=LSDynaJob(1))


JPT.Exec('New Document()')
import_status = Home.ImportMesh.LsDyna(strlPaths=[lsdyna_file_path])
JPT.Debugger(import_status)
```
