---
id: Properties-ElemRelatedInfo-Shell
title: Properties.ElemRelatedInfo.Shell()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Modify information such as direction vectors and end releases for the selected shell elements or elements contained in a face, individually
---

## Description

Modify information such as direction vectors and end releases for the selected shell elements or elements contained in a face, individually.

## Syntax

```psj
Properties.ElemRelatedInfo.Shell(...)
```

Ribbon: <menuselection>Properties &#187; ElemRelatedInfo &#187; Shell</menuselection>

## Inputs

### `listERIShellData`

- A _List of [ERISHELL_DATA](../../data-type/psj-command/parameter-types/ERISHELL_DATA) class_ specifying the element related information of shell.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {22-31}
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
Properties.Shell(
    crlTargets=[Part(1)], 
    strName="ShellProperty_1", 
    iPropertyId=2, 
    iPropertyColor=3315481, 
    crMatMembrane=Material(5), 
    crMatBend=Material(5), 
    crMatShear=Material(5), 
    dThickness=0.0002)
ret = Properties.ElemRelatedInfo.Shell(
        listERIShellData=[
            ERISHELL_DATA(
                iElemId=117, 
                iPropId=2, 
                dTheta=0.523599), 
            ERISHELL_DATA(
                iElemId=118, 
                iPropId=2, 
                dTheta=0.523599)])
print(ret)
```
