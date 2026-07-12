---
id: Analysis-Nastran-ModalTransientResponse
title: Analysis.Nastran.ModalTransientResponse()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Export the input file for Nastran Modal Transient Response Analysis (SOL 112)
---

## Description

Export the input file for Nastran Modal Transient Response Analysis (SOL 112).

## Syntax

```psj
Analysis.Nastran.ModalTransientResponse(...)
```

Ribbon: <menuselection>Analysis &#187; Nastran &#187; Modal Transient Response(SOL 112)</menuselection>

## Inputs

### `strName`

- A _String_ specifying the job name of Nastran analysis.
- The default value is "Job_1".

### `strDescription`

- A _String_ specifying the description of Nastran analysis job.
- The default value is "".

### `crlTargets`

- A _List of Cursor_ specifying the list of target parts.
- The default value is [].

### `nastranAnalysis`

- A _[NASTRAN_ANALYSIS](./../../data-type/psj-command/parameter-types/NASTRAN_ANALYSIS)_ specifying the Nastran analysis input parameter.
- The default value is _[NASTRAN_ANALYSIS](./../../data-type/psj-command/parameter-types/NASTRAN_ANALYSIS)_.

### `bDummyPropAutoAssign`

- A _Boolean_ specifying whether to enable or disable the auto dummy properties creation option.
- The default value is _False_.

### `iDummyPropMaterialID`

- An _Integer_ specifying the material ID which using for dummy property assignment.
- The default value is 0.

### `crEdit`

- A _Cursor_ specifying an existing Nastran job.
  - If this parameter is used, the specified job will be modified.
  - If it is left _None_, a new job will be created.
- The default value is _None_.

### `strPath`

- A _String_ specifying the export path for bdf file.
- The default value is "".

### `iModelCheckAnswer`

- An _Integer_ specifying the model checking option.
  - 0: disable model checking option used for seeking dummy property.
  - 1: enable model checking option used for seeking dummy property.
- The default value is 0.

### `iDeleteSlaveNodesAnswer`

- An _Integer_ specifying the deleting slave nodes option.
  - 0: disable the deleting slave nodes checking option.
  - 1: enable the deleting slave nodes checking option.
- The default value is 0.

## Return Code

A _Cursor_ specifying the newly created or the modified Nastran job.

## Sample Code

```psj {19}
Geometry.Part.Cube()
Meshing.SolidMeshing(crlParts=[Part(1)], bTet10=True, dGradingFactor=1.05,
     dStretchLimit=0.1, iSpeedVsQual=1, iRegion=1, bSafeMode=False,
     iParallel=12, bInternalMeshOnly=False, iPartColor=65280)

Properties.Material.Add("Structural_Steel", [Density([(DENSITY, 7.85e-09)]),
     Elastic([(YOUNGS_MODULUS, 200000.0), (POISSONS_RATIO, 0.3)])])
Properties.Solid(crMaterial=Material(1), dDynaRemeshVal1=DFLT_DBL,
     dDynaRemeshVal2=DFLT_DBL, dDispHG=DFLT_DBL, crlTargets=[Part(1)], iFLG=-1)

BoundaryConditions.FixedConstraint(crlTargets=[Face(25)])
BoundaryConditions.Pressure.General(dPressure=10.0, dlDirection=[0.0, 0.0, -1.0],
     crlTargets=[Face(26)])

nastran_param = NASTRAN_ANALYSIS(iSolverType=1, iGridFormatType=1, dEpsilon=DFLT_DBL,
     iMaxNumOfIter=DFLT_INT, iMemory=DFLT_INT, iNcpu=1, iSolNo=112,
    nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(iTypeStress=0, iTypeStrain=0),
    nastranNonlinear=NASTRAN_NONLINEAR(bUseEPSW=True))
Analysis.Nastran.ModalTransientResponse(nastranAnalysis= nastran_param,strPath="D:/Job_1.bdf")
```
