---
id: CmdPostContourSettings
title: CmdPostContourSettings()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Contour setting.

## Syntax

```psj
CmdPostContourSettings(int Contour, int ContourType, int MaxMinType, float MaxUser, float MinUser, float MaxTotal, float MinTotal, 
int SpectrumType, color UpperColor, color LowerColor, color FrameColor, string strColors, int Log, bool ShowBlankValueAs0, bool OptimizedShape, , float contours, color NoResult)
```
## Inputs
### `1. int  `

Step number

### `2. int  `

ContourType

### `3. int  `

Max Min Type 
0: Visible Entity, 1: Total Entity, 2: User Define, 3: Multiple Result

### `4. float  `

Maximum value.

### `5. float  `

Minimum value.

### `6. float  `

Total maximum value.

### `7. float  `

Total Minimum value.

### `8. int  `

Spectrum Type

### `9. color  `

Out of Maximum color

### `10. color  `

Out of Minimum color

### `11. color  `

Contour Frame Color

### `12. string  `

Colors

### `13. int  `

Log type

### `14. bool  `

Show blank value as 0 flag.

### `15. bool  `

Optimization Toolkit flag.

### `16. float []  `

Contour step value.

### `17. color []  `

No Result color.

### `18. int`

User Define Option selection status.
-1 :Without User Define option.
0:User Define with Fixed option.
1:User Define with Interpolate option.

### `19. int []`

Set markups for three most recently changed entries in the table.

### `20. bool`

(Will change)

### `20. bool`

Enables to display color contour on Rigid/Spring elements for transltaion results.

### `21. bool`

Enables to display Rigid/Spring elements by specified color for transltaion results.

### `22. color`

Color of Rigid/Spring elements

## Returint Code

Nothing.

## Sample Code

```psj
CmdPostContourSettings(10, 1, 0, 3.8698804379,  0.0000000000,  3.8698804379,  0.0000000000, 2, 255, 16711680, 65535, [], 0, 0, 0, [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0], 8421504)
```
