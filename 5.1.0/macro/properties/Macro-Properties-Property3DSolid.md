---
id: Property3DSolid
title: Property3DSolid()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create property 3D solid

## Syntax

```psj
Property3DSolid(string Name, int Id, color propertyColor, Cursor Material, int CordM, int iN, int OutLoc,
    int ISOP, int iFLflag, int ModifiedElem, int ModifiedElemADVC, bool HasDynaRemesh,
    double DynaRemeshValMin, double DynaRemeshValMax, int HGType, int DispHG,
    Cursor[] Target, Cursor crEdit, int FLG)
```

## Inputs

### `1. string`

Name Property 3d solid

### `2. Int`

ID

### `3. Color`

Color of the property.

### `4. Cursor`

Material

### `5. Int`

Material coordinate [0:blank; 1:Element CS; 2:Global]

### `6. Int`

Integrating network [0:blank; 1:TWO; 2:THREE; 3:BUBBLE]

### `7. Int`

Output location [0:blank; 1:GAUSS; 2:GRID]

### `8. Int`

Integrating schema[0:blank; 1:REDUCED; 2:FULL]

### `9. Int`

Fluid element flag[0:blank; 1:PFLUID; 2:SMECH]

### `10. Int`

A bitmask-type flag used to switch the modified element type (Abaqus solver).
  - 0 : Don't use any Modified element (binary 000000)
  - 1 : Using the Hybrid element (binary 000001)
  - 2 : Using the Incompatible element (binary 000010)
  - 4 : Using the Modified element (binary 000100)
  - 8 : Using the Degenerate Integral element (binary 001000)
  - 16 : Using the Coupled Temp-Disp element (binary 100000)
  - 32 : Using the Acoustic solid element (binary 100000)

### `11. Int`

A bitmask-type flag used to switch the modified element type (ADVC solver). Based on the specified value, the element formulation and handling within the mesh are switched.
  - 0 : Don't use any Modified element (binary 000000)
  - 2 : Using the Non-conforming element (binary 000010)
  - 4 : Using the Modified element (binary 000100)
  - 8 : Using the Degenerate Integral element (binary 001000)
  - 256 : Using the First-order solid element (binary 100000000)
  - 512 : Using the Incompatible solid element (binary 1000000000)
  - 1024: Using the u-p formulation solid element (binary 10000000000)
  
### `12. Bool`

Has Dyna Remesh flag true = 1, false = 0

### `13. Double`

Remesh [Min Edge Length]

### `14. Double`

Remesh[Max Edge Length]

### `15. Int`

Hourglass Type [Use Default;Enhanced;Stiffness]

### `16. double`

Displacement Hourglass

### `17. Cursor[]`

Target list

### `18. Cursor`

Edit target (3D Property)

### `19. Int`

FLG

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Property3DSolid("Solid Property 1", 1, 16131973, 22:1, -2, 0, 0, 0, 0, 0, 0, 0,
    1.79769e+308, 1.79769e+308, 0, 1.79769e+308, [3:1], 0:0, -1)
```
