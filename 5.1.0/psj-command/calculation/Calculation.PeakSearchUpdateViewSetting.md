---
id: Calculation-PeakSearchUpdateViewSetting
title: Calculation.PeakSearchUpdateViewSetting()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Update the view setting of peak search
---

## Description

Update the view setting of peak search.

## Syntax

```psj
Calculation.PeakSearchUpdateViewSetting(...)
```

Macro: 

Ribbon: <menuselection>Calculation &#187; PeakSearchUpdateViewSetting</menuselection>

## Inputs

### `bRangeMax`

- A _Boolean_ specifying whether to display only the notes that are less or equal to the specified value.
- The default value is _False_.

### `bRangeMin`

- A _Boolean_ specifying whether to display only the notes that are greater or equal to the specified value.
- The default value is _False_.

### `bFlagVisibleGroupOnly`

- A _Boolean_ specifying whether to display only peaks on the currently visible part.
- The default value is _False_.

### `bFlagVisibleAreaOnly`

- A _Boolean_ specifying whether to display only peaks within the visible region shown in the result window. Peaks outside the region or on the reverse side are hidden.
- The default value is _False_.

### `bFlagMaxPrincipalStress`

- A _Boolean_ specifying whether to display the maximum principal stress value on the notes.
- The default value is _False_.

### `bFlagMinPrincipalStress`

- A _Boolean_ specifying whether to display the minimum principal stress value on the notes.
- The default value is _False_.

### `bVectorMaxPrincipalStress`

- A _Boolean_ specifying whether to display the maximum principal stress vector.
- The default value is _False_.

### `bVectorMinPrincipalStress`

- A _Boolean_ specifying whether to display the minimum principal stress vector. 
- The default value is _False_.

### `bDisplayPeakNum`

- A _Boolean_ specifying whether to display the number of peaks.
- The default value is _False_.

### `bDisplaySearchOptions`

- A _Boolean_ specifying whether to display the parameters used.
- The default value is _False_.

### `bFlagColor`

- A _Boolean_ specifying whether to change the note color base on the condition.
- The default value is _False_.

### `bRefreshFlag`

- A _Boolean_ specifying whether to refresh the notes. 
- The default value is _False_.

### `dRangeMax`

- A _Double_ specifying the maximum range value.
- The default value is 0.0.

### `dRangeMin`

- A _Double_ specifying the minimum range value.
- The default value is 0.0.

### `iColorType`

- An _Integer_ specifying the method to display the note color.
  - 0: Singular Points
  - 1: Principal Stress
  - 2: User Input
- The default value is 0.

### `colSingular`

- A _Class of [COLOR_SINGULAR](../../data-type/psj-command/parameter-types/COLOR_SINGULAR)_ specifying the color for each load point, constraint point, rigid element connection point, and material boundary point.
- The default value is _COLOR_SINGULAR_.

### `colPrincipal`

- A _Class of [COLOR_PRINCIPAL](../../data-type/psj-command/parameter-types/COLOR_PRINCIPAL)_ specifying note color based on the maximum/minimum principal stress relationship.
- The default value is _COLOR_PRINCIPAL_.

### `colUser`

- A _Class of [COLOR_USER](../../data-type/psj-command/parameter-types/COLOR_USER)_ specifying the user input color.
- The default value is _COLOR_USER_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {30-33}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\Post\\Static_Renkon.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
# Plot the result
Post.ShowContour(
  crPostJob=TSVPostJob(1),
   lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
    iAnalysisType=1, 
    iResultSet=1, 
    iTimeStep=1, 
    strResultName="Stress", 
    strResultCompName="Max Principal Stress", 
    iResultPos=4), 
   postDataOp=PostDataOp(
    iResultLocation=1, 
    iOptionCoord=1, 
    iOptionConversion=1, 
    iOptionContinuous=8))])
Post.ShowDeformation(
  crPostJob=TSVPostJob(1), 
  postResultKey=PostResultKey(
    iAnalysisType=1, 
    iResultSet=1, 
    iTimeStep=1, 
    strResultName="Stress", 
    strResultCompName="Max Principal Stress"))

# Peak search and update view settings
Calculation.PeakSearch(bStep=False, crlTargets=[Part(1)])
view_setting = Calculation.PeakSearchUpdateViewSetting(
  bFlagVisibleAreaOnly=True, 
  bVectorMaxPrincipalStress=True, 
  bFlagColor=True)
print(view_setting)
```
