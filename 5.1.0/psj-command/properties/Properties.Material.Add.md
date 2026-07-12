---
id: Properties-Material-Add
title: Properties.Material.Add()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a new material to the current User database library
---

## Description

Create a new material to the current User database library.

> This command is not compatible with V5.0 series. If you wish to use scripts currently running on V5.0.1-V5.0.4 with V5.1, please modify your scripts accordingly.



## Syntax

```psj
Properties.Material.Add(...)
```

Ribbon: <menuselection>Properties &#187; Material &#187; Add</menuselection>

## Inputs

### `strMaterialName`

- A _String_ specifying the material name.
- This is a required input.

### `dictMaterialProperty`

- A _dictionary_ specifying  _[dictMatProps](../../data-type/psj-utility/pre-utility/built-in-types/DMaterial)_.
- This is a required input.

### `listMaterialProperty`

- A _[List of MATERIAL PROPERTY](./../../data-type/psj-command/material-property/structure/Density)_ specifying all attributes of property such as _density_, _elasticity_, etc.

:::caution
This input is discarded from V5.1. Please use dictMaterialProperty instead.
:::

### `iMaterialID`

- An _Integer_ specifying the _NasID_ of material to be added.
- The _NasID_ can be referred in \*.mlib material library file.
- This is a required input.

### `iMaterialColor`

- An _Integer_ specifying the ID of color .
- The default value is 0.

### `strDescription`

- A _String_ specifying the description of material.
- The default value is "".

## Return Code

A _Cursor_ specifying the new material created.

## Sample Code

```psj {30-34}
#Prepare material with unit
dict_mat_prop = {
    'Density': {
        'density': {
            'DENSITY': [8.3e-9],
        },
    },
    'Elastic': {
        'elastic': {
            'POISSONS_RATIO': [0.3],
            'YOUNGS_MODULUS': [1.1e+5],
            'SHEAR_MODULUS': [5.2e+3],
        }
    },
    'Unit': {
        'Density': {
            'density': {  
                'DENSITY': JPT.DensityUnit.Density_t_mm3
            }
        },
        'Elastic': {
            'elastic': {  
                'YOUNGS_MODULUS': JPT.ModulusUnit.Modulus_N_mm2
            }
        }
    }
}

#Add new material to document
new_material=Properties.Material.Add(
    strMaterialName="NewMaterial", 
    dictMaterialProperty=dict_mat_prop,
    iMaterialID=1, 
    iMaterialColor=9614382)

JPT.Debugger(new_material) #for checking return value
```
