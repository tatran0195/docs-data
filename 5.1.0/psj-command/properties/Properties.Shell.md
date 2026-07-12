---
id: Properties-Shell
title: Properties.Shell()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Assign Shell property to the selected entities
---

## Description

Assign Shell property to the selected entities.

## Syntax

```psj
Properties.Shell(...)
```

Ribbon: <menuselection>Properties &#187; Shell</menuselection>

## Inputs

### `crlTargets`

- A _List of Cursor_ specifying the target to assign the Shell property. The target can be Part, Face, or 2D Element.
- This is a required input.

### `strName`

- A _String_ specifying the property name.
- The default value is "ShellProperty".

### `iPropertyId`

- An _Integer_ specifying the property identification number (ID number).
- The default value is 1.

### `iPropertyColor`

- An _Integer_ specifying the property color.
- The default value is 0.

### `crMatMembrane`

- A _Cursor_ specifying the material for membrane behavior.
- The default value is _None_.

### `crMatBend`

- A _Cursor_ specifying the material for bending behavior.
- The default value is _None_.

### `crMatShear`

- A _Cursor_ specifying the material for lateral shear behavior.
- The default value is _None_.

### `crMatCoupl`

- A _Cursor_ specifying the material for coupled film-bending behavior.
- The default value is _None_.

### `dMatOrient1`

- A _Double_ specifying the theta angle 1 when material orientation is defined by angle.
- The default value is DFLT_DBL.

### `dThickness`

- A _Double_ specifying the thickness of element in millimeters.
- The default value is DFLT_DBL.

### `dBendStiff`

- A _Double_ specifying the bending stiffness parameter.
- The default value is DFLT_DBL.

### `dThickRatio`

- A _Double_ specifying the thickness ratio of the lateral shear stiffness.
- The default value is DFLT_DBL.

### `dNSM`

- A _Double_ specifying the Non-Structural Mass which is a contribution to the model mass from features that have negligible structural stiffness.
- The default value is DFLT_DBL.

### `dFiberDist1`

- A _Double_ specifying the Fiber distances 1 for stress computation from the reference plane.
- The default value is DFLT_DBL.

### `dFiberDist2`

- A _Double_ specifying the Fiber distances 2 for stress computation from the reference plane.
- The default value is DFLT_DBL.

### `dPlateOff`

- A _Double_ specifying the offset value from the reference plane.
- The default value is DFLT_DBL.

### `iItgPts`

- An _Integer_ specifying the integral number of shell elements.
- The default value is DFLT_DBL.

### `iMatOrientType`

- An _Integer_ specifying the material orientation type (Angle - 0 or Coordinate system - 1).
- The default value is 0.

### `crLocalCS`

- A _Cursor_ specifying the Local coordinate system when material orientation is defined by Coordinate system.
  The X axis of the coordinate system is projected to the element plane.
- The default value is _None_.

### `crEdit`

- A _Cursor_ specifying an existing Shell property setting item. 
  - If this parameter is used, the specified Shell property setting item will be modified. 
  - If it is left _None_, a new Shell property setting item will be created.
- The default value is _None_.

### `iDuplicateOpt`

- An _Integer_ specifying the duplicate option. When the property is already assigned to some of the selected bodies 
  - If this value = 6 means the existing property will be changed. 
  - If this value = 2 or 7 means the property will be assigned only to bodies that do not have the property assigned yet.
- The default value is 0.

### `iPanelLabelId`

- An _Integer_ specifying the panel label ID.
- The default value is 1.

### `strPanelLabelName`

- A _String_ specifying the panel label name.
- The default value is ''.

### `iPanelLabelERP`

- An _Integer_ specifying whether to enable the ERP function.
- The default value is 0.

### `iTempVariation`

- An _Integer_ specifying the temperature variation value (Natural numbers only).
- The default value is DFLT_INT.

## Return Code

A _Cursor_ specifying the created shell property.

## Sample Code

```psj {12-18}
Geometry.Part.Cube()
Properties.Material.Add(strMaterialName="Structural_Steel", 
                        dictMaterialProperty={
                          'Density': {'density': {'DENSITY': [7850.000000000001]}}, 
                          'Elastic': {'elastic': {'YOUNGS_MODULUS': [200000000000.0], 
                          'POISSONS_RATIO': [0.3]}}, 
                          'Expansion': {'expansion': {'ALPHA': [1.2e-05]}}, 
                          'Conductivity': {'conductivity': {'CONDUCTIVITY': [59.0]}}, 
                          'SpecificHeat': {'specificHeat': {'SPECIFIC_HEAT': [461.0]}}}, 
                        iMaterialID=5, 
                        iMaterialColor=10264731)
created_prop = Properties.Shell(crlTargets=[Face(26, 24)], 
                              strName="ShellProperty_1", 
                              iPropertyColor=15329791, 
                              crMatMembrane=Material(5), 
                              crMatBend=Material(5), 
                              crMatShear=Material(5), 
                              dThickness=0.01)
JPT.Debugger(created_prop)
```
