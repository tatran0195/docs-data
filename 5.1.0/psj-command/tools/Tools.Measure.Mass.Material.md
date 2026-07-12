---
id: Tools-Measure-Mass-Material
title: Tools.Measure.Mass.Material()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Measure mass by using the specified material's density
---

## Description

Measure mass by using the specified material's density.

## Syntax

```psj
Tools.Measure.Mass.Material(...)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Mass &#187; Material</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the list of parts to measure the mass. This argurment could be in Part type and/or Bar type. If this parameter is [], `crlMassConditions` must be specified.
  - If the measurement is applied to `crlParts` only, then `crlParts` is a required input.
  - If the measurement is applied to `crlMassConditions` only, then `crlParts` would have the default value is [].

### `crlMassConditions`

- A _List of Cursor_ specifying the list of mass conditions created by _[Connections.MassElements](../connections/Connections.MassElements)_. If this is [], `crlParts` must be specified.
  - If the measurement is applied to `crlMassConditions` only, then `crlMassConditions` is a required input.
  - If the measurement is applied to `crlParts` only, then `crlMassConditions` would have the default value is [].

### `dMaterialDensity`

- A _String_ specifying the material density (default unit: kg/m3).
- This is a required input.

### `strTarget`

- A _String_ specifying the target value of mass information to be outputted. Depending on the target information, this parameter can be one of the following:
  - If _strTarget="Mass"_: Return the mass value.
  - If _strTarget="Gravity Center X"_: Return the X position of Gravity Center.
  - If _strTarget="Gravity Center Y"_: Return the Y position of Gravity Center.
  - If _strTarget="Gravity Center Z"_: Return the Z position of Gravity Center.
  - If _strTarget="Moment Inertial XX"_: Return the Moment of Inertia about X axis.
  - If _strTarget="Moment Inertial YY"_: Return the Moment of Inertia about Y axis.
  - If _strTarget="Moment Inertial ZZ"_: Return the Moment of Inertia about Z axis.
  - If _strTarget="Moment Inertial XY"_: Return the product of Moment of Inertia on XY.
  - If _strTarget="Moment Inertial YZ"_: Return the product of Moment of Inertia on YZ.
  - If _strTarget="Moment Inertial XZ"_: Return the product of Moment of Inertia on XZ.
  - If _strTarget="Principal Moment X"_: Return the Moment of Inertia about Principal axis 11.
  - If _strTarget="Principal Moment Y"_: Return the Moment of Inertia about Principal axis 22.
  - If _strTarget="Principal Moment Z"_: Return the Moment of Inertia about Principal axis 33.
  - If _strTarget="Traits Vector XX"_: Return the X direction of Principal axis 11.
  - If _strTarget="Traits Vector XY"_: Return the Y direction of Principal axis 11.
  - If _strTarget="Traits Vector XZ"_: Return the Z direction of Principal axis 11.
  - If _strTarget="Traits Vector YX"_: Return the X direction of Principal axis 22.
  - If _strTarget="Traits Vector YY"_: Return the Y direction of Principal axis 22.
  - If _strTarget="Traits Vector YZ"_: Return the Z direction of Principal axis 22.
  - If _strTarget="Traits Vector ZX"_: Return the X direction of Principal axis 33.
  - If _strTarget="Traits Vector ZY"_: Return the Y direction of Principal axis 33.
  - If _strTarget="Traits Vector ZZ"_: Return the Z direction of Principal axis 33.
  - If _strTarget="Euler Angle X"_: Return the rotation angle of main axis with X axis.
  - If _strTarget="Euler Angle Y"_: Return the rotation angle of main axis with Y axis.
  - If _strTarget="Euler Angle Z"_: Return the rotation angle of main axis with Z axis.
- The default value is "Mass".

### `bGravityCenter`

- A _Boolean_ specifying the use of gravity center Coordinate System to measure the mass.
  - If _True_, `crCoord` will not be disable. All information will be outputted based on referring to Gravity Center Coordinate System.
  - If _False_, `crCoord` will be defined. All information will be outputted based on referring to Coordinate System that the `crCoord` specified.
- The default value is _False_.

### `crCoord`

- A _Cursor_ specifying the Coordinate System to measure the mass. This parameter cannot be used when `bGravityCenter` is _True_.
- The default value is _None_ (Global Coordinate).

### `iPrecision`

- An _Integer_ specifying the number of digit after floating point. The greater `iPrecision` could be, the more accuracy of mass value can be measured.
- The default value is 6.

## Return Code

A _Double_ specifying the value of Mass information.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

mass = Tools.Measure.Mass.Material(crlParts=[Part(1)], 
                                   dMaterialDensity=2300.0)

JPT.Debugger(mass)
```
