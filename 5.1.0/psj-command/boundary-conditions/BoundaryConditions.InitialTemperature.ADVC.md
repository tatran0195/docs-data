---
id: BoundaryConditions-InitialTemperature-ADVC
title: BoundaryConditions.InitialTemperature.ADVC()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Read the temperature result output from format of Adventure Cluster solver and defines it as the initial temperature
---

## Description

Read the temperature result output from format of Adventure Cluster solver and defines it as the initial temperature.

## Syntax

```psj
BoundaryConditions.InitialTemperature.ADVC(...)
```

Ribbon: <menuselection>Boundary Conditions &#187; Initial Temperature &#187; ADVC file</menuselection>

## Inputs

### `strName`

- A _String_ specifying the initial temperature name.
- The default value is "InitialTemperature1".

### `strFilePathName`

- A _String_ specifying the ADVC temperature result file path.
- This is a required input.

### `iLocalTemperatureUnit`

- An _Ingeter_ specifying the local temperature.
- The default value is 0.

### `bUseDefault`

- A _Boolean_ specifying whether enable or disable the default temperature.
- The default value is _False_.

### `crlTargets`

- A _List of Cursor_ specifying list of target part for initial temperature.
- This is a required input.

### `crEdit`

- A _Cursor_ specifying an existing initial temperature.
  - If this parameter is used, the specified initial temperature will be modified.
  - If it is left _None_, a new initial temperature will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {61-66}
import os

temp_folder = os.environ["Temp"] + "/TechnoStar"

if os.path.isdir(temp_folder):
    pass
else:
    os.mkdir(temp_folder)

Geometry.Part.Cube(iPartColor=6473570)
BoundaryConditions.BoundaryTemperature.Constant(dFTemp=293.15, 
                                                crlTargets=[Part(1)])
Properties.Material.Add("Structural_Steel", 
                        [Density([(DENSITY, 
                                   7.85e-09)]), 
                        Elastic([(YOUNGS_MODULUS, 
                                  200000.0), 
                                 (POISSONS_RATIO, 
                                  0.3)])])
Properties.Shell(crlTargets=[Part(1)], 
                 strName="Shell Property 1", 
                 iPropertyColor=16131973, 
                 crMatMembrane=Material(1), 
                 crMatBend=Material(1), 
                 crMatShear=Material(1), 
                 dMatOrient1=DFLT_DBL, 
                 dThickness=0.001, 
                 dBendStiff=DFLT_DBL, 
                 dThickRatio=DFLT_DBL, 
                 dNSM=DFLT_DBL, 
                 dFiberDist1=DFLT_DBL, 
                 dFiberDist2=DFLT_DBL, 
                 dPlateOff=DFLT_DBL, 
                 iItgPts=DFLT_INT)
Analysis.ADVC.MakeProcess.SteadyState(strName="ADVC_DEFAULT_PROCESS", 
                                      advcHeatTimeStep=ADVC_HEAT_TIME_STEP(dMaxdt=1.0, 
                                                                           dMindt=1e-05))
Analysis.ADVC.MakeProcess.SteadyState(strName="ADVC_DEFAULT_PROCESS", 
                                      advcHeatTimeStep=ADVC_HEAT_TIME_STEP(dMaxdt=1.0, 
                                                                           dMindt=1e-05), 
                                      crEdit=ADVCProcessSSH(1), 
                                      listLoadNode=[ADVC_LOAD_NODE(cr=LbcTempBoundary(1))])
Analysis.ADVC.MakeProcess.SteadyState(strName="ADVC_DEFAULT_PROCESS", 
                                      advcHeatTimeStep=ADVC_HEAT_TIME_STEP(dMaxdt=1.0, 
                                                                           dMindt=1e-05), 
                                      crEdit=ADVCProcessSSH(1))
Analysis.ADVC.HeatTransfer(strPath=temp_folder + "/test.adx", 
                           strName="Job_1", 
                           crlProcessSequence=[ADVCProcessSSH(1)], 
                           crlTargets=[Part(1)], 
                           bAutoAssignDummyProp=True, 
                           crDummyPropMaterial=Material(1), 
                           listLoadNodeContact=[], 
                           iUiPrecision=6, 
                           bExportGeometryID=True)

JPT.Exec('New Document()')

Geometry.Part.Cube()

created_bcs = BoundaryConditions.InitialTemperature.ADVC(
    strName="InitialTemperature_1",
    iLocalTemperatureUnit=1, 
    strFilePathName = temp_folder \
                      + "/test.adx", 
    crlTargets=[Part(1)])

JPT.Debugger(created_bcs)
```
