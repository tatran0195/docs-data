---
id: Geometry-Transform-Scaling
title: Geometry.Transform.Scaling()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Resize an part about its centroid or a coordinate system. It can resize different dimensions at different scales
---

## Description

Resize an part about its centroid or a coordinate system. It can resize different dimensions at different scales.

## Syntax

```psj
Geometry.Transform.Scaling(...)
```

Macro: [ScaleBody](../../macro/geometry/ScaleBody)

Ribbon: <menuselection>Geometry &#187; Transform &#187; Scaling</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the parts to be scaled.
- This is a required input.

### `dlScaleVector`

- A _List of Double_ specifying the scale vector. It defines how much scaling is done in each direction.
- The default value is [1.0,1.0,1.0].

### `dlScaleCenter`

- A _List of Double_ specifying the scale center. It defines a point about which the given part figure scales.
- The default value is [0.0,0.0,0.0].

### `crCoordinate`

- A _Cursor_ specifying the coordinate system.
- The default value is _None_.

### `bCreateNew`

- A _Boolean_ specifying whether to create new part or attach to original parts.
- The default value is _False_.

### `bCopyLbc`

- A _Boolean_ specifying whether to copy load boundary condition of original part to scaled part.
- The default value is _False_.

### `bCopyProperty`

- A _Boolean_ specifying whether to copy property of original part to scaled part.
- The default value is _False_.

### `bUsePartCenter`

- A _Boolean_ specifying whether to use original part center as scaled center.
- The default value is _True_.

### `bCopyReference`

- A _Boolean_ specifying whether to copy references from the existing part to the created parts or not.
- The default value is _False_.
  
## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {3,4,5,6,7}
Geometry.Part.Cube()

scaling_status = Geometry.Transform.Scaling(crlParts=[Part(1)], 
                                            dlScaleVector=[1.5, 
                                                           0.5, 
                                                           0.5], 
                                            bCreateNew=True)

JPT.Debugger(scaling_status)
```
