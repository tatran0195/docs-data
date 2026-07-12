---
id: Properties-ElemRelatedInfo-Bar
title: Properties.ElemRelatedInfo.Bar()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Modify information such as direction vectors and end releases for the selected bar elements or 1D elements contained within the selected edge, individually
---

## Description

Modify information such as direction vectors and end releases for the selected bar elements or 1D elements contained within the selected edge, individually.

## Syntax

```psj
Properties.ElemRelatedInfo.Bar(...)
```

Ribbon: <menuselection>Properties &#187; ElemRelatedInfo &#187; Bar</menuselection>

## Inputs

### `listERIRodData`

- A _List of [ERIBAR_DATA](../../data-type/psj-command/parameter-types/ERIBAR_DATA) class_ specifying the element related information of bar.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {21-34}
Geometry.Part.Cube(iPartColor=6409934)
Properties.Material.Add(
    strMaterialName="Structural_Steel", 
    dictMaterialProperty={
        'Density': {'density': {'DENSITY': [7850.000000000001]}}, 
        'Elastic': {'elastic': {'YOUNGS_MODULUS': [200000000000.0], 
        'POISSONS_RATIO': [0.3]}}, 
        'Expansion': {'expansion': {'ALPHA': [1.2e-05]}}, 
        'Conductivity': {'conductivity': {'CONDUCTIVITY': [59.0]}}, 
        'SpecificHeat': {'specificHeat': {'SPECIFIC_HEAT': [461.0]}}}, 
    iMaterialID=5, 
    iMaterialColor=10264731)
Properties.BAR(
    strName="BAR_1", 
    iPropertyColor=16131973, 
    crMaterial=Material(5), 
    dSectionArea=2e-07, 
    dlSectionOrientation=[0.0, 1.0, 0.0], 
    dlInertiaMoment=[DFLT_DBL, DFLT_DBL, DFLT_DBL], 
    crlTargets=[Elem(88, 87, 89)])
ret = Properties.ElemRelatedInfo.Bar(
    listERIBarData=[
        ERIBAR_DATA(
            iElemId=88, 
            iPropId=1, 
            iEndA=79, 
            iEndB=80, 
            dlOrientVec=[0.0, 0.0, 1.0]), 
        ERIBAR_DATA(
            iElemId=87, 
            iPropId=1, 
            iEndA=78, 
            iEndB=79, 
            dlOrientVec=[0.0, 0.0, 1.0])])
print(ret)
```
