---
id: Calculation-StressRecovery
title: Calculation.StressRecovery()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Recover stresses (strain) in arbitrary elements from the calculation results of RecurDyn
---

## Description

Recover stress (strain) in arbitrary elements from the calculation results of RecurDyn. 

## Syntax

```psj
Calculation.StressRecovery(...)
```

Macro: 

Ribbon: <menuselection>Post &#187; Calculation &#187; StressRecovery</menuselection>

## Inputs

### `crlTargets`

- A _List of Cursor_ specifying the target. The target can be Part, Face or Group
- This is a required input.

### `strMDFFilePath`

- A _String_ specifying the MDF file path.
- The default value is ''.

### `iNodalDisplacement`

- An _Integer_ specifying nodal displacement recovery.
  -  0: No nodal displacement recovery.
  -  1: All nodal displacements recovery.
- The default value is 1.

### `iElementStress`

- An _Integer_ specifying element stress recovery.
  - 0: No element stress recovery.
  - 1: Specify the element stress for the selected area. 
- The default value is 1.

### `iElementStrain`

- An _Integer_ specifying element strain recovery.
  - 0: No element strain recovery.
  - 1: Specify element strain fort the selected area.
- The default value is 0.

### `iTargetElement`

- An _Integer_ specifying whether to recover stress only for elements on the free faces or for all elements in case a solid element part is selected.
  - 0: Recover stress for elements on free faces only.
  - 1: Recover stress for all elements.
- The default value is 0.

### `dlStep`

- A _List of Double_ specifying the start-end time step.
- The default value is [].

### `bRunSunShine`

- A _Boolean_ specifying whether to run the stress recovery calculation by SunShine-Solver.
- The default value is _True_.

### `bImportOP2`

- A _Boolean_ specifying whether to read additional Op2 of the stress recovery results.
- The default value is _True_.

### `strSunShinePath`

- A _String_ specifying the path of SunShine-Solver.
- The default value is _[JPT.GetProgramPath()+"SunShine/tss.bat"]_.

:::note
When creating a FEM reduced model using the mode synthesis method, be sure to use the same version of SunShine as the one used for stress recovery. If the versions do not match, an error may occur during stress recovery. Even if stress results are obtained, they may not be correct.
:::

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {13-17}
# Please prepare the result files with a compatible version of Sunshine.
op2_path = ".../StressRecovery.op2"
mdf_path = ".../StressRecovery.mdf"
sunshine_path = ".../tss.bat"
# Import result model
Home.ImportResults.Nastran(
  strPath=op2_path, 
  bReadLoadAndConstraint=True, 
  bReadConnection=True, 
  bCreateResultsAtMidNode=True)

# Durability > Stress Recovery
stress_recovery = Calculation.StressRecovery(
  crlTargets=[Part(3, 2)], 
  strMDFFilePath=mdf_path, 
  dlStep=[(0.138889, 2.36111), (7.91667, 10.1389)], 
  strSunShinePath=sunshine_path)
print(stress_recovery)
```
