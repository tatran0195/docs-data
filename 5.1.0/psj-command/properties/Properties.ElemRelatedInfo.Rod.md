---
id: Properties-ElemRelatedInfo-Rod
title: Properties.ElemRelatedInfo.Rod()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Modify information such as direction vectors and end releases for the selected rod elements, individually
---

## Description

Modify information such as direction vectors and end releases for the selected rod elements, individually.

## Syntax

```psj
Properties.ElemRelatedInfo.Rod(...)
```

Ribbon: <menuselection>Properties &#187; ElemRelatedInfo &#187; Rod</menuselection>

## Inputs

### `listERIRodData`

- A _List of [ERIROD_DATA](../../data-type/psj-command/parameter-types/ERIROD_DATA) class_ specifying the element related information of rod.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {19-25}
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
Properties.Rod(
    strName="ROD_1", 
    iPropertyColor=3742001, 
    crMat=Material(5), 
    dArea=2e-07, 
    crlTargets=[Elem(89, 88, 87)])
ret = Properties.ElemRelatedInfo.Rod(
        listERIRodData=[
            ERIROD_DATA(
                iElemId=87, 
                iPropId=1, 
                iEndA=79, 
                iEndB=78)])
print(ret)
```
