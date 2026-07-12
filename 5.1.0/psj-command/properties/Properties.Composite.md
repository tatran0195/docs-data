---
id: Properties-Composite
title: Properties.Composite()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create 2D Composite Material Shell Property
---

## Description

Define a shell property of 2D composite material.

## Syntax

```psj
Properties.Composite(...)
```

Ribbon: <menuselection>Properties &#187; Composite</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of the new property.
- The default value is "ComMatShell1".

### `iPropertyColor`

- An _Integer_ specifying the color of the new property.
- The default value is "".

### `iFT`

- An _Integer_ specifying the Failure Theory for composite materials:
  - 0: No Failure Theory is specified.
  - 1: The Hill theory.
  - 2: The Hoffman theory.
  - 3: The Tsai-Wu theory.
  - 4: The Maximum Strain theory.
- The default value is 0.

### `dGE`

- A _Double_ specifying the Structural Damping coefficient.
- The default value is DFLT_DBL.

### `iLAM`

- An _Integer_ specifying the Laminate options:

  - 0: Not specified - All plies must be specified and all stiffness terms are developed.
  - 1: "SYM" - Only plies on one side of the laminate centerline are specified. The plies are numbered starting with 1 for the bottom ply. If the laminate contains an odd number of plies, then model the center ply as half the thickness of the actual center ply.
  - 2: "MEM" - All plies must be specified, but only membrane terms (MID1 on the derived PSHELL entry) are computed.
  - 3: "BEND" - All plies must be specified, but only bending terms (MID2 on the derived PSHELL entry) are computed.
  - 4: "SMEAR" - All plies must be specified, stacking sequence is ignored, MID1=MID2 on the derived PSHELL entry and MID3, MID4 and TS/T and 12I/T\*\*3 terms are set to zero.
  - 5: "SMCORE" - Face plies on one side of the laminate and the core are specified to define a laminate that is symmetric about the midplane of the core. The core is specified last. When calculating face sheet stiffness, stacking sequence of the face sheets is ignored.

- The default value is 0.

### `crMaterial`

- A _Cursor_ specifying the material will be applied for composite property.
- The default value is _None_.

### `dNSM`

- A _Double_ specifying the non-structural mass per unit length which is a contribution to the model mass from features that have negligible structural stiffness.
- The default value is DFLT_DBL.

### `iPID`

- An _Integer_ specifying the property identification number. This number must be unique with respect to all other property identification numbers.
- The default value is 0.

### `dSB`

- A _Double_ specifying the allowable shear stress of the bonding material (allowable interlaminar shear stress). Required if _iFT_ is also specified.
- The default value is DFLT_DBL.

### `iSOUT`

- An _Integer_ specifying whether to control individual ply stress and strain print or punch output.

  - 0: Not specified - Not control individual ply stress and strain print or punch output
  - 1: NO - Not control individual ply stress and strain print or punch output
  - 2: YES - Control individual ply stress and strain print or punch output

- The default value is 0.

### `dTREF`

- A _Double_ specifying the Reference temperature.
- The default value is DFLT_DBL.

### `dZ0`

- A _Double_ specifying the laminate offsets.
- The default value is DFLT_DBL.

### `dZOFF`

- A _Double_ specifying the amount of offset of the laminate.
- The default value is DFLT_DBL.

### `crlTargets`

- A _List of Cursor_ specifying the entities to be applied to the composite property.
- The _crlTargets_ and _crCompositeProperty_ arguments are mutually exclusive (one of them must be specified).
- The default value is [].

### `crCompositeProperty`

- A _Cursor_ specifying the existing Composite Property.
  - If this argument is not _None_, the specified Composite Property will be modified.
  - Otherwise, a new Composite Property will be created.
- The _crlTargets_ and _crCompositeProperty_ arguments are mutually exclusive (one of them must be specified).
- The default value is _None_.

### `crLocalCS`

- A _Cursor_ specifying the local coordinate system used to define the material axis of the element.
- It must be specified if the specified _iOrientationMethod_ is 1 (Coordinate System).
- The default value is _None_.

### `iOrientationMethod`

- An _Integer_ specifying method to define the material axis of the element.
  - 0: Theta - Use the _dlOrientationVector_ value.
  - 1: Coordinate System - Use the coordinate system _crLocalCS_. The X-axis of the coordinate system is projected to the element plane.
- The default value is 0.

### `dlOrientationVector`

- A _Vector_ specifying orientation angle of the longitudinal direction of each ply with the material axis of the element.
- It must be specified if the specified _iOrientationMethod_ is 0 (Theta).
- The default value is [DFLT_DBL, DFLT_DBL, DFLT_DBL].

## Return Code

A _Cursor_ specifying the newly created or the modified Composite Property.

## Sample Code

```psj {4-5}
Geometry.Part.Cube()
Properties.Material.Add("Structural_Steel", [Density([(DENSITY, 7.85e-09)]),
    Elastic([(YOUNGS_MODULUS, 200000.0), (POISSONS_RATIO, 0.3)])])
Properties.Composite(strName="ComMatShell1", iPropertyColor=16131973, crMaterial=Material(1),
    iPID=1, crlTargets=[Face(26)])
```
