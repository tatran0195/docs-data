---
id: Geometry-Transform-Rotation
title: Geometry.Transform.Rotation()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Rotate given parts by the specified angle
---

## Description

Rotate given parts by the specified angle.

## Syntax

```psj
Geometry.Transform.Rotation(...)
```

Macro: [RotateBody](../../macro/geometry/RotateBody)

Ribbon: <menuselection>Geometry &#187; Transform &#187; Rotation</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the parts to be rotated.
- The default value is [].

### `posCenter`

- A _List_ specifying the center position of rotation.
- The default value is [0,0,0].

### `vecAxis`

- A _List_ specifying the axis of rotation.
- The default value is [1,0,0].

### `dAngle`

- A _Double_ specifying the rotation angle.
- The default value is 0.

### `bCreateNewPart`

- A _Boolean_ specifying whether to copy a new one and perform the transform operation.
- The default value is _False_.

### `bCopyLBC`

- A _Boolean_ specifying whether to copy load boundary condition of the original part to rotation part. This argument will be ignored if _bCreateNewPart=False_.
- The default value is _False_.

### `bCopyProperty`

- A _Boolean_ specifying the option that copy property of the original part to rotation part. This argument will be ignored if _bCreateNewPart=False_.
- The default value is _False_.

### `iCopyCount`

- An _Integer_ specifying the number of copy parts. This argument will be ignored if _bCreateNewPart=False_.
- The default value is 1.

### `bMergeNode`

- A _Boolean_ specifying whether to merge nodes between the original part and the transformed one. This argument will be ignored if _bCreateNewPart=False_.
- The default value is _False_.

### `dTol`

- A _Double_ specifying the merge tolerance. This argument should be specified when _bMergeNode=True_.
- The default value is 1.0e-5.

### `bCopyReference`

- A _Boolean_ specifying whether to copy references from the existing part to the created parts or not.
- The default value is _False_.
- 
## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {3,4,5,6,7,8}
Geometry.Part.Cube()

rotate_status = Geometry.Transform.Rotation(crlParts=[Part(1)], 
                                            vecAxis=[0.0, 0.001, 0.0],
                                            dAngle=0.5,
                                            bCreateNewPart=True, 
                                            iCopyCount=3,
                                            dTol=1e-05)

JPT.Debugger(rotate_status)
```
