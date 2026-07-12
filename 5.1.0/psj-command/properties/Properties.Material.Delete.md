---
id: Properties-Material-Delete
title: Properties.Material.Delete()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Delete an existing material in the User database by inputting its ID
---

## Description

Delete an existing material in the User database by inputting its ID.

## Syntax

```psj
Properties.Material.Delete(...)
```

Ribbon: <menuselection>Properties &#187; Material &#187; Delete</menuselection>

## Inputs

### `iMaterialID`

- A _Integer_ specifying the material identification number (ID).
- This is a required input.

## Return Code

A _Boolean_ specifying whether the inputted material is deleted successfully or not.

## Sample Code

```psj {9}
structure_steel = Properties.Material.Add(strMaterialName = "Structural_Steel",
                                          listMaterialProperty = [Density([(DENSITY, 
                                                                            7.85e-09)]),
                                                                  Elastic([(YOUNGS_MODULUS, 
                                                                            200000.0), 
                                                                           (POISSONS_RATIO, 
                                                                            0.3)])])

del_mat = Properties.Material.Delete(1) # 1 is the ID of the created material

JPT.Debugger(del_mat) # For checking return value
```
