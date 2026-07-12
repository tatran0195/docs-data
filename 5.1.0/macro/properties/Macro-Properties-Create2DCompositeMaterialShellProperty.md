---
id: Create2DCompositeMaterialShellProperty
title: Create2DCompositeMaterialShellProperty()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create property 2D composite material shell

## Syntax

```psj
Create2DCompositeMaterialShellProperty(String m_strName, color propertyColor, ??, ??, ??, Cursor ?, ??, int m_ulId, 
    Cursor m_crMatShear,Cursor m_crMatCoupl,double m_matOrient[0],double m_matOrient[1],
    double m_matOrient[2],double m_dThickness,double m_dBendStiff,double m_dThickRatio,
    double m_dNSM,double m_dFiberDist[0],double m_dFiberDist[1],double m_dPlateOff,
    int m_iItgPts,int m_matOrientType,Cursor m_crLocalCS,Cursor[] taTarget,Cursor crEdit,
    int duplicateOpt)
```
Create2DCompositeMaterialShellProperty("ComMatShell2", 13708224, 0, 1.79769e+308, 0, 22:50000000, 1.79769e+308, 3, 1.79769e+308, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, [6:24], 0:0, 0:0, 0, [1.7976931e+308, 1.7976931e+308, 1.7976931e+308])

## Inputs

### `1. String`

Name of property 2D composite material shell

### `2. Color`

Color of the property.

### `. Int`

ID of property 2D shell

### `4. Cursor`

Cursor of membrane material

### `5. Cursor`

Cursor of bending material

### `6. Cursor`

Cursor of shear material

### `7. Cursor`

Cursor of coupling material

### `8. Double`

Theta[degree]

### `9. Double`

Not used

### `10. Double`

Not used

### `11. Double`

Thickness

### `12. Double`

Bending stiffness

### `13. Double`

Thickness ratio

### `14. Double`

Nonstructural mass

### `15. Double`

Fiber dist 1

### `16. Double`

Fiber dist 2

### `17. Double`

Plate offset

### `18. Int`

No SHELL Integration points

### `19. Int`

Material orientation by[0: Theta; 1: coordinate system]

### `20. Cursor`

Local coordinate system

### `21. Cursor[]`

Targets

### `22. Cursor`

Edit cursor

### `23. Int`

Answer of message box when targets are duplicated[0: targets are not duplicated; 2: cancel; 6: yes; 7: no]

### `24. Int`

Status of ERP check box.[0: OFF, 1: ON]

### `25. String`

Panel Label Name.

### `26. Int`

Panel Label ID.

### `27. Int`

The number of temperature layers.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Create2DCompositeMaterialShellProperty(
    "ComMatShell1", 12901750, 0, 1.79769e+308, 0, 22:50000000, 1.79769e+308, 
    2, 1.79769e+308, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, 
    [6:22], 0:0, 0:0, 0, [1.7976931e+308, 1.7976931e+308, 1.7976931e+308])
```
