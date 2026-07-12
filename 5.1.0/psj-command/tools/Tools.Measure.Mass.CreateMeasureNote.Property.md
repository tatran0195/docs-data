---
id: Tools-Measure-Mass-CreateMeasureNote-Property
title: Tools.Measure.Mass.CreateMeasureNote.Property()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a Measure Note for Measure > Mass > By Property
---

## Description

Create a Measure Note for Measure > Mass > By Property

## Syntax

```psj
Tools.Measure.Mass.CreateMeasureNote.Property(...)
```

Macro: [CreateMeasureNoteMassByProperty]

Ribbon: <menuselection>Tools &#187; Measure &#187; Mass &#187; CreateMeasureNote &#187; Property</menuselection>

## Inputs

### `strNoteName`

- A _String_ specifying the name of the created note.
- This is a required input.

### `crlParts`

- A _List of Cursor_ specifying parts.
- This is a required input.

### `crCoordinate`

- A _Cursor_ specifying local coordinate.
- The default value is _None_.

### `iFontSize`

- An _Integer_ specifying font size.
- The default value is 16.

### `iFontColor`

- An _Integer_ specifying font color.
- The default value is 0.

### `bBold`

- A _Boolean_ specifying bold type or not.
- The default value is _False_.

### `iBackgroundColor`

- An _Integer_ specifying background color.
- The default value is 16777215.

### `iOutlineWidth`

- An _Integer_ specifying outline width.
- The default value is 1.

### `iOutlineColor`

- An _Integer_ specifying outline color.
- The default value is 0.

### `iArrowWidth`

- An _Integer_ specifying arrow width.
- The default value is 1.

### `iArrowColor`

- An _Integer_ specifying arrow color.
- The default value is 0.

### `iArrowType`

- An _Integer_ specifying arrow type.
  - 0: None.
  - 1: Arrow.
- The default value is 1.

### `iTitleType`

- An _Integer_ specifying title type.
  - 0: None.
  - 1: Measure type.
  - 2: Name of note.
- The default value is 1.

## Return Code

A _CursorStr_ specifying created note.

## Sample Code

```psj{40-43}
#Preapre model
Geometry.Part.Cube(ilAxialNodes=[4, 4, 4], iPartColor=14903267)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

Meshing.SolidMeshing(
  crlParts=[Part(1)], 
  bTet10=True,
  dGradingFactor=1.05,
  dStretchLimit=0.1, 
  iSpeedVsQual=1, 
  iRegion=1, 
  bSafeMode=False, 
  iParallel=8, 
  bInternalMeshOnly=False,
  iPartColor=65280)

Properties.Material.Add(
  strMaterialName="Copper_Alloy", 
  dictMaterialProperty={
    'Density': {
      'density': {'DENSITY': [8300.0]}}, 
    'Elastic': {
      'elastic': {
        'YOUNGS_MODULUS': [110000000000.0], 
        'POISSONS_RATIO': [0.34]}}, 
    }, iMaterialID=1, iMaterialColor=7901428)

Properties.Solid(
  crlTargets=[Part(1)], 
  strName="SolidProperty_1",
  iPropertyColor=16131973, 
  crMaterial=Material(1), 
  iCordM=-2, 
  dDynaRemeshVal1=DFLT_DBL, 
  dDynaRemeshVal2=DFLT_DBL, 
  dDispHG=DFLT_DBL, iFLG=-1)

#Create a Measure Note
Tools.Measure.Mass.CreateMeasureNote.Property(
  strNoteName="Mass1", 
  crlParts=[Part(1)])
```
