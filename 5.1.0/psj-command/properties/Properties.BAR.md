---
id: Properties-BAR
title: Properties.BAR()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Apply bar property on the selected entities
---

## Description

Apply bar property on the selected entities.

## Syntax

```psj
Properties.BAR(...)
```

Macro: [Property1DBar](../../macro/properties/Property1DBar)

Ribbon: <menuselection>Properties &#187; BAR</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of the new property.
- The default value is "".

### `iPropertyId`

- An _Integer_ specifying the identify number of the created property.
- The default value is 1.

### `iPropertyColor`

- An _Integer_ specifying the color of the created property.

### `crCrossSection`

- A _Cursor_ specifying the cross-sectional in the library. The _crCrossSection_ and _iShapeDataType_ arguments are mutually exclusive. One of them must be specified.
- The default value is _None_.

### `iShapeDataType`

- An _Integer_ specifying the shape type from the default list. The _crCrossSection_ and _iShapeDataType_ arguments are mutually exclusive. One of them must be specified.
- The default value is 0.

### `crMaterial`

- A _Cursor_ specifying the material will be applied for Bar property.
- The default value is _None_.

### `dSectionArea`

- A _Double_ specifying the area of bar cross-section. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dlSectionOrientation`

- A _List of Double_ specifying the orientation of bar cross-section.
- This is a required input.

### `dlInertiaMoment`

- A _List of Double_ specifying the three components area moments of inertia, expressed in the principal axis of the bar. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is [0.0,0.0,0.0].

### `dDatadTorConst`

- A _Double_ specifying the torsion constant which is involved in the relationship between angle of twist and applied torque along the axis of the bar. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dDatadNSM`

- A _Double_ specifying the nonstructural mass per unit length which is a contribution to the model mass from features that have negligible structural stiffness. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dDataShearAreaFactor0`

- A _Double_ specifying the area factor for shear for plane 1. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dDataShearAreaFactor1`

- A _Double_ specifying the the area factor for shear for plane 2. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dDataStressRecoveryCoeff0`

- A _Double_ specifying the stress recovery coefficients at the y-coordinate in the BAR element coordinate system of point C at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dDataStressRecoveryCoeff1`

- A _Double_ specifying the stress recovery coefficients at the z-coordinate in the BAR element coordinate system of point C at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dDataStressRecoveryCoeff2`

- A _Double_ specifying the stress recovery coefficients at the y-coordinate in the BAR element coordinate system of point D at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dDataStressRecoveryCoeff3`

- A _Double_ specifying the stress recovery coefficients at the z-coordinate in the BAR element coordinate system of point D at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dDataStressRecoveryCoeff4`

- A _Double_ specifying the stress recovery coefficients at the y-coordinate in the BAR element coordinate system of point E at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dDataStressRecoveryCoeff5`

- A _Double_ specifying the stress recovery coefficients at the z-coordinate in the BAR element coordinate system of point E at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dDataStressRecoveryCoeff6`

- A _Double_ specifying the stress recovery coefficients at the y-coordinate in the BAR element coordinate system of point F at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dDataStressRecoveryCoeff7`

- A _Double_ specifying the stress recovery coefficients at the z-coordinate in the BAR element coordinate system of point F at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `bDataPinA0`

- A _Boolean_ specifying whether to remove the connection between the grid point and the translation UX of the bar at end A.
- The default value is _False_.

### `bDataPinA1`

- A _Boolean_ specifying whether to remove the connection between the grid point and the translation UY of the bar at end A.
- The default value is _False_.

### `bDataPinA2`

- A _Boolean_ specifying whether to remove the connection between the grid point and the translation UZ of the bar at end A.
- The default value is _False_.

### `bDataPinA3`

- A _Boolean_ specifying whether to remove the connection between the grid point and the rotation RX of the bar at end A.
- The default value is _False_.

### `bDataPinA4`

- A _Boolean_ specifying whether to remove the connection between the grid point and the rotation RY of the bar at end A.
- The default value is _False_.

### `bDataPinA5`

