---
id: Properties-Material-Modify
title: Properties.Material.Modify()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Modify an existing material in the User database library by inputting all information of the modifying material
---

## Description

Modify an existing material in the User database library by inputting all information of the modifying material.

## Syntax

```psj
Properties.Material.Modify(...)
```

Ribbon: <menuselection>Properties &#187; Material &#187; Modify</menuselection>

## Inputs

### `iMaterialID`

- A _Integer_ specifying the material identification number (ID).
- This is a required input.

### `dictMaterialProperty`

- A _dictionary_ specifying  _[dictMatProps](../data-type/psj-utility/pre-utility/built-in-types/DMaterial)_.
- This is a required input.
  
### `listMaterialProperty`

- A _List of MATERIAL PROPERTY_ specifying the list of all attributes of property such as _density_, _elasticity_, etc.

:::caution
This input is discarded from V5.1. Please use dictMaterialProperty instead.
:::

## Return Code

A _Boolean_ specifying whether the material is modified or not.

## Sample Code

```psj {13-23}
structure_steel = Properties.Material.Add(
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

mod_mat = Properties.Material.Modify(
    strMaterialName="Structural_Steel", 
    dictMaterialProperty={
        'Density': {'density': {'DENSITY': [9850.0]}}, 
        'Elastic': {'elastic': {'YOUNGS_MODULUS': [200000000000.0], 
        'POISSONS_RATIO': [0.3]}}, 
        'Expansion': {'expansion': {'ALPHA': [1.2e-05]}}, 
        'Conductivity': {'conductivity': {'CONDUCTIVITY': [59.0]}}, 
        'SpecificHeat': {'specificHeat': {'SPECIFIC_HEAT': [461.0]}}}, 
    iMaterialID=5, 
    iMaterialColor=10264731)
JPT.Debugger(mod_mat) #for checking return value
```
