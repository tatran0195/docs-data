---
id: Analysis-ADVC-MakeProcess-EigenValue
title: Analysis.ADVC.MakeProcess.EigenValue()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a Structure - Eigenvalue analysis as an ADVC process
---

## Description

Create a Structure - Eigenvalue analysis as an ADVC process.

## Syntax

```psj
Analysis.ADVC.MakeProcess.EigenValue(...)
```

Macro: [AdvcEigenProcess](../../macro/analysis/AdvcEigenProcess)

Ribbon: <menuselection>Analysis &#187; ADVC &#187; Structure &#187; EigenValue</menuselection>

## Inputs

### `strName`

- A _String_ specifying the process name of Structure - Eigenvalue analysis.
- This is a required input.

### `bEigenValue`

- A _Boolean_ specifying to be enable/disable the Eigenvalue parameters option.
- The default value is _False_.

### `advcNormalModal`

- A _[ADVC_NORMAL_MODAL](./../../data-type/psj-command/parameter-types/ADVC_NORMAL_MODAL)_ specifying the parameters setting for the Eigenvalue analysis such as Eigen Num of Modes, Eigenvalue Parameter.
- The default value is _[ADVC_NORMAL_MODAL](./../../data-type/psj-command/parameter-types/ADVC_NORMAL_MODAL)_.

### `crEdit`

- A _Cursor_ specifying the ADVC Eigenvalue process in Assembly Tree to modify it. This option uses only for editing process purpose.
- The default value is _None_.

### `listLoadNode`

- A _List of [ADVC_LOAD_NODE](./../../data-type/psj-command/parameter-types/ADVC_LOAD_NODE)_ specifying the load node.
- If this argument is specified, the `listLoadCaseNode` will be empty.
- The default value is [].

### `listLoadCaseNode`

- A _List of [ADVC_LOAD_NODE](./../../data-type/psj-command/parameter-types/ADVC_LOAD_NODE)_ specifying the loadcase node.
- If this argument is specified, the `listLoadNode` will be empty.
- The default value is [].

### `listLoadNodeContact`

- A _List of [ADVC_LOAD_NODE](./../../data-type/psj-command/parameter-types/ADVC_LOAD_NODE)_ specifying the load node contact.
- This argument uses the instance of [ADVC_LOAD_NODE](./../../data-type/psj-command/parameter-types/ADVC_LOAD_NODE) and won't be duplicated with `listLoadNode` or `listLoadCaseNode`
- The default value is [].

### `ilOutputParamList`

- A _List of Integer_ specifying the list of output parameters.
- The default value is [].

### `iRefType`

- An _Integer_ specifying the result reference type.
  - If _iRefType=0_: Temperature Load
  - If _iRefType=1_: Stress
- The default value is 0.

### `strRefPath`

- A _String_ specifying the path of reference result.
- The default value is "".

### `listAdvcRefStressResult`

- A _List of [ADVC_REF_STRESS_RESULT](./../../data-type/psj-command/parameter-types/ADVC_LOAD_NODE)_ specifying the advc reference stress result.
- The default value is [].

## Return Code

A _Cursor_ specifying the created/modified Structure - Eigenvalue analysis as an ADVC process.

## Sample Code

```psj {31}
from os import environ
import re

Geometry.Part.Cube(iPartColor=5619133)
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
                 iPropertyColor=12275404, 
                 crMaterial=Material(1), 
                 iCordM=-2, 
                 dDynaRemeshVal1=DFLT_DBL,
                 dDynaRemeshVal2=DFLT_DBL, 
                 dDispHG=DFLT_DBL, 
                 iFLG=-1)

creating_status = Analysis.ADVC.MakeProcess.EigenValue(strName="Process_0")

JPT.Debugger(creating_status)

Analysis.ADVC.Structure(strPath=environ["Temp"] + \
                                "/TechnoStar/Test.adx", 
                        strName="Job_1", 
                        crlProcessSequence=[ADVCProcessEigen(1)], 
                        crlTargets=[Part(1)], 
                        bAutoAssignDummyProp=True, 
                        crDummyPropMaterial=Material(1), 
                        listLoadNodeContact=[], 
                        iUiPrecision=6, 
                        bExportGeometryID=True)
```