- A _Boolean_ specifying whether to remove the connection between the grid point and the rotation RZ of the bar at end A.
- The default value is _False_.

### `bDataPinB0`

- A _Boolean_ specifying whether to remove the connection between the grid point and the translation UX of the bar at end B.
- The default value is _False_.

### `bDataPinB1`

- A _Boolean_ specifying whether to remove the connection between the grid point and the translation UY of the bar at end B.
- The default value is _False_.

### `bDataPinB2`

- A _Boolean_ specifying whether to remove the connection between the grid point and the translation UZ of the bar at end B.
- The default value is _False_.

### `bDataPinB3`

- A _Boolean_ specifying whether to remove the connection between the grid point and the rotation RX of the bar at end B.
- The default value is _False_.

### `bDataPinB4`

- A _Boolean_ specifying whether to remove the connection between the grid point and the rotation RY of the bar at end B.
- The default value is _False_.

### `bDataPinB5`

- A _Boolean_ specifying whether to remove the connection between the grid point and the rotation RZ of the bar at end B.
- The default value is _False_.

### `dlDataOffset0`

- A _List of Double_ specifying the offset vector of end point A.
- The default value is [DFLT_DBL, DFLT_DBL, DFLT_DBL].

### `dlDataOffset1`

- A _List of Double_ specifying the offset vector of end point B.
- The default value is [DFLT_DBL, DFLT_DBL, DFLT_DBL].

### `iLocalLengthUnit`

- An _Integer_ specifying the local unit as the units of length measurement. Possible values are 0, 1, 2, 3 and 4 that correspond to _mm_, _m_, _ft_, _in_, and _cm_.
- The default value is 0.

### `iLocalMassUnit`

- An _Integer_ specifying the local unit as the units of mass measurement. Possible values are 0, 1 and 2 that correspond to _t_, _kg_, and _kgf\*s^2/mm_.
- The default value is 0.

### `crlTargets`

- A _List of Cursor_ specifying the entities to be applied the Bar property. Possible targets are Bar Part, Edge, and 1D Element. The _crlTargets_ and _crEdit_ arguments are mutually exclusive. One of them must be specified.
- The default value is [].

### `crEdit`

- A _Cursor_ specifying the existing Bar property. If this argument is not _None_, the specified Bar property will be modified. Otherwise, a new Bar property will be created. The _crlTargets_ and _crEdit_ arguments are mutually exclusive. One of them must be specified.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created bar property.

## Sample Code

```psj {16,17,18,19,20,21,22,23,24,25,26}
Geometry.Part.Cube()

Properties.Material.Add("Structural_Steel", 
                        [Density([(DENSITY, 
                                   7.85e-09)]),
                         Elastic([(YOUNGS_MODULUS, 
                                   200000.0), 
                                  (POISSONS_RATIO, 
                                   0.3)])])

Properties.Section.AddGeneral(strName="Circle", 
                              iSecGenType=2, 
                              dDsecGensizeT1=0.0002)

created_prop = Properties.BAR(strName="BAR2", 
                              iPropertyId=2, 
                              iPropertyColor=15383527, 
                              crCrossSection=SectionGeneral(1), 
                              crMaterial=Material(1), 
                              dSectionArea=1.25664e-07, 
                              dlSectionOrientation=[1.0, 0.0, 0.0], 
                              dlInertiaMoment=[1.257e-15, 1.257e-15, 0.0], 
                              dTorionalConst=2.513e-15, 
                              dShearAreaFactorY=0.9, 
                              dShearAreaFactorZ=0.9, 
                              dStressRecoveryCoeffCy=0.0002, 
                              dStressRecoveryCoeffCz=0.0, 
                              dStressRecoveryCoeffDy=0.0, 
                              dStressRecoveryCoeffDz=0.0002, 
                              dStressRecoveryCoeffEy=-0.0002, 
                              dStressRecoveryCoeffEz=0.0, 
                              dStressRecoveryCoeffFy=0.0, 
                              dStressRecoveryCoeffFz=-0.0002, 
                              crlTargets=[Edge(19)])

JPT.Debugger(created_prop)
```
