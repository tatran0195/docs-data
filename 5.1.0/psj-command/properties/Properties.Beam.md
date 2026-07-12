---
id: Properties-Beam
title: Properties.Beam()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Apply beam property on the selected entities
---

## Description

Apply beam property on the selected entities.

## Syntax

```psj
Properties.Beam(...)
```

Ribbon: <menuselection>Properties &#187; Beam</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of the new property.
- The default value is "BEAM1".

### `iPropertyColor`

- An _Integer_ specifying the color of the created property.

### `crCrossSection`

- A _Cursor_ specifying the cross-sectional in the library. The _crCrossSection_ and _iShapeDataType_ arguments are mutually exclusive. One of them must be specified. Two section types are listed as below:
  - _SectionGeneral()_: The general cross-sectional shape.
  - _SectionLibrary()_: The cross-sectional shape library of Nastran.
- The default value is _None_.

### `iShapeDataType`

- An _Integer_ specifying the shape data type.
- The default value is 0.

### `crMaterial`

- A _Cursor_ specifying the material will be applied for Beam.
- The default value is _None_.

### `dSectionArea`

- A _Double_ specifying the area of beam cross-section. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

### `dlSectionOrientation`

- A _List of Double_ specifying the orientation of beam cross-section.
- The default value is [0,0,0].

### `dlInertiaMoment`

- A _List of Double_ specifying the three components area moments of inertia, expressed in the principal axis of the BEAM. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is [0,0,0].

### `dTorsionalConst`

- A _Double_ specifying the torsion constant which is involved in the relationship between angle of twist and applied torque along the axis of the beam. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

### `dNSM`

- A _Double_ specifying the nonstructural mass per unit length which is a contribution to the model mass from features that have negligible structural stiffness. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dNSMA`

- A _Double_ specifying the nonstructural mass per unit length at end A. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dNSMB`

- A _Double_ specifying the nonstructural mass per unit length at end B. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dNSMNode1`

- A _Double_ specifying y-coordinate of center of gravity of nonstructural mass for end A. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dNSMNode2`

- A _Double_ specifying z-coordinate of center of gravity of nonstructural mass for end A. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dNSMNode3`

- A _Double_ specifying y-coordinate of center of gravity of nonstructural mass for end B. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dNSMNode4`

- A _Double_ specifying z-coordinate of center of gravity of nonstructural mass for end B. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dShearStiffnessFactorK1`

- A _Double_ specifying the area factors for shear for plane 1. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

### `dShearStiffnessFactorK2`

- A _Double_ specifying the area factors for shear for plane 2. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

### `dShearAreaReliefS1`

- A _Double_ specifying the shear relief coefficient due to taper for plane 1. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dShearAreaReliefS2`

- A _Double_ specifying the shear relief coefficient due to taper for plane 2. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dWrapCoeff1`

- A _Double_ specifying the warping coefficient for end A. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dWrapCoeff2`

- A _Double_ specifying the warping coefficient for end B. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dNA1`

- A _Double_ specifying the y-coordinate of neutral axis for end A. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dNA2`

- A _Double_ specifying the z-coordinate of neutral axis for end A. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dNA3`

- A _Double_ specifying the y-coordinate of neutral axis for end B. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dNA4`

- A _Double_ specifying the z-coordinate of neutral axis for end B. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT_DBL.

### `dStressRecoveryCoeffCy`

- A _Double_ specifying the stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point C at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

### `dStressRecoveryCoeffCz`

- A _Double_ specifying the stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point C at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

### `dStressRecoveryCoeffDy`

- A _Double_ specifying the stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point D at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

### `dStressRecoveryCoeffDz`

- A _Double_ specifying the stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point D at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

### `dStressRecoveryCoeffEy`

- A _Double_ specifying the stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point E at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

### `dStressRecoveryCoeffEz`

- A _Double_ specifying the stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point E at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

### `dStressRecoveryCoeffFy`

- A _Double_ specifying the stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point F at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

### `dStressRecoveryCoeffFz`

- A _Double_ specifying the stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point F at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

### `bPinA1`

- A _Boolean_ specifying whether to remove the connection between the grid point and the translation UX of the BEAM at end A.
- The default value is _False_.

### `bPinA2`

- A _Boolean_ specifying whether to remove the connection between the grid point and the translation UY of the BEAM at end A.
- The default value is _False_.

### `bPinA3`

- A _Boolean_ specifying whether to remove the connection between the grid point and the translation UZ of the BEAM at end A.
- The default value is _False_.

### `bPinA4`

- A _Boolean_ specifying whether to remove the connection between the grid point and the rotation RX of the BEAM at end A.
- The default value is _False_.

### `bPinA5`

- A _Boolean_ specifying whether to remove the connection between the grid point and the rotation RY of the BEAM at end A.
- The default value is _False_.

### `bPinA6`

