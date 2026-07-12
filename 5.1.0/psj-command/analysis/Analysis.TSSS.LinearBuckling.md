---
id: Analysis-TSSS-LinearBuckling
title: Analysis.TSSS.LinearBuckling()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Export the Input Deck for TechnoStar SunShine Linear Buckling analysis (SOL 105)
---

## Description

Export the Input Deck for TechnoStar SunShine Linear Buckling analysis (SOL 105).

## Syntax

```psj
Analysis.TSSS.LinearBuckling(...)
```

Ribbon: <menuselection>Analysis &#187; SunShine &#187; Linear Buckling(SOL 105)</menuselection>

## Inputs

### `strName`

- A _String_ specifying the job name of TechnoStar SunShine solver. Output set by this name will be saved in the Assembly tree.
- The default value is "Job_1".

### `strDescription`

- A _String_ specifying the description of TechnoStar SunShine solver job.
- The default value is "".

### `crlTargets`

- A _List of Cursor_ specifying the list of target part.
- The default value is [] (all parts in the model).

### `nastranAnalysis`

- A _[NASTRAN_ANALYSIS](./../../data-type/psj-command/parameter-types/NASTRAN_ANALYSIS)_ specifying the TechnoStar Sunshine solver input parameter.
- The default value is _[NASTRAN_ANALYSIS](./../../data-type/psj-command/parameter-types/NASTRAN_ANALYSIS)_.

### `crEdit`

- A _Cursor_ specifying the created TechnoStar SunShine solver job. If this parameter is used, the value will be DynamisJob(_ID_), where _ID_ is the ID of the solver job had been created. If it is left _None_, a new TechnoStar solver job will be created.
- The default value is _None_.

### `strPath`

- A _String_ specifying the export location for bdf file.
- This is a required input.

### `iModelCheckAnswer`

- An _Integer_ specifying the model checking option.
- The default value is 0.

### `iDeleteSlaveNodesAnswer`

- An _Integer_ specifying the deleting slave nodes option.
- The default value is 0.

### `iRigidMethod`

- An _Integer_ specifying export RIGID card.
  
## Return Code

A _Cursor_ specifying the exported job.

## Sample Code

```psj {48-50}
from os import environ
import re

Geometry.Part.Cube()
Meshing.SolidMeshing(crlParts=[Part(1)],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=12,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

Properties.Material.Add("Concrete",
                        [Density([(DENSITY, 2.3e-09)]),
                        Elastic([(YOUNGS_MODULUS, 30000.0),
                                 (POISSONS_RATIO, 0.18)])])

Properties.Solid(crlTargets=[Part(1)],
                 strName="Solid Property 1",
                 iPropertyColor=16131973,
                 crMaterial=Material(1),
                 iCordM=-2,
                 dDynaRemeshVal1=DFLT_DBL,
                 dDynaRemeshVal2=DFLT_DBL,
                 dDispHG=DFLT_DBL,
                 iFLG=-1)

BoundaryConditions.FixedConstraint(crlTargets=[Face(24)])
BoundaryConditions.Pressure.General(dPressure=1000000.0,
                                    crlTargets=[Face(21,
                                                     23)])

input_param = NASTRAN_ANALYSIS(iSolverType=6,
                               iGridFormatType=1,
                               dEpsilon=DFLT_DBL,
                               iMaxNumOfIter=DFLT_INT,
                               iNumberOfThreads=1,
                               iMemory=2,
                               iNcpu=1,
                               iSolNo=105,
                               nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(iTypeStress=0,
                                                                           iTypeStrain=0),
                               nastranNonlinear=NASTRAN_NONLINEAR(bUseEPSW=True))

export_status = Analysis.TSSS.LinearBuckling(nastranAnalysis = input_param,
                                             strPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                                       "/TechnoStar/Test.bdf")

JPT.Debugger(export_status)
```