- A _Boolean_ specifying whether to remove the connection between the grid point and the rotation RZ of the BEAM at end A.
- The default value is _False_.

### `bPinB1`

- A _Boolean_ specifying whether to remove the connection between the grid point and the translation UX of the BEAM at end B.
- The default value is _False_.

### `bPinB2`

- A _Boolean_ specifying whether to remove the connection between the grid point and the translation UY of the BEAM at end B.
- The default value is _False_.

### `bPinB3`

- A _Boolean_ specifying whether to remove the connection between the grid point and the translation UZ of the BEAM at end B.
- The default value is _False_.

### `bPinB4`

- A _Boolean_ specifying whether to remove the connection between the grid point and the rotation RX of the BEAM at end B.
- The default value is _False_.

### `bPinB5`

- A _Boolean_ specifying whether to remove the connection between the grid point and the rotation RY of the BEAM at end B.
- The default value is _False_.

### `bPinB6`

- A _Boolean_ specifying whether to remove the connection between the grid point and the rotation RZ of the BEAM at end B.
- The default value is _False_.

### `dlOffsetA`

- A _List of Double_ specifying the offset vector of end point A.
- The default value is [DFLT_DBL,DFLT_DBL,DFLT_DBL].

### `dlOffsetB`

- A _List of Double_ specifying the offset vector of end point B.
- The default value is [DFLT_DBL,DFLT_DBL,DFLT_DBL].

### `iLengthUnit`

- An _Integer_ specifying the local unit as the units of length measurement. Possible values are 0, 1, 2, 3 and 4 that correspond to _mm_, _m_, _ft_, _in_, and _cm_.
- The default value is 0.

### `iMassUnit`

- An _Integer_ specifying the local unit as the units of mass measurement. Possible values are 0, 1 and 2 that correspond to _t_, _kg_, and _kgf\*s^2/mm_.
- The default value is 0.

### `crlTargets`

- A _List of Cursor_ specifying the entities to be applied the BEAM property. Possible targets are BEAM, Edge, 1D Element, and Node. The _crlTargets_ and _crEdit_ arguments are mutually exclusive. One of them must be specified.
- The default value is [].

### `crEdit`

- A _Cursor_ specifying the existed Beam property to modify it. This option uses only for editing property purpose.
- The default value is _None_.

### `bTapped`

- A _Boolean_ specifying whether the cross-sectional performance should be changed with node position of the beam element.
- The default value is _False_.

### `dTapArea`

- A _Double_ specifying the area of tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT_DBL.

### `dlVecTapInertia`

- A _Double List_ specifying the three components area moments of inertia of tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is [DFLT_DBL,DFLT_DBL,DFLT_DBL].

### `dTapTorConst`

- A _Double_ specifying the torsional constant of tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT_DBL.

### `dTapNSM`

- A _Double_ specifying the nonstructural mass per unit length of tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT_DBL.

### `dTapStressRecoveryCoeffCy`

- A _Double_ specifying the stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point C at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT_DBL.

### `dTapStressRecoveryCoeffCz`

- A _Double_ specifying the stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point C at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT_DBL.

### `dTapStressRecoveryCoeffDy`

- A _Double_ specifying the stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point D at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT_DBL.

### `dTapStressRecoveryCoeffDz`

- A _Double_ specifying the stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point D at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT_DBL.

### `dTapStressRecoveryCoeffEy`

- A _Double_ specifying the stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point E at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT_DBL.

### `dTapStressRecoveryCoeffEz`

- A _Double_ specifying the stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point E at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT_DBL.

### `dTapStressRecoveryCoeffFy`

- A _Double_ specifying the stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point F at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT_DBL.

### `dTapStressRecoveryCoeffFz`

- A _Double_ specifying the stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point F at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT_DBL.

### `iIntePtNum`

- An _Integer_ specifying the integration points of the Beam element.
- The default value is DFLT_INT.

## Return Code

A _Cursor_ specifying the created beam property.

## Sample Code

```psj
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

created_prop = Properties.Beam(strName="BEAM1",
                               iPropertyColor=3986571, 
                               crCrossSection=SectionGeneral(1), 
                               crMaterial=Material(1), 
                               dSectionArea=1.25664e-07, 
                               dlSectionOrientation=[1.0, 
                                                     0.0, 
                                                     0.0], 
                               dlInertiaMoment=[1.257e-15, 
                                                1.257e-15, 
                                                0.0], 
                               dTorsionalConst=2.513e-15, 
                               dShearStiffnessFactorK1=0.9, 
                               dShearStiffnessFactorK2=0.9, 
                               dStressRecoveryCoeffCy=0.0002, 
                               dStressRecoveryCoeffDz=0.0002, 
                               dStressRecoveryCoeffEy=-0.0002, 
                               dStressRecoveryCoeffFz=-0.0002, 
                               crlTargets=[Edge(18)])

JPT.Debugger(created_prop)
```
